"""qubes-doc configuration file"""

import os
import sys
from pathlib import Path

# Append the path to custom extensions
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
  'sphinx.ext.autosectionlabel',  # Automatically generate section labels
  'sphinx.ext.intersphinx',  # Reference other doc projects
  'sphinxnotes.strike', # Add strike-through text support
  'sphinx_reredirects', # Manage redirects in the documentation
  'sphinxext.opengraph', # Add Open Graph meta tags for social media sharing
  'youtube_frame', # Embed YouTube videos
  'last_edition',
  'custom_menuselections',
]

# Redirects for specific URLs as fall back
redirects = {
    "user/hardware/hcl":
        "https://www.qubes-os.org/hcl/",
    "user/downloading-installing-upgrading/downloads:mirrors":
        "https://www.qubes-os.org/downloads/mirrors/",
    "developer/general/visual-style-guide":
        "https://www.qubes-os.org/doc/visual-style-guide/",
    "user/downloading-installing-upgrading/downloads":
        "https://www.qubes-os.org/downloads/",

    # user/templates/windows URLs
    "user/templates/windows/windows":
        "/user/templates/windows/",
    "user/templates/windows/windows-qubes-4-1":
        "qubes-windows.html",
    "user/templates/windows/windows-qubes-4-0":
        "qubes-windows.html",
    "user/templates/windows/qubes-windows-tools-4-1":
        "qubes-windows-tools.html",
    "user/templates/windows/qubes-windows-tools-4-0":
        "qubes-windows-tools.html",
    "user/templates/windows/migrate-to-4-1":
        "qubes-windows-migrate.html",
}

# -- -- Options for highlighting ---------------------------------------------

# Disable syntax highlighting
highlight_language = 'none'

# Set the Pygments style for syntax highlighting
pygments_style = 'sphinx'

# -- -- Options for source files ---------------------------------------------

# Patterns to exclude from the source directory
exclude_patterns = [
  '_*',
  '**/.*',
  '**/*.txt',
  'attachment',
  '.venv',
]

# -- -- Options for templating -----------------------------------------------

templates_path = ['_templates']

# -- Builder options ---------------------------------------------------------

# -- -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_title = f'{project} Documentation'

html_theme_options = {
  'style_external_links': True,
  'collapse_navigation': True,
}

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

html_static_path = ['_static']
html_css_files = ['css/custom.css']

html_use_opensearch = "https://doc.qubes-os.org"

html_logo = "attachment/icons/128x128/apps/qubes-logo-icon.png"
html_favicon = "attachment/icons/favicon-16x16.png"

# -- -- Options for the linkcheck builder ------------------------------------

linkcheck_anchors = False
linkcheck_ignore = [r'^https?://[^/\s]+\.onion']

# -- Extensions configuration ------------------------------------------------
# Prefix section labels with the document name
autosectionlabel_prefix_document = True

# Allows references to the docs in dev.qubes-os.org
# i.e.: :doc:`core-admin:libvirt`
intersphinx_mapping = {
    'core-admin': ('https://dev.qubes-os.org/projects/core-admin/en/latest/', None),
    'core-admin-client': ('https://dev.qubes-os.org/projects/core-admin-client/en/latest/', None),
    'core-qrexec': ('https://dev.qubes-os.org/projects/qubes-core-qrexec/en/stable/', None),
}
intersphinx_disabled_reftypes = ["*"]

# Open Graph image for social media sharing
ogp_image = "https://www.qubes-os.org/attachment/icons/qubes-logo-icon-name-slogan-fb.png"
# Disable Open Graph image alt text
ogp_image_alt = False

# -- HTML configuration ------------------------------------------------------


# -- -- Add 'Edit on GitHub' Link --------------------------------------------

html_context = {
    "display_github": True,
    "github_user": "QubesOs",
    "github_repo": "qubes-doc",
    "github_version": "main",
    "conf_py_path": "/",
}

# The onion site only mirrors the content of the documentation built as /en/latest/
if os.environ.get('READTHEDOCS_LANGUAGE') == 'en' and os.environ.get('READTHEDOCS_VERSION') == 'latest':
    html_context["onion_location"] = "http://doc.qubesosfasa4zl44o4tws22di6kepyzfeqv3tg4e3ztknltfxqrymdad.onion"

# -- -- Options for internationalisation -------------------------------------

# Directories containing translation files
locale_dirs = ['_translated']

gettext_compact = False

gettext_uuid = True

# -- -- Options for markup ---------------------------------------------------

# Define a block of reusable reStructuredText (reST) snippets, warnings etc. that Sphinx automatically appends to every source file before it is parsed
rst_epilog = """
.. |debian-codename| replace:: trixie
.. |debian-version| replace:: 13
.. |qubes-logo-icon| image:: /attachment/icons/128x128/apps/qubes-logo-icon.png
   :height: 1em
   :class: no-scaled-link
   :alt: Qubes logo icon
"""

# -- -- Options for the nitpicky mode ----------------------------------------

nitpicky = True
