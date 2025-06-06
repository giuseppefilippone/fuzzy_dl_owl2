# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Fuzzy Description Language Reasonear and Fuzzy OWL 2 ontology handler'
copyright = '2025, Giuseppe Filippone'
author = 'Giuseppe Filippone'
release = 'v1.0.8'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ['source/_templates']
exclude_patterns = []

# Optional: if you use numpy-style or Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# -- Options for LaTeX math rendering ---------------------------------

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ["source/_static"]
