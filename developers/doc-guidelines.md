---
layout: doc
title: Documentation Guidelines
permalink: /doc/doc-guidelines/
redirect_from:
- /en/doc/doc-guidelines/
- /wiki/DocStyle/
- /doc/DocStyle/
---

Documentation Guidelines
========================

All Qubes OS documentation pages are stored as plain text files in the
dedicated [qubes-doc] repository. By cloning and regularly pulling from
this repo, users can maintain their own up-to-date offline copy of all Qubes
documentation rather than relying solely on the Web.

The documentation is a community effort in which volunteers work hard trying to
keep everything accurate and comprehensive. If you notice a problem with the
documentation or some way it can be improved, please [report] it! Better
yet, you can [edit the documentation][contribute] yourself, both to add new
content and to edit existing content.


How to Report Issues
--------------------

To report an issue, please create an issue in [qubes-issues], but before you do,
please make sure your issue does **not** already exist. Documentation-related
issues will be assigned the `doc` label. Issues which have been created in
[qubes-issues] are significantly more likely to be addressed than those sent in
emails to the mailing lists or to individuals.


How to Contribute
-----------------

Editing the documentation is easy, so if you spot any errors, please help us
fix them! (As mentioned above, the documentation maintainers are just volunteers
who have day jobs of their own, so we rely heavily on the community to improve
the documentation.) Since Qubes is a security-oriented project, every
documentation change will be reviewed before it's published to the web. This
allows us to maintain quality control and protect our users.

As mentioned above, we keep all the documentation in a dedicated [Git
repository][qubes-doc] hosted on [GitHub]. Thanks to GitHub interface, you can
edit the documentation even if you don't know Git at all! The only thing you
need is a GitHub account, which is free.

(Note: If you're already familiar with GitHub or wish to work from the command
line, you can skip the rest of this section. All you need to do to contribute is
to [fork and clone][gh-fork] the [qubes-doc] repo, make your changes, then
[submit a pull request][gh-pull].)

Ok, let's start. Every documentation page has an "Edit this page" button. It may
be on the right side (in the desktop layout):

![edit-button-desktop](/attachment/wiki/doc-edit/03-button2.png)

Or at the bottom (in the mobile layout):

![edit-button-mobile](/attachment/wiki/doc-edit/02-button1.png)

When you click on it, you'll be prompted for your GitHub username and password
(if you aren't already logged in). You can also create an account from here.

![github-sign-in](/attachment/wiki/doc-edit/04-sign-in.png)

If this is your first contribution to the documentation, you need to "fork" the
repository (make your own copy). It's easy --- just click the big green button
on the next page. This step is only needed the first time you make a
contribution.

![fork](/attachment/wiki/doc-edit/05-fork.png)

Now you can make your modifications. You can also preview the changes to see how
they'll be formatted by clicking the "Preview changes" tab.

![edit](/attachment/wiki/doc-edit/06-edit.png)

Once you're finish, describe your changes at the bottom and click "Propose file
change".

![commit](/attachment/wiki/doc-edit/07-commit-msg.png)

After that, you'll see exactly what modifications you've made. At this stage,
those changes are still in your own copy of the documentation ("fork"). If
everything looks good, send those changes to us by pressing the "Create pull
request" button.

![pull-request](/attachment/wiki/doc-edit/08-review-changes.png)

You will be able to adjust the pull request message and title there. In most
cases, the defaults are ok, so you can just confirm by pressing the "Create pull
request" button again.

![pull-request-confirm](/attachment/wiki/doc-edit/09-create-pull-request.png)

That's all! We will review your changes. If everything looks good, we'll pull
them into the official documentation. Otherwise, we may have some questions for
you, which we'll post in a comment on your pull request. (GitHub will
automatically notify you if we do.) If, for some reason, we can't accept your
pull request, we'll post a comment explaining why we can't.

![done](/attachment/wiki/doc-edit/10-done.png)


Style Guidelines
----------------

 * Familiarize yourself with the terms defined in the [glossary]. Use these
   terms consistently and accurately throughout your writing.


Markdown Conventions
--------------------

All the documentation is written in Markdown for maximum accessibility. When
making contributions, please try to observe the following style conventions:

 * Use spaces instead of tabs.
 * Hard wrap Markdown lines at 80 characters.
 * If appropriate, make numerals in numbered lists match between Markdown
   source and HTML output.
   * Rationale: In the event that a user is required to read the Markdown source
     directly, this will make it easier to follow, e.g., numbered steps in a set
     of instructions.
 * Use hanging indentations  
   where appropriate.
 * Use underline headings (`=====` and `-----`) if possible. If this is not
   possible, use Atx-style headings on both the left and right sides
   (`### H3 ###`).
 * Use `[reference-style][ref]` links.  
 
`[ref]: https://daringfireball.net/projects/markdown/syntax#link`

([This][md] is a great source for learning about Markdown.)


Git Conventions
---------------

Please attempt to follow these conventions when writing your Git commit
messages:

 * Separate the subject line from the body with a blank line.
 * Limit the subject line to approximately 50 characters.
 * Capitalize the subject line.
 * Do not end the subject line with a period.
 * Use the imperative mood in the subject line.
 * Wrap the body at 72 characters.
 * Use the body to explain *what* and *why* rather than *how*.

For details, examples, and the rationale behind each of these conventions,
please see [this blog post][git-commit], which is the source of this list.


[qubes-doc]: https://github.com/QubesOS/qubes-doc
[glossary]: /doc/glossary/
[report]: #how-to-report-issues
[contribute]: #how-to-contribute
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues
[gh-fork]: https://guides.github.com/activities/forking/
[gh-pull]: https://help.github.com/articles/using-pull-requests/
[GitHub]: https://github.com/
[md]: https://daringfireball.net/projects/markdown/
[git-commit]: http://chris.beams.io/posts/git-commit/
