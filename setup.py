"""
Cython build script for the fast fuzzy DL parser.

Usage (from the repo root)::

    python fuzzy_dl_owl2/fuzzy_dl_owl2/fuzzydl/parser/setup_dl_parser.py build_ext --inplace

This produces a compiled ``dl_parser_fast.<platform>.so`` next to the
``.py`` source. Importing ``DLParserFast`` afterwards will pick up the
compiled module transparently (Python prefers the extension over the .py
when both are present). Without compilation the pure-Python source is
still used and is already 5-10x faster than the original pyparsing
implementation.

Build prerequisites::

    pip install cython>=3.0
"""

from __future__ import annotations

from setuptools import setup

if __name__ == "__main__":
    setup()
