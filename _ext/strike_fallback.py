"""Minimal replacement for sphinxnotes.strike, for offline builds where it is
not packaged: :strike:`text` renders as an inline with the "strike" class"""

from docutils import nodes


def strike_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    return [nodes.inline(rawtext, text, classes=['strike'])], []


def setup(app):
    app.add_role('strike', strike_role)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
