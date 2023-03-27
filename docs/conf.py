
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

project = 'fast-marching-square'
copyright = '2023, Vistor'
author = 'Vistor'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'numpydoc',
]

autosummary_generate = True
numpydoc_show_class_members = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
