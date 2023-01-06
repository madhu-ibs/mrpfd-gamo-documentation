# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MRPFD-GAMO'
copyright = '2023 | All Rights Reserved | Impressico Business Solutions'
author = 'Impressico Business Solutions'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
html_show_sphinx = False
html_show_sourcelink = False

html_theme_options = {
    'display_version': False}
html_context = {
"display_github": False,
"last_updated": True,
"commit": False,
}
