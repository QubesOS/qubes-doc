# Qubes OS Documentation

Canonical URL: https://doc.qubes-os.org

All [Qubes OS Project](https://github.com/QubesOS) documentation pages are
stored as plain reStructuredText files in this dedicated repository. By cloning and
regularly pulling from this repo, users can maintain their own up-to-date
offline copy of all Qubes documentation rather than relying solely on the Web.

To contribute, please see [how to edit the
documentation](https://doc.qubes-os.org/en/latest/developer/general/how-to-edit-the-rst-documentation.html).

## How to build the documentation

In a qube, after cloning or downloading this repo, do:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install .

Then, build the documentation using any sphinx builder, i.e. with HTML:

    sphinx-build -M html . build

The HTML version of the documentation is now accessible in `build/html`
