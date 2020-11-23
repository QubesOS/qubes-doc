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

All Qubes OS documentation pages are stored as plain text files in the dedicated [qubes-doc] repository.
By cloning and regularly pulling from this repo, users can maintain their own up-to-date offline copy of all Qubes documentation rather than relying solely on the web.

The documentation is a community effort. Volunteers work hard trying to keep everything accurate and comprehensive.
If you notice a problem or some way it can be improved, please [edit the documentation][contribute]!


Security
--------

All pull requests against [qubes-doc] must pass review prior to be merged, except in the case of [external documentation] (see [#4693]).
This process is designed to ensure that contributed text is accurate and non-malicious.
This process is a best effort that should provide a reasonable degree of assurance, but it is not foolproof.
For example, all text characters are checked for ANSI escape sequences.
However, binaries, such as images, are simply checked to ensure they appear or function the way they should when the website is rendered.
They are not further analyzed in an attempt to determine whether they are malicious.

Once a pull request passes review, the reviewer should add a signed comment stating, "Passed review as of `<latest_commit>`" (or similar).
The documentation maintainer then verifies that the pull request is mechanically sound (no merge conflicts, broken links, ANSI escapes, etc.).
If so, the documentation maintainer then merges the pull request, adds a PGP-signed tag to the latest commit (usually the merge commit), then pushes to the remote.
In cases in which another reviewer is not required, the documentation maintainer may review the pull request (in which case no signed comment is necessary, since it would be redundant with the signed tag).


Questions, problems, and improvements
-------------------------------------

If you have a question about something you read in the documentation, please send it to the appropriate [mailing list][support].
If you see that something in the documentation should be fixed or improved, please [contribute] the change yourself.
To report an issue with the documentation, please follow our standard [issue reporting guidelines][issue].
(If you report an issue with the documentation, you will likely be asked to address it, unless there is a clear indication in your report that you are not willing or able to do so.)


How to Contribute
-----------------

Editing the documentation is easy, so if you see that a change should be made, please contribute it!

A few notes before we get started:

 * Since Qubes is a security-oriented project, every documentation change will be reviewed before it's accepted.
   This allows us to maintain quality control and protect our users.
 * We don't want you to spend time and effort on a contribution that we can't accept.
   If your contribution would take a lot of time, please [file an issue][issue] for it first so that we can make sure we're on the same page before significant works begins.
 * Alternatively, you may already have written content that doesn't conform to these guidelines, but you'd be willing to modify it so that it does.
   In this case, you can still submit it by following the instructions below.
   Just make a note in your pull request that you're aware of the changes that need to be made and that you're just asking for the content to be reviewed before you spend time making those changes.

As mentioned above, we keep all the documentation in a dedicated [Git repository][qubes-doc] hosted on [GitHub].
Thanks to GitHub's interface, you can edit the documentation even if you don't know Git at all!
The only thing you need is a GitHub account, which is free.

(**Note:** If you're already familiar with GitHub or wish to work from the command line, you can skip the rest of this section.
All you need to do to contribute is to [fork and clone][gh-fork] the [qubes-doc] repo, make your changes, then [submit a pull request][gh-pull].)

Ok, let's start.
Every documentation page has an "Edit this page" button.
It may be on the side (in the desktop layout):

![edit-button-desktop](/attachment/wiki/doc-edit/03-button2.png)

Or at the bottom (in the mobile layout):

![edit-button-mobile](/attachment/wiki/doc-edit/02-button1.png)

When you click on it, you'll be prompted for your GitHub username and password (if you aren't already logged in).
You can also create an account from here.

![github-sign-in](/attachment/wiki/doc-edit/04-sign-in.png)

If this is your first contribution to the documentation, you need to "fork" the repository (make your own copy). It's easy --- just click the big green button on the next page.
This step is only needed the first time you make a contribution.

![fork](/attachment/wiki/doc-edit/05-fork.png)

Now you can make your modifications.
You can also preview the changes to see how they'll be formatted by clicking the "Preview changes" tab.
If you're making formatting changes, please [render the site locally] to verify that everything looks correct before submitting any changes.

![edit](/attachment/wiki/doc-edit/06-edit.png)

Once you're finished, describe your changes at the bottom and click "Propose file change".

![commit](/attachment/wiki/doc-edit/07-commit-msg.png)

After that, you'll see exactly what modifications you've made.
At this stage, those changes are still in your own copy of the documentation ("fork").
If everything looks good, send those changes to us by pressing the "Create pull request" button.

![pull-request](/attachment/wiki/doc-edit/08-review-changes.png)

You will be able to adjust the pull request message and title there.
In most cases, the defaults are ok, so you can just confirm by pressing the "Create pull request" button again.

![pull-request-confirm](/attachment/wiki/doc-edit/09-create-pull-request.png)

That's all!
We will review your changes.
If everything looks good, we'll pull them into the official documentation.
Otherwise, we may have some questions for you, which we'll post in a comment on your pull request.
(GitHub will automatically notify you if we do.)
If, for some reason, we can't accept your pull request, we'll post a comment explaining why we can't.

![done](/attachment/wiki/doc-edit/10-done.png)


How to add images
-----------------

To add an image to a page, use the following syntax in the main document:

```
![Image Title](/attachment/wiki/page-title/image-filename.png)
```

Then, submit your image(s) in a separate pull request to the [qubes-attachment] repository using the same path and filename.
This is the only permitted way to include images.
Do not link to images on other websites.


Version-specific Documentation
------------------------------

We maintain only one set of documentation for Qubes OS.
We do not maintain a different set of documentation for each version of Qubes.
Our single set of Qubes OS documentation is updated on a continual, rolling basis.
Our first priority is to document all **current, stable releases** of Qubes.
Our second priority is to document the next, upcoming release (if any) that is currently in the beta or release candidate stage.

In cases where a documentation page covers functionality that differs considerably between Qubes OS versions, the page should be subdivided into clearly-labeled sections that cover the different functionality in different versions:

### Incorrect Example ###

```
# Page Title #

## How to Foo ##

Fooing is the process by which one foos. There are both general and specific
versions of fooing, which vary in usefulness depending on your goals, but for
the most part, all fooing is fooing.

To foo in Qubes 3.2:

   $ qvm-foo <foo-bar>

Note that this does not work in Qubes 4.0, where there is a special widget
for fooing, which you can find in the lower-right corner of the screen in
the Foo Manager. Alternatively, you can use the more general `qubes-baz`
command introduced in 4.0:

   $ qubes-baz --foo <bar>

Once you foo, make sure to close the baz before fooing the next bar.
```

### Correct Example ###

```
# Page Title #

## Qubes 3.2 ##

### How to Foo ###

Fooing is the process by which one foos. There are both general and specific
versions of fooing, which vary in usefulness depending on your goals, but for
the most part, all fooing is fooing.

To foo:

   $ qvm-foo <foo-bar>

Once you foo, make sure to close the baz before fooing the next bar.


## Qubes 4.0 ##

### How to Foo ###

Fooing is the process by which one foos. There are both general and specific
versions of fooing, which vary in usefulness depending on your goals, but for
the most part, all fooing is fooing.

There is a special widget for fooing, which you can find in the lower-right
corner of the screen in the Foo Manager. Alternatively, you can use the
general `qubes-baz` command:

   $ qubes-baz --foo <bar>

Once you foo, make sure to close the baz before fooing the next bar.
```

Subdividing the page into clearly-labeled sections for each version has several benefits:

 * It preserves good content for older (but still supported) versions.
   Many documentation contributors are also people who prefer to use the latest version.
   Many of them are tempted to *replace* existing content that applies to an older, supported version with content that applies only to the latest version.
   This is somewhat understandable.
   Since they only use the latest version, they may be focused on their own experience, and they may even regard the older version as deprecated, even when it's actually still supported.
   However, allowing this replacement of content would do a great disservice to those who still rely on the older, supported version.
   In many cases, these users value the stability and reliability of the older, supported version.
   With the older, supported version, there has been more time to fix bugs and make improvements in both the software and the documentation.
   Consequently, much of the documentation content for this version may have gone through several rounds of editing, review, and revision.
   It would be a tragedy for this content to vanish while the very set of users who most prize stability and reliability are depending on it.
 * It's easy for readers to quickly find the information they're looking for, since they can go directly to the section that applies to their version.
 * It's hard for readers to miss information they need, since it's all in one place.
   In the incorrect example, information that the reader needs could be in any paragraph in the entire document, and there's no way to tell without reading the entire page.
   In the correct example, the reader can simply skim the headings in order to know which parts of the page need to be read and which can be safely ignored.
   The fact that some content is repeated in the two version-specific sections is not a problem, since no reader has to read the same thing twice.
   Moreover, as one version gets updated, it's likely that the documentation for that version will also be updated.
   Therefore, content that is initially duplicated between version-specific sections will not necessarily stay that way, and this is a good thing:
   We want the documentation for a version that *doesn't* change to stay the same, and we want the documentation for a version that *does* change to change along with the software.
 * It's easy for documentation contributors and maintainers to know which file to edit and update, since there's only one page for all Qubes OS versions.
   Initially creating the new headings and duplicating content that applies to both is only a one-time cost for each page, and many pages don't even require this treatment, since they apply to all currently-supported Qubes OS versions.

By contrast, an alternative approach, such as segregating the documentation into two different branches, would mean that contributions that apply to both Qubes versions would only end up in one branch, unless someone remembered to manually submit the same thing to the other branch and actually made the effort to do so.
Most of the time, this wouldn't happen.
When it did, it would mean a second pull request that would have to be reviewed.
Over time, the different branches would diverge in non-version-specific content.
Good general content that was submitted only to one branch would effectively disappear once that version was deprecated.
(Even if it were still on the website, no one would look at it, since it would explicitly be in the subdirectory of a  deprecated version, and there would be a motivation to remove it from the website so that search results wouldn't be populated with out-of-date information.)

For further discussion about version-specific documentation in Qubes, see [here][version-thread].


Style Guidelines
----------------

 * Familiarize yourself with the terms defined in the [glossary]. Use these
   terms consistently and accurately throughout your writing.
 * Syntactically distinguish variables in commands.
   For example, this is ambiguous:

       $ qvm-run --dispvm=dvm-template --service qubes.StartApp+xterm

   It should instead be:

       $ qvm-run --dispvm=<DVM_TEMPLATE> --service qubes.StartApp+xterm

   Note that we syntactically distinguish variables in three ways:
   1. Surrounding them in angled brackets (`< >`)
   2. Using underscores (`_`) between words
   3. Using all capital letters


Markdown Conventions
--------------------

All the documentation is written in Markdown for maximum accessibility.
When making contributions, please try to observe the following style conventions:

 * Use spaces instead of tabs.
 * Do not write HTML inside Markdown documents (except in rare, unavoidable cases, such as alerts).
   In particular, never include HTML or CSS for styling, formatting, or white space control.
   That belongs in the (S)CSS files instead.
 * Link only to images in [qubes-attachment] (see [instructions above](#how-to-add-images)).
   Do not link to images on other websites.
 * In order to enable offline browsing, use relative paths (e.g., `/doc/doc-guidelines/` instead of `https://www.qubes-os.org/doc/doc-guidelines/`, except when the source text will be reproduced outside of the Qubes website repo.
   Examples of exceptions:
   * [QSBs] (intended to be read as plain text)
   * [News] posts (plain text is reproduced on the [mailing lists][support])
   * URLs that appear inside code blocks (e.g., in comments and document templates)
   * Files like `README.md` and `CONTRIBUTING.md`
 * Insert a newline at, and only at, the end of each sentence, except when the text will be reproduced outside of the Qubes website repo (see previous item for examples).
   * Rationale: This practice results in one sentence per line, which is most appropriate for source that consists primarily of natural language text.
     It results in the most useful diffs and facilitates translation into other languages while mostly preserving source readability.
 * If appropriate, make numerals in numbered lists match between Markdown source and HTML output.
   * Rationale: In the event that a user is required to read the Markdown source directly, this will make it easier to follow, e.g., numbered steps in a set of instructions.
 * Use hanging indentations  
   where appropriate.
 * Use Atx-style headings: `# h1`, `##h 2`, `### h3`, etc.
 * When writing code blocks, use [syntax highlighting](https://github.github.com/gfm/#info-string) where [possible](https://github.com/jneen/rouge/wiki/List-of-supported-languages-and-lexers) and use `[...]` for anything omitted.
 * When providing command line examples:
   * Tell the reader where to open a terminal (dom0 or a specific domU), and show the command along with its output (if any) in a code block, e.g.:
     ~~~markdown
     Open a terminal in dom0 and run:
     ```shell_session
     $ cd test
     $ echo Hello
     Hello
     ```
     ~~~
   * Precede each command with the appropriate command prompt:
     At a minimum, the prompt should contain a trailing `#` (for the user `root`) or `$` (for other users) on Linux systems and `>` on Windows systems, respectively.
   * Don't try to add comments inside the code block.
     For example, *don't* do this:
     ~~~markdown
     Open a terminal in dom0 and run:
     ```shell_session
     # Navigate to the new directory
     $ cd test
     # Generate a greeting
     $ echo Hello
     Hello
     ```
     ~~~
     The `#` symbol preceding each comment is ambiguous with a root command prompt.
     Instead, put your comments *outside* of the code block in normal prose.
 * Use `[reference-style][ref]` links.  
 
   `[ref]: https://daringfireball.net/projects/markdown/syntax#link`

([This][md] is a great source for learning about Markdown.)


Git Conventions
---------------

Please try to write good commit messages, according to the
[instructions in our coding style guidelines][git-commit].


[qubes-doc]: https://github.com/QubesOS/qubes-doc
[glossary]: /doc/glossary/
[issue]: /doc/reporting-bugs/
[contribute]: #how-to-contribute
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues
[gh-fork]: https://guides.github.com/activities/forking/
[gh-pull]: https://help.github.com/articles/using-pull-requests/
[GitHub]: https://github.com/
[support]: /support/
[version-example]: /doc/template/fedora/upgrade-25-to-26/
[version-thread]: https://groups.google.com/d/topic/qubes-users/H9BZX4K9Ptk/discussion
[QSBs]: /security/bulletins/
[News]: /news/
[md]: https://daringfireball.net/projects/markdown/
[git-commit]: /doc/coding-style/#commit-message-guidelines
[render the site locally]: https://github.com/QubesOS/qubesos.github.io#instructions
[qubes-attachment]: https://github.com/QubesOS/qubes-attachment
[external documentation]: /doc/#external-documentation
[#4693]: https://github.com/QubesOS/qubes-issues/issues/4693
