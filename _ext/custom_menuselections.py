"""Add an appmenuselection role"""

from sphinx.application import Sphinx
from sphinx.roles import MenuSelection

from docutils.nodes import Node, system_message


class Menu(MenuSelection):
    """Customize menuselection for Qubes App Menu"""

    name = "appmenuselection"

    def run(self) -> tuple[list[Node], list[system_message]]:
        self.text = f"Qubes App Menu (Q icon) --> {self.text}"
        nodes = super().run()
        nodes[0][0].attributes["classes"].append("menuselection")
        return nodes


def setup(app: Sphinx):
    app.add_role("appmenuselection", Menu())
