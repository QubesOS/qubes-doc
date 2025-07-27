# Qubes OS Documentation

Canonical URL: https://www.qubes-os.org/doc/

All [Qubes OS Project](https://github.com/QubesOS) documentation pages are
stored as plain text files in this dedicated repository. By cloning and
regularly pulling from this repo, users can maintain their own up-to-date
offline copy of all Qubes documentation rather than relying solely on the Web.

To contribute, please see [how to edit the
documentation](https://www.qubes-os.org/doc/how-to-edit-the-documentation/).

## How to build the documentation

In a qube, after cloning or downloading this repo, do:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Then, build the documentation using any sphinx builder, i.e. with HTML:

    sphinx-build -M html . build

The HTML version of the documentation is now accessible in `build/html`

