# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('../src/listmode'))
sys.path.append('../src')



# -- Project information -----------------------------------------------------
project = 'listmode'
copyright = '2020, Timo Hilden'
author = 'Timo Hilden'

# The full version, including alpha/beta/rc tags
release = '0.5.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'rst2pdf.pdfbuilder'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for PDF output -------------------------------------------------
pdf_documents = [('manual/manual', 'Listmode User Manual', 'Listmode', 'Timo Hildén'),
                 ('autodocs/reference', 'Listmode Reference', 'Listmode', 'Timo Hildén')]
#pdf_documents = [('index', 'Listmode Manual', 'Listmode', 'Timo Hildén')]
# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx']
pdf_use_coverpage = True
pdf_break_level = 2
pdf_breakside = 'any'
