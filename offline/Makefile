# Offline build of the documentation, for distribution packages.
# Uses only distribution-packaged Sphinx extensions (see conf.py, tag "offline").

SPHINXBUILD ?= sphinx-build
SPHINXOPTS ?= -q -t offline
BUILDDIR ?= _build/offline
DESTDIR ?=
# Not under /usr/share/doc: the HTML is used by the desktop entry, and
# systems may be configured not to install documentation directories
DATADIR ?= /usr/share/qubes-doc
MANDIR ?= /usr/share/man
INFODIR ?= /usr/share/info
APPDIR ?= /usr/share/applications
ICONDIR ?= /usr/share/icons/hicolor/128x128/apps

SRCDIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))..

all:
	for builder in html man texinfo epub; do \
		$(SPHINXBUILD) $(SPHINXOPTS) -b $$builder -d $(BUILDDIR)/doctrees \
			$(SRCDIR) $(BUILDDIR)/$$builder || exit 1; \
	done
	sh $(SRCDIR)/offline/bundle-fonts.sh $(BUILDDIR)/html
	# Point the info images to the installed HTML images (DATADIR next to
	# INFODIR), and build from a tree with the same layout so that makeinfo
	# finds them
	mkdir -p $(BUILDDIR)/info-tree/info $(BUILDDIR)/info-tree/qubes-doc
	ln -sfn $(abspath $(BUILDDIR))/html $(BUILDDIR)/info-tree/qubes-doc/html
	sed 's|@image{qubesos-figures/|@image{../qubes-doc/html/_images/|g' \
		$(BUILDDIR)/texinfo/qubesos.texi > $(BUILDDIR)/info-tree/info/qubesos.texi
	cd $(BUILDDIR)/info-tree/info && makeinfo --no-split -o qubesos.info qubesos.texi

install:
	install -d $(DESTDIR)$(DATADIR)
	cp -r $(BUILDDIR)/html $(DESTDIR)$(DATADIR)/html
	rm -f $(DESTDIR)$(DATADIR)/html/.buildinfo
	install -m 644 $(BUILDDIR)/epub/QubesOS.epub $(DESTDIR)$(DATADIR)/qubes-os.epub
	install -m 644 -D $(BUILDDIR)/man/qubesos.1 $(DESTDIR)$(MANDIR)/man1/qubesos.1
	install -m 644 -D $(BUILDDIR)/info-tree/info/qubesos.info $(DESTDIR)$(INFODIR)/qubesos.info
	install -m 644 -D $(SRCDIR)/offline/qubes-doc.desktop $(DESTDIR)$(APPDIR)/qubes-doc.desktop
	install -m 644 -D $(SRCDIR)/attachment/icons/128x128/apps/qubes-logo-icon.png $(DESTDIR)$(ICONDIR)/qubes-doc.png

clean:
	rm -rf $(BUILDDIR)

.PHONY: all install clean
