"""Poetry build hook: cythonize the fast DL parser into a native extension.

Poetry-core 2.x invokes this file as ``python build.py`` during
``pip install .`` / ``poetry build``. It must compile the extension
in-place next to its ``.py`` source so the wheel builder picks the
resulting ``.so`` up via ``find_files_to_add``.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from cffi import FFI
from Cython.Build import cythonize
from Cython.Compiler import Options as CythonOptions
from setuptools import Distribution, Extension
from setuptools.command.build_ext import build_ext

CythonOptions.docstrings = False
CythonOptions.fast_fail = True

HERE = Path(__file__).parent


# Only compile hot-path modules to reduce dlopen() overhead at import time.
# Non-hot-path modules stay as .py — they load faster as bytecode than as
# .so files, and don't benefit much from Cython.
CYTHON_SOURCES = (
    [
        (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "knowledge_base.py").as_posix(),
        (
            HERE / "fuzzy_dl_owl2" / "fuzzydl" / "general_concept_inclusion.py"
        ).as_posix(),
        (
            HERE / "fuzzy_dl_owl2" / "fuzzydl" / "primitive_concept_definition.py"
        ).as_posix(),
        (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "graph" / "digraph.py").as_posix(),
        (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "util" / "constants.py").as_posix(),
    ]
    + [
        p.as_posix()
        for p in (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "concept").glob("**/*.py")
        if not p.as_posix().endswith(
            "__init__.py"
        )  # and not "interface" in p.as_posix()
    ]
    + [
        p.as_posix()
        for p in (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "individual").glob("**/*.py")
        if not p.as_posix().endswith("__init__.py")
    ]
    + [
        p.as_posix()
        for p in (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "query").glob("**/*.py")
        if not p.as_posix().endswith("__init__.py")
    ]
    + [
        p.as_posix()
        for p in (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "milp").glob("**/*.py")
        if not p.as_posix().endswith("__init__.py")
    ]
    + [
        p.as_posix()
        for p in (HERE / "fuzzy_dl_owl2" / "fuzzydl" / "parser").glob("**/*.py")
        if not p.as_posix().endswith("__init__.py")
        and not p.as_posix().endswith("tokens.py")
        and not p.as_posix().endswith("generate.py")
        and not p.as_posix().endswith("tokenizer_handler.py")
        and not p.as_posix().endswith("dl_parser.py")
    ]
)

# CYTHON_SOURCES = [
#     f.as_posix()
#     for f in (HERE / "fuzzy_dl_owl2").glob("**/*.py")
#     if not f.as_posix().endswith("__init__.py")
#     and not "interface" in f.as_posix()
#     and not f.as_posix().endswith("/degree.py")
#     and not f.as_posix().endswith("/has_value_restriction.py")
#     and not f.as_posix().endswith("generate_tokens.py")
# ]

COMPILER_DIRECTIVES = {
    "boundscheck": False,
    "wraparound": False,
    "initializedcheck": False,
    "cdivision": True,
    "nonecheck": False,
    "infer_types": True,
    "language_level": 3,
    "embedsignature": False,
    # Cython 3 default is True: PEP 484 annotations get enforced as C-level
    # types, which rejects valid Optional/Union arguments at runtime (e.g.
    # OwaConcept(weights=None,...) raises "expected list, got NoneType").
    "annotation_typing": False,
}


# Directory that holds the lexer generator sources (``lexer_re2c.re`` /
# ``lexer_flex.l`` / ``tokens.h``) and where the ``_fdl_lexer`` extension is
# built so it ships inside the package.
LEXER_DIR = HERE / "fuzzy_dl_owl2" / "fuzzydl" / "parser" / "tokenizer"

# CFFI cdef shared by both backends — the C tokenizer's public surface.
_LEXER_CDEF = """
    size_t fdl_count_tokens(const char *buf, size_t len);
    size_t fdl_tokenize(const char *buf, size_t len,
                        int32_t *types, int32_t *starts, int32_t *lens);
"""


def make_lexer_exts() -> list[Extension]:
    """Generate the C tokenizer and return its extensions.

    Runs re2c on ``lexer_re2c.re`` (preferred) or flex on ``lexer_flex.l`` to
    produce the scanner ``.c``, then builds two extensions inside the
    ``fuzzy_dl_owl2.fuzzydl.parser`` package:

      * ``_fdl_lexer``  -- CFFI wrapper exposing the int32-array API
        (``fdl_count_tokens`` / ``fdl_tokenize``) used by ``tokens.py``.
      * ``_fdl_tuples`` -- Cython module whose ``tokenize_tuples(bytes)``
        builds the parser's 4-tuple stream in C, linking the same scanner.

    Returns ``[]`` (build continues) if no generator source is present or the
    required tool (re2c / flex) is not on PATH. The ``_fdl_tuples`` extension
    is only added when its ``.pyx`` is present.
    """

    # (generator source, tool, command to run)
    gen_c = (LEXER_DIR / "lexer_gen.c").as_posix()
    candidates = (
        ("lexer_re2c.re", "re2c", ["re2c", "-o", gen_c]),
        ("lexer_flex.l", "flex", ["flex", "-o", gen_c]),
    )
    for src, tool, cmd in candidates:
        if shutil.which(tool) is None:
            print(f"build_lexer: {tool} not on PATH, skipping {src}")
            continue

        output = subprocess.run(
            [sys.executable, (LEXER_DIR / "generate.py").as_posix(), tool],
            check=False,
            capture_output=True,
            text=True,
        )
        print(output.stdout.strip())
        if output.returncode != 0:
            print(
                f"build_lexer: generate.py failed for {tool} "
                f"(exit {output.returncode}):\n{output.stderr.strip()}"
            )

        src_path = LEXER_DIR / src
        if not src_path.is_file():
            # generate.py is the only producer of the scanner source; without
            # it the backend cannot run, so fall through to the next candidate
            # (or skip the lexer entirely) instead of crashing the wheel build.
            print(f"build_lexer: {src} not present, skipping {tool}")
            continue

        print(f"build_lexer: generating tokenizer from {src} ({tool})")
        subprocess.run([*cmd, src_path.as_posix()], check=True)

        exts: list[Extension] = []

        # 1. CFFI _fdl_lexer (int32-array API for tokens.py).
        ffibuilder = FFI()
        ffibuilder.cdef(_LEXER_CDEF)
        with open(gen_c) as f:
            # Bare module name keeps CFFI from emitting a nested package tree;
            # the dotted package path is set on the Extension below.
            ffibuilder.set_source(
                "_fdl_lexer",
                f.read(),
                include_dirs=[LEXER_DIR.as_posix()],
                extra_compile_args=["-O3"],
            )
        wrapper_c = (LEXER_DIR / "_fdl_lexer.c").as_posix()
        ffibuilder.emit_c_code(wrapper_c)
        exts.append(
            Extension(
                "fuzzy_dl_owl2.fuzzydl.parser.tokenizer._fdl_lexer",
                sources=[wrapper_c],
                include_dirs=[LEXER_DIR.as_posix()],
                extra_compile_args=["-O3"],
            )
        )

        # 2. Cython _fdl_tuples (C tuple-builder), linking the same scanner .c.
        pyx = LEXER_DIR / "_fdl_tuples.pyx"
        if pyx.is_file():
            (tuples_ext,) = cythonize(
                [
                    Extension(
                        "fuzzy_dl_owl2.fuzzydl.parser.tokenizer._fdl_tuples",
                        sources=[pyx.as_posix(), gen_c],
                        include_dirs=[LEXER_DIR.as_posix()],
                        extra_compile_args=["-O3"],
                    )
                ],
                language_level=3,
                compiler_directives=COMPILER_DIRECTIVES,
                annotate=False,
            )
            exts.append(tuples_ext)
        else:
            print("build_lexer: _fdl_tuples.pyx absent, skipping tuple builder")

        return exts

    print("build_lexer: no lexer generator source available, skipping")
    return []


def build(setup_kwargs: dict | None = None) -> None:
    """Compile the Cython sources in-place.

    Also accepts a ``setup_kwargs`` mapping for backward compatibility
    with the historical poetry build-script signature; the mapping is
    populated with ``ext_modules`` so callers that still rely on it
    keep working.
    """

    ext_modules = cythonize(
        CYTHON_SOURCES,
        language_level=3,
        compiler_directives=COMPILER_DIRECTIVES,
        annotate=False,
    )

    # Append the re2c/flex-generated lexer extensions if their source is
    # present (CFFI _fdl_lexer + Cython _fdl_tuples).
    ext_modules.extend(make_lexer_exts())

    # Silence harmless Clang warnings on Cython-generated CYTHON_FALLTHROUGH
    # macros in switch cases that Clang's reachability analysis marks as dead.
    if sys.platform == "win32":
        extra = []  # cl.exe already uses /O2; rejects -Wno-*/-O3 (D8021)
    else:
        extra = [
            "-O3", # Maximum optimization
            "-Wno-unreachable-code-fallthrough"
        ]
    for ext in ext_modules:
        ext.extra_compile_args = list(ext.extra_compile_args or []) + extra

    if setup_kwargs is not None:
        setup_kwargs.update({"ext_modules": ext_modules, "zip_safe": False})

    dist = Distribution({"name": "fuzzy_dl_owl2", "ext_modules": ext_modules})
    cmd = build_ext(dist)
    cmd.inplace = 1
    cmd.ensure_finalized()
    cmd.run()


if __name__ == "__main__":
    build()
