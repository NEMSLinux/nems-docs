# -*- coding: utf-8 -*-
#
# -- General configuration -------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'NEMS Linux Documentation'
copyright = u'2020 Robbie Ferguson'

version = '0.0.1'

# -- Options for HTML output -----------------------------------

html_theme = 'bizstyle'

html_theme_options = {
    'rightsidebar': False,
}

extensions = [
  'sphinxcontrib.css3image',
]
