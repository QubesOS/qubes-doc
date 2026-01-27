"""Create a last-updates directive

.. code::

    .. last-updates:: 10

Will return the last 10 entries of the git log.
"""

import subprocess
import shlex
from docutils import nodes
from sphinx.util.docutils import SphinxDirective

GIT_COMMAND = "git --git-dir {git_dir} log --max-count {max_count}"


class LastUpdatesDirective(SphinxDirective):
    """A directive to say hello!"""

    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        git_command = GIT_COMMAND.format(
            git_dir=self.state.document.settings.env.srcdir / ".git",
            max_count=self.arguments[0],
        )
        content = f"Run {git_command}"

        try:
            content = subprocess.check_output(shlex.split(git_command)).decode()

        except (FileNotFoundError, subprocess.CalledProcessError):
            raise
        node = nodes.literal_block(text=content)

        return [node]


def setup(app):
    app.add_directive("last-updates", LastUpdatesDirective)
