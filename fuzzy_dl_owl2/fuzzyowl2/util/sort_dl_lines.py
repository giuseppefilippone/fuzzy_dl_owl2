from __future__ import annotations

import re
from collections.abc import Iterable
from itertools import groupby
from fuzzy_dl_owl2.fuzzydl.util import Util

# Total syntax order induced by the PDF:
# first by page number, then by top-to-bottom order on that page.
# These are regexes. They are intentionally anchored to parenthesized fuzzyDL
# commands where possible, to avoid collisions such as feature-level
# (functional F) vs role-level (functional R).

FUZZYDL_PDF_ORDER: list[str] = [
    # Page 1
    r"^\s*\(\s*define-fuzzy-logic\b",
    r"^\s*\(\s*define-truth-constant\b",
    r"^\s*\(\s*define-modifier\b.*\blinear-modifier\b",
    r"^\s*\(\s*define-modifier\b.*\btriangular-modifier\b",
    # Page 2
    r"^\s*\(\s*define-fuzzy-concept\b.*\bcrisp\s*\(",
    r"^\s*\(\s*define-fuzzy-concept\b.*\bleft-shoulder\s*\(",
    r"^\s*\(\s*define-fuzzy-concept\b.*\bright-shoulder\s*\(",
    r"^\s*\(\s*define-fuzzy-number\b.*\btriangular\s*\(",
    r"^\s*\(\s*define-fuzzy-concept\b.*\btrapezoidal\s*\(",
    r"^\s*\(\s*define-fuzzy-concept\b.*\blinear\s*\(",
    r"^\s*\(\s*define-fuzzy-concept\b.*\bmodified\s*\(",
    r"^\s*\(\s*define-fuzzy-number-range\b",
    r"^\s*\(\s*define-fuzzy-number\b",
    # Feature declarations.
    # This is still ambiguous with role-level (functional R) unless you know
    # the identifier is a feature. If your input contains both, use a context
    # flag or separate preclassification.
    r"^\s*\(\s*functional\b",
    r"^\s*\(\s*range\b.*\*integer\*",
    r"^\s*\(\s*range\b.*\*real\*",
    r"^\s*\(\s*range\b.*\*string\*",
    r"^\s*\(\s*range\b.*\*boolean\*",
    # Page 3
    r"^\s*\(\s*constraints\b",
    r"^\s*\(\s*show-concrete-fillers\b",
    r"^\s*\(\s*show-concrete-fillers-for\b",
    r"^\s*\(\s*show-concrete-instance-for\b",
    r"^\s*\(\s*show-abstract-fillers\b",
    r"^\s*\(\s*show-abstract-fillers-for\b",
    r"^\s*\(\s*show-concepts\b",
    r"^\s*\(\s*show-instances\b",
    r"^\s*\(\s*show-variables\b",
    r"^\s*\(\s*show-language\b",
    r"^\s*\(\s*crisp-concept\b",
    r"^\s*\(\s*crisp-role\b",
    # Page 4 / 5 note area in the PDF text
    r"^\s*\(\s*define-fuzzy-similarity\b",
    r"^\s*\(\s*define-fuzzy-equivalence\b",
    # Page 5 axioms
    r"^\s*\(\s*define-primitive-concept\b",
    r"^\s*\(\s*define-concept\b",
    r"^\s*\(\s*instance\b",
    r"^\s*\(\s*related\b",
    r"^\s*\(\s*implies\b",
    r"^\s*\(\s*g-implies\b",
    r"^\s*\(\s*kd-implies\b",
    r"^\s*\(\s*l-implies\b",
    r"^\s*\(\s*z-implies\b",
    r"^\s*\(\s*equivalent-concepts\b",
    r"^\s*\(\s*disjoint\b",
    r"^\s*\(\s*disjoint-union\b",
    # Role-level range/domain and role properties.
    # Note: role-level range is syntactically indistinguishable from some
    # feature ranges unless the datatype marker *integer*, *real*, etc. is present.
    r"^\s*\(\s*range\b(?!.*\*(?:integer|real|string|boolean)\*)",
    r"^\s*\(\s*domain\b",
    r"^\s*\(\s*functional\b",
    r"^\s*\(\s*inverse-functional\b",
    r"^\s*\(\s*reflexive\b",
    r"^\s*\(\s*symmetric\b",
    r"^\s*\(\s*transitive\b",
    r"^\s*\(\s*implies-role\b",
    r"^\s*\(\s*inverse\b",
    # Page 6 queries
    r"^\s*\(\s*sat\?\b",
    r"^\s*\(\s*max-instance\?\b",
    r"^\s*\(\s*min-instance\?\b",
    r"^\s*\(\s*all-instances\?\b",
    r"^\s*\(\s*max-related\?\b",
    r"^\s*\(\s*min-related\?\b",
    r"^\s*\(\s*max-subs\?\b",
    r"^\s*\(\s*min-subs\?\b",
    r"^\s*\(\s*max-g-subs\?\b",
    r"^\s*\(\s*min-g-subs\?\b",
    r"^\s*\(\s*max-l-subs\?\b",
    r"^\s*\(\s*min-l-subs\?\b",
    r"^\s*\(\s*max-kd-subs\?\b",
    r"^\s*\(\s*min-kd-subs\?\b",
    r"^\s*\(\s*max-sat\?\b",
    r"^\s*\(\s*min-sat\?\b",
    r"^\s*\(\s*max-var\?\b",
    r"^\s*\(\s*min-var\?\b",
    r"^\s*\(\s*defuzzify-lom\?\b",
    r"^\s*\(\s*defuzzify-mom\?\b",
    r"^\s*\(\s*defuzzify-som\?\b",
    r"^\s*\(\s*bnp\?\b",
]

FUZZYDL_PDF_ORDER_RE: list[re.Pattern[str]] = [
    re.compile(pattern, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
    for pattern in FUZZYDL_PDF_ORDER
]


def find_fuzzydl_pdf_order_index(text: str) -> int:
    """
    Find the index of the first regex in FUZZYDL_PDF_ORDER that matches s.
    If no entry matches, return a large number so the item sorts at the end.
    """
    for index, pattern in enumerate(FUZZYDL_PDF_ORDER_RE):
        if pattern.search(text):
            Util.debug(
                f"Matched {text!r} to pattern {pattern.pattern!r} at index {index}"
            )
            return index
    Util.debug(f"No fuzzyDL PDF-order match for {text!r}")
    return 10**9


def sort_by_fuzzydl_pdf_order(
    values: Iterable[str],
    *,
    group_separator: str = "",
) -> list[str]:
    """
    Sort fuzzyDL statements by PDF order index, group equal-index items,
    and insert `group_separator` after each group.

    Unknown statements are placed at the end.
    """
    prepared: list[tuple[int, str]] = [
        (
            find_fuzzydl_pdf_order_index(value),
            value,
        )
        for value in values
    ]

    prepared.sort(key=lambda item: (item[0], item[1]))

    result: list[str] = []

    for index, group in groupby(prepared, key=lambda item: item[0]):
        group_items = [value for _, value in group]
        result.extend(group_items)
        result.append(group_separator)

    return result
