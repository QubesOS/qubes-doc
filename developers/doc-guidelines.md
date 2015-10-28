---
layout: doc
title: Documentation Guidelines
permalink: /doc/doc-guidelines/
redirect_from:
- /en/doc/doc-guidelines/
- /wiki/DocStyle/
- /doc/DocStyle/
---

Guidelines for Documentation Contributors
=========================================

All Qubes OS documentation pages are stored as plain text files in the
dedicated [qubes-doc] repository. By cloning and regularly pulling from
this repo, users can maintain their own up-to-date offline copy of all Qubes
documentation rather than relying solely on the Web.  Contributions to the
documentation (both new content and edits of existing content) are welcome. To
contribute, please [fork and clone][gh-fork] this repo, make your changes,
then either [submit a pull request][gh-pull] or [send a patch][patch] to the
`qubes-devel` [mailing list][lists]. If you have a GitHub account (free), you
can simply browse the [qubes-doc] repository and edit the files there. The
GitHub interface will automatically guide you through the
[fork and pull request creation process][gh-fork].


Markdown Conventions
--------------------

All the documentation is written in Markdown for maximum accessibility. When
making contributions, please observe the following style conventions:

 * Use spaces instead of tabs.
 * Hard wrap Markdown lines at 80 characters.
 * Hard wrap Git commit message lines at 72 characters.
   * This leaves exactly four spaces on each side of the commit message when
   viewed in the default `git log` format.)
 * If appropriate, make numerals in numbered lists match between Markdown
   source and HTML output.
   * In the event that a user is required to read the Markdown source
   directly, this will make it easier to follow, e.g., numbered steps in a
   set of instructions.
 * Use hanging indentations  
   where appropriate.
 * Use underline headings (`=====` and `-----`) if possible. If this is not
   possible, use Atx-style headings on both the left and right sides
   (`### H3 ###`).
 * Use `[reference-style][ref]` links.  
 
`[ref]: http://daringfireball.net/projects/markdown/syntax#link`


[qubes-doc]: https://github.com/QubesOS/qubes-doc
[qubes]: https://github.com/QubesOS
[gh-fork]: https://guides.github.com/activities/forking/
[gh-pull]: https://help.github.com/articles/using-pull-requests/
[patch]: /doc/SourceCode/#sending-a-patch
[lists]: https://www.qubes-os.org/doc/QubesLists/
