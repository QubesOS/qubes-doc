"""qubes-doc configuration file"""

import os
import sys
from pathlib import Path

sys.path.append(str(Path('_ext').resolve()))

# For the full list of options, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------

project = 'Qubes OS'
author = 'Qubes OS Project'
copyright = f'%Y, {author}'

# Warning: Sphinx's version and release differ from Qubes OS !

# The major project version, used as the replacement for the |version| default
# substitution. i.e. '4.3'
version = '4.2'

# The full version, including alpha/beta/rc tags
release = '4.2.4'


# -- General configuration ---------------------------------------------------

extensions = [
  'sphinx.ext.autosectionlabel',
  'sphinxnotes.strike',
  'sphinx_reredirects',
  'sphinxext.opengraph',
  'youtube_frame',
]

redirects = {
    "user/hardware/hcl":
        "https://www.qubes-os.org/hcl/",
    "user/downloading-installing-upgrading/downloads:mirrors":
        "https://www.qubes-os.org/downloads/mirrors/",
    "developer/general/visual-style-guide":
        "https://www.qubes-os.org/doc/visual-style-guide/",
    "developer/general/website-style-guide":
        "https://www.qubes-os.org/doc/website-style-guide/",
    "user/downloading-installing-upgrading/downloads":
        "https://www.qubes-os.org/downloads/",
    "developer/general/how-to-edit-the-documentation":
        "https://www.qubes-os.org/doc/how-to-edit-the-documentation/",
}


# -- -- Options for highlighting ---------------------------------------------

highlight_language = 'none'


# -- -- Options for source files ---------------------------------------------

exclude_patterns = [
  '_*',
  '**/.*',
  '**/*.txt'
  'attachment',
]


# -- Builder options ---------------------------------------------------------

# -- -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_title = f'{project} Documentation'

html_theme_options = {
  'style_external_links': True,
  'collapse_navigation': True,
}

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

html_static_path = ['attachment/doc']

html_use_opensearch = "https://doc.qubes-os.org"

html_logo = "attachment/icons/128x128/apps/qubes-logo-icon.png"
html_favicon = "attachment/icons/favicon-16x16.png"

# -- -- Options for the linkcheck builder ------------------------------------

linkcheck_anchors = False
linkcheck_ignore = [r'^https?://[^/\s]+\.onion']

# -- Extensions configuration ------------------------------------------------

autosectionlabel_prefix_document = True

ogp_image = "https://www.qubes-os.org/attachment/icons/qubes-logo-icon-name-slogan-fb.png"
ogp_image_alt = False

# -- HTML configuration ------------------------------------------------------


# -- -- Add 'Edit on GitHub' Link --------------------------------------------

html_context = {
    "display_github": True,
    "github_user": "QubesOs",
    "github_repo": "qubes-doc",
    "github_version": "rst",
    "conf_py_path": "/",
}

# -- -- Options for internationalisation -------------------------------------

locale_dirs = ['_translated']

gettext_compact = False

gettext_uuid = True
