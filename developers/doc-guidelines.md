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

Editing Qubes documentation
---------------------------

Editing Qubes documentation is easy, if you spot some errors, feel free to
correct it. Because Qubes OS is security-oriented project, every documentation
change will be reviewed before being visible on the main page.

First of all, we keep documentation in git repository hosted on
[github][github]. Thanks to github interface, you can edit documentation even
if you do not know git at all. But you need a github account for that (it is
free!).

Ok, lets start. Every documentation page have "Edit this page" button. It can
be on the right side (in desktop layout):

![edit-button-desktop](/attachment/wiki/doc-edit/03-button2.png)

Or at the bottom in mobile layout:

![edit-button-mobile](/attachment/wiki/doc-edit/02-button1.png)

When you click on it, you'll be prompted for Github username and password (if
you aren't logged in already). You can also create an account from
there. 

![github-sign-in](/attachment/wiki/doc-edit/04-sign-in.png)

If it is your first contribution to the documentation, you need to "fork" a
repository (make your own copy). It's easy - just click that big green button
on the next page. This step is needed only for the first time.

![fork](/attachment/wiki/doc-edit/05-fork.png)

Then you can make your modifications. You can also preview how the changes will
be formated using "Preview changes" tab above editor.

![edit](/attachment/wiki/doc-edit/06-edit.png)

When you finish, describe your changes at the bottom and click "Propose file change". 

![commit](/attachment/wiki/doc-edit/07-commit-msg.png)

After that, you'll see what exactly modification you've made. At this stage
those changes are still in your own copy of the documentation ("fork"). If
everything is ok, send those change to us back using "Create pull request"
button.

![pull-request](/attachment/wiki/doc-edit/08-review-changes.png)

You will be able to adjust pull request message and title there. In most cases
defaults are ok, so you can just confirm with "Create pull request" button
again.

![pull-request-confirm](/attachment/wiki/doc-edit/09-create-pull-request.png)


That's all! We will review your changes and eventually pull them into Qubes
documentation. You'll get email notification about that.

![done](/attachment/wiki/doc-edit/10-done.png)

[qubes-doc]: https://github.com/QubesOS/qubes-doc
[qubes]: https://github.com/QubesOS
[gh-fork]: https://guides.github.com/activities/forking/
[gh-pull]: https://help.github.com/articles/using-pull-requests/
[patch]: /doc/SourceCode/#sending-a-patch
[lists]: https://www.qubes-os.org/doc/QubesLists/
[github]: https://github.com/
