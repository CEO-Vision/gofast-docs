# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser

extensions = []
templates_path = ['/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx', 'templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
source_parsers = {
            '.md': CommonMarkParser,
        }
master_doc = 'index'
project = u'gofast-docs'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build', 'docs-gofast-users/doc-gofast-guide-utilisateurs*', 'docs-gofast-technical/release*']
pygments_style = 'sphinx'
htmlhelp_basename = 'gofast-docs'
html_theme = 'sphinx_rtd_theme'
file_insertion_enabled = False
latex_documents = [
  ('index', 'gofast-docs.tex', u'gofast-docs Documentation',
   u'', 'manual'),
]

language = 'fr'

locale_dirs = [
    'locale/',
]
gettext_compact = False
gettext_uuid = True

#make gettext
#sphinx-intl update -p _build/locale fr

