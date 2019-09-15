---
layout: doc
title: Documentation Guidelines
redirect_from:
- /doc/doc-guidelines/
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


Release-specific documentation
------------------------------

We maintain a separate set of documentation for each major Qubes OS release (e.g., R1, R2, R3).
We do **not** maintain separate sets of documentation for minor versions (e.g., R1.1, R1.2, R1.3) or patch versions (e.g., R1.0.1, R1.0.2, R1.0.3).
You can tell which version of the documentation you're reading by noting the release number in the URL.
For example, here is the Installation Guide for Release 4:

<https://www.qubes-os.org/doc/r4/installation-guide/>

(Notice the `r4` in the URL.)
When a new set of documentation is created, each page is approved for the new release.
At the top of each documentation page, you will see a notice that provides information about its approval status (e.g., that it has not yet been approved and may be out-of-date or that it has been approved).


### Technical details for maintainers and reviewers

Each release-specific set of documentation is managed in its own Git branch.
In order to maintain multiple versions correctly:

 * Do **not** specify a `permalink:` in the YAML header of any version-specific documentation page.
   Instead, allow the permalink to be generated by the contents of `_config.yml`.

 * When reviewing pages for a new release, add `approved_release: RX` (where `X` is the release number) on its own line in the YAML header.
   Without this line, there will be a warning that the page has not yet been approved for release `X`.
   With this line, there will be a notification that the page has been approved for release `X`.

For each new major Qubes OS release:

1. Create a new `qubes-doc` Git branch for that release.

2. Update the release number in the following files:
   ```
   _config.yml
   _includes/doc-heading.html
   _includes/doc-rX-approved.html
   _includes/doc-rX-unapproved.html
   ```

3. Connect the new branch as a separate module in the main repo.

4. Update URL redirects so that unversioned URLs point to the new release.
   (TODO: Write a script for this.)


Style Guidelines
----------------

 * Familiarize yourself with the terms defined in the [glossary]. Use these
   terms consistently and accurately throughout your writing.


Markdown Conventions
--------------------

All the documentation is written in Markdown for maximum accessibility.
When making contributions, please try to observe the following style conventions:

 * Use spaces instead of tabs.
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
 * Use underline headings (`=====` and `-----`) if possible.
   If this is not possible, use Atx-style headings: (`### H3 ###`).
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

