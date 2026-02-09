"""Create a last-updates directive

.. code::

    .. last-updates:: 10

Will return the last 10 entries of the git log.
"""

import shlex
import subprocess

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class LastUpdatesDirective(SphinxDirective):
    """Return the last entries of the git log."""

    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        git_dir = self.state.document.settings.env.srcdir / ".git"
        max_count = self.arguments[0]

        git_command = ("git", "--git-dir", git_dir, "log", "--max-count", max_count)
        try:
            content = subprocess.check_output(git_command).decode()
        except (FileNotFoundError, subprocess.CalledProcessError):
            content = "Run {}".format(shlex.join(git_command))

        node = nodes.literal_block(text=content)

        return [node]


def setup(app):
    app.add_directive("last-updates", LastUpdatesDirective)
