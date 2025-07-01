# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MicroAgroBiome'
copyright = '2025, César Aguilar, Fernando Fontove-Herrera, David A. García-Estrada, Haydeé Contreras-Peruyero, Anton Pashkov, Shaday Guerrero-Flores, Nelly Sélem-Mojica'
author = 'César Aguilar, Fernando Fontove-Herrera, David A. García-Estrada, Haydeé Contreras-Peruyero, Anton Pashkov, Shaday Guerrero-Flores, Nelly Sélem-Mojica'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []
source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_theme = "classic"
# html_theme_options = {
#     "rightsidebar": "false",
#     "relbarbgcolor": "black"
# }
html_show_sourcelink = False
html_static_path = ['_static']
html_favicon = '_static/logo_MicroAgroBiome.png'  # Path to the favicon file
html_css_files = ['custom.css'] # Custom CSS file for additional styling (DAVID)