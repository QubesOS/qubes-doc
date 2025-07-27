"""
  ReST directive for embedding Youtube and Vimeo videos.
  There are two directives added: ``youtube`` and ``vimeo``. The only
  argument is the video id of the video to include.
  Both directives have three optional arguments: ``height``, ``width``
  and ``align``. Default height is 281 and default width is 500.
  Example::
    .. youtube:: anwy2MPT5RE
      :height: 315
      :width: 560
      :align: left
  :copyright: (c) 2012 by Danilo Bargen.
  :license: BSD 3-clause
"""
from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives

# -- Project information -----------------------------------------------------

project = 'Qubes OS'
copyright = '2025, Qubes OS Project'
author = 'Qubes OS Project'

title = "Qubes Docs"
html_title = "Qubes Docs"

# The full version, including alpha/beta/rc tags
release = '4.3'

# -- General configuration ---------------------------------------------------

html_static_path = ['attachment/doc']
extensions = [
  'sphinx.ext.autosectionlabel',
  'sphinxnotes.strike',
  'sphinx_reredirects'
]

redirects = {
  "user/hardware/hcl": "https://www.qubes-os.org/hcl/",
  "user/downloading-installing-upgrading/downloads:mirrors":"https://www.qubes-os.org/downloads/mirrors/",
  "developer/general/visual-style-guide": "https://www.qubes-os.org/doc/visual-style-guide/",
  "developer/general/website-style-guide":"https://www.qubes-os.org/doc/website-style-guide/",
  "user/downloading-installing-upgrading/downloads":"https://www.qubes-os.org/downloads/",
  "developer/general/how-to-edit-the-documentation":"https://www.qubes-os.org/doc/how-to-edit-the-documentation/"
}

autosectionlabel_prefix_document = True

source_suffix = {
  '.rst': 'restructuredtext',
}
templates_path = ['_templates']

root_doc = "index"
exclude_patterns = [
  '_dev/*',
  'attachment/*',
  '**/*.txt'
]

html_theme = 'sphinx_rtd_theme'
# html_theme = 'default'
# html_theme = 'classic'

html_theme_options = {
  'externalrefs': True,
  'bgcolor': 'white',
  'linkcolor': '#99bfff',
  'textcolor': '#000000',
  'visitedlinkcolor': '#7b7b7b',
  'bodyfont': '"Open Sans", Arial, sans-serif',
  'codebgcolor': '$color-qube-light',
  'codebgcolor': 'grey',
  'body_min_width': '50%',
  'body_max_width': '90%',
  'collapse_navigation': True,
}

gettext_uuid = True
gettext_compact = False

# epub_show_urls = 'footnote'
# latex_show_urls ='footnote'


locale_dirs = ['_translated']

html_context = {
    "display_github": True,
    "github_user": "QubesOS",
    "github_repo": "qubes-doc",
    "github_version": "main",
    "conf_py_path": "/",
}

# from https://gist.github.com/ehles/bed012d78aad5d3cd6c35a49bef32f9f
def align(argument):
  """Conversion function for the "align" option."""
  return directives.choice(argument, ('left', 'center', 'right'))


class IframeVideo(Directive):
  has_content = False
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = False
  option_spec = {
    'height': directives.nonnegative_int,
    'width': directives.nonnegative_int,
    'align': align,
  }
  default_width = 500
  default_height = 281

  def run(self):
    self.options['video_id'] = directives.uri(self.arguments[0])
    if not self.options.get('width'):
      self.options['width'] = self.default_width
    if not self.options.get('height'):
      self.options['height'] = self.default_height
    if not self.options.get('align'):
      self.options['align'] = 'left'
    return [nodes.raw('', self.html % self.options, format='html')]


class GeneralVid(IframeVideo):
  html = '<iframe src="%(video_id)s" width="%(width)u" height="%(height)u" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowfullscreen class="responsive" referrerpolicy="no-referrer" scrolling="no"></iframe>'


class Youtube(IframeVideo):
  html = '<iframe src="https://www.youtube-nocookie.com/embed/%(video_id)s" \
  width="%(width)u" height="%(height)u" frameborder="0" \
  webkitAllowFullScreen mozallowfullscreen allowfullscreen \
  class="responsive" referrerpolicy="no-referrer" scrolling="no"></iframe>'


def setup(builder):
  directives.register_directive('youtube', Youtube)
  directives.register_directive('generalvid', GeneralVid)
