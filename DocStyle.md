---
layout: doc
title: DocStyle
permalink: /doc/DocStyle/
redirect_from: /wiki/DocStyle/
---

Guidelines for Documentation Contributors
=========================================

 * Use spaces instead of tabs.
 * Hard wrap Markdown lines at 80 characters.
 * Hard wrap Git commit message lines at 72 characters.
   * This leaves exactly four spaces on each side of the commit message when
   viewed in the default `git log` format.)
 * If appropriate, make numerals in numbered lists match between Markdown source
   and HTML output.
   * In the event that a user is required to read the Markdown
   source directly, this will make it easier to follow, e.g., numbered steps in
   a set of instructions.
 * Use hanging indentations  
   where appropriate.
 * Use `[reference-style][ref]` links.  
   `[ref]: http://daringfireball.net/projects/markdown/syntax#link`
 * Use underline headings `=====` and `-----` if possible. If this is not
   possible use the Atx-style headings on the left side, e. g. `### H3`.

Sending documentation updates
-----------------------------

Main documentation repository is [qubes-doc] on [QubesOS] github account. If
you want to add something there, clone that repository commit the changes and
send us patches using either [github pull requests][github-forking] or [plain
email sent to qubes-devel mailing list][patch].

If you have a github account (its free!), you can simply browse [qubes-doc]
repository and edit the files there! Github interface will automatically guide
you through [fork & pull request creation process][github-forking].

[qubes-doc]: https://github.com/QubesOS/qubes-doc
[QubesOS]: https://github.com/QubesOS/
[github-forking]: https://guides.github.com/activities/forking/
[patch]: /doc/SourceCode/#sending-a-patch
