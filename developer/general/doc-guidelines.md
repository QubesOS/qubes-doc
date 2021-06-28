---
lang: en
layout: doc
permalink: /doc/doc-guidelines/
redirect_from:
- /en/doc/doc-guidelines/
- /wiki/DocStyle/
- /doc/DocStyle/
ref: 30
title: Documentation Guidelines
---

All Qubes OS documentation pages are stored as plain text files in the
dedicated [qubes-doc](https://github.com/QubesOS/qubes-doc) repository. By
cloning and regularly pulling from this repo, users can maintain their own
up-to-date offline copy of all Qubes documentation rather than relying solely
on the web.

The documentation is a community effort. Volunteers work hard trying to keep
everything accurate and comprehensive. If you notice a problem or some way it
can be improved, please [edit the documentation](#how-to-contribute)!

## Security

*Also see: [Should I trust this website?](/faq/#should-i-trust-this-website)*

All pull requests (PRs) against
[qubes-doc](https://github.com/QubesOS/qubes-doc) must pass review prior to be
merged, except in the case of [external
documentation](/doc/#external-documentation) (see
[#4693](https://github.com/QubesOS/qubes-issues/issues/4693)). This process is
designed to ensure that contributed text is accurate and non-malicious. This
process is a best effort that should provide a reasonable degree of assurance,
but it is not foolproof. For example, all text characters are checked for ANSI
escape sequences. However, binaries, such as images, are simply checked to
ensure they appear or function the way they should when the website is
rendered. They are not further analyzed in an attempt to determine whether they
are malicious.

Once a pull request passes review, the reviewer should add a signed comment
stating, "Passed review as of `<latest_commit>`" (or similar). The
documentation maintainer then verifies that the pull request is mechanically
sound (no merge conflicts, broken links, ANSI escapes, etc.). If so, the
documentation maintainer then merges the pull request, adds a PGP-signed tag to
the latest commit (usually the merge commit), then pushes to the remote. In
cases in which another reviewer is not required, the documentation maintainer
may review the pull request (in which case no signed comment is necessary,
since it would be redundant with the signed tag).

## Questions, problems, and improvements

If you have a question about something you read in the documentation, please
send it to the appropriate [mailing list](/support/). If you see that something
in the documentation should be fixed or improved, please
[contribute](#how-to-contribute) the change yourself. To report an issue with
the documentation, please follow our standard [issue reporting
guidelines](/doc/issue-tracking/). (If you report an issue with the
documentation, you will likely be asked to address it, unless there is a clear
indication in your report that you are not willing or able to do so.)

## How to contribute

Editing the documentation is easy, so if you see that a change should be made,
please contribute it!

A few notes before we get started:

* Since Qubes is a security-oriented project, every documentation change will
  be reviewed before it's accepted. This allows us to maintain quality control
  and protect our users.
* We don't want you to spend time and effort on a contribution that we can't
  accept. If your contribution would take a lot of time, please [file an
  issue](/doc/issue-tracking/) for it first so that we can make sure we're on
  the same page before significant works begins.
* Alternatively, you may already have written content that doesn't conform to
  these guidelines, but you'd be willing to modify it so that it does. In this
  case, you can still submit it by following the instructions below. Just make
  a note in your pull request (PR) that you're aware of the changes that need
  to be made and that you're just asking for the content to be reviewed before
  you spend time making those changes.

As mentioned above, we keep all the documentation in a dedicated [Git
repository](https://github.com/QubesOS/qubes-doc) hosted on
[GitHub](https://github.com/). Thanks to GitHub's interface, you can edit the
documentation even if you don't know Git at all! The only thing you need is a
GitHub account, which is free.

(**Note:** If you're already familiar with GitHub or wish to work from the
command line, you can skip the rest of this section. All you need to do to
contribute is to [fork and
clone](https://guides.github.com/activities/forking/) the
[qubes-doc](https://github.com/QubesOS/qubes-doc) repo, make your changes, then
[submit a pull
request](https://help.github.com/articles/using-pull-requests/).)

Ok, let's start. Every documentation page has an "Edit this page" button. It
may be on the side (in the desktop layout):

[![edit-button-desktop](/attachment/doc/03-button2.png)](/attachment/doc/03-button2.png)

Or at the bottom (in the mobile layout):

[![edit-button-mobile](/attachment/doc/02-button1.png)](/attachment/doc/02-button1.png)

When you click on it, you'll be prompted for your GitHub username and password
(if you aren't already logged in). You can also create an account from here.

[![github-sign-in](/attachment/doc/04-sign-in.png)](/attachment/doc/04-sign-in.png)

If this is your first contribution to the documentation, you need to "fork" the
repository (make your own copy). It's easy --- just click the big green button
on the next page. This step is only needed the first time you make a
contribution.

[![fork](/attachment/doc/05-fork.png)](/attachment/doc/05-fork.png)

Now you can make your modifications. You can also preview the changes to see
how they'll be formatted by clicking the "Preview changes" tab. If you want to
add images, please see [How to add images](#how-to-add-images). If you're
making formatting changes, please [render the site
locally](https://github.com/QubesOS/qubesos.github.io#instructions) to verify
that everything looks correct before submitting any changes.

[![edit](/attachment/doc/06-edit.png)](/attachment/doc/06-edit.png)

Once you're finished, describe your changes at the bottom and click "Propose
file change".

[![commit](/attachment/doc/07-commit-msg.png)](/attachment/doc/07-commit-msg.png)

After that, you'll see exactly what modifications you've made. At this stage,
those changes are still in your own copy of the documentation ("fork"). If
everything looks good, send those changes to us by pressing the "Create pull
request" button.

[![pull-request](/attachment/doc/08-review-changes.png)](/attachment/doc/08-review-changes.png)

You will be able to adjust the pull request message and title there. In most
cases, the defaults are ok, so you can just confirm by pressing the "Create
pull request" button again.

[![pull-request-confirm](/attachment/doc/09-create-pull-request.png)](/attachment/doc/09-create-pull-request.png)

If any of your changes should be reflected in the [documentation index (a.k.a.
table of contents)](/doc/) --- for example, if you're adding a new page,
changing the title of an existing page, or removing a page --- please see [How
to edit the documentation index](#how-to-edit-the-documentation-index).

That's all! We will review your changes. If everything looks good, we'll pull
them into the official documentation. Otherwise, we may have some questions for
you, which we'll post in a comment on your pull request. (GitHub will
automatically notify you if we do.) If, for some reason, we can't accept your
pull request, we'll post a comment explaining why we can't.

[![done](/attachment/doc/10-done.png)](/attachment/doc/10-done.png)

## How to edit the documentation index

The source file for the [documentation index (a.k.a. table of contents)](/doc/)
lives here:

<https://github.com/QubesOS/qubesos.github.io/blob/master/_data/doc-index.yml>

Editing this file will change what appears on the documentation index. If your
pull request (PR) adds, removes, or edits anything that should be reflected in
the documentation index, please make sure you also submit an associated pull
request against this file.

## How to add images

To add an image to a page, use the following syntax in the main document. This
will make the image a hyperlink to the image file, allowing the reader to click
on the image in order to view the image by itself.

```
[![Image Title](/attachment/doc/image.png)](/attachment/doc/image.png)
```

Then, submit your image(s) in a separate pull request to the
[qubes-attachment](https://github.com/QubesOS/qubes-attachment) repository
using the same path and filename. This is the only permitted way to include
images. Do not link to images on other websites.

## Organizational guidelines

### Do not duplicate documentation

Duplicating documentation is almost always a bad idea. There are many reasons
for this. The main one is that almost all documentation has to be updated as
some point. When similar documentation appears in more than one place, it is
very easy for it to get updated in one place but not the others (perhaps
because the person updating it doesn't realize it's in more than once place).
When this happens, the documentation as a whole is now inconsistent, and the
outdated documentation becomes a trap, especially for novice users. Such traps
are often more harmful than if the documentation never existed in the first
place. The solution is to **link** to existing documentation rather than
duplicating it. There are some exceptions to this policy (e.g., information
that is certain not to change for a very long time), but they are rare.

### Core vs. external documentation

Core documentation resides in the [Qubes OS Project's official
repositories](https://github.com/QubesOS/), mainly in
[qubes-doc](https://github.com/QubesOS/qubes-doc). External documentation can
be anywhere else (such as forums, community websites, and blogs), but there is
an especially large collection in the [Qubes
Community](https://github.com/Qubes-Community) project. External documentation
should not be submitted to [qubes-doc](https://github.com/QubesOS/qubes-doc).
If you've written a piece of documentation that is not appropriate for
[qubes-doc](https://github.com/QubesOS/qubes-doc), we encourage you to submit
it to the [Qubes Community](https://github.com/Qubes-Community) project
instead. However, *linking* to external documentation from
[qubes-doc](https://github.com/QubesOS/qubes-doc) is perfectly fine. Indeed,
the maintainers of the [Qubes Community](https://github.com/Qubes-Community)
project should regularly submit PRs against the documentation index (see [How
to edit the documentation index](#how-to-edit-the-documentation-index)) to add
and update Qubes Community links in the "External Documentation" section of the
documentation table of contents.

The main difference between **core** (or **official**) and **external** (or
**community** or **unofficial**) documentation is whether it documents software
that is officially written and maintained by the Qubes OS Project. The purpose
of this distinction is to keep the core docs maintainable and high-quality by
limiting them to the software output by the Qubes OS Project. In other words,
we take responsibility for documenting all of the software we put out into the
world, but it doesn't make sense for us to take on the responsibility of
documenting or maintaining documentation for anything else. For example, Qubes
OS may use a popular Linux distribution for an official
[TemplateVM](/doc/templates/). However, it would not make sense for a
comparatively small project like ours, with modest funding and a lean
workforce, to attempt to document software belonging to a large, richly-funded
project with an army of paid and volunteer contributors, especially when they
probably already have documentation of their own. This is particularly true
when it comes to Linux in general. Although many users who are new to Qubes are
also new to Linux, it makes absolutely no sense for our comparatively tiny
project to try to document Linux in general when there is already a plethora of
documentation out there.

Many contributors do not realize that there is a significant amount of work
involved in *maintaining* documentation after it has been written. They may
wish to write documentation and submit it to the core docs, but they see only
their own writing process and fail to consider that it will have to be kept
up-to-date and consistent with the rest of the docs for years afterward.
Submissions to the core docs also have to go through a review process to ensure
accuracy before being merged (see [security](#security)), which takes up
valuable time from the team. We aim to maintain high quality standards for the
core docs (style and mechanics, formatting), which also takes up a lot of time.
If the documentation involves anything external to the Qubes OS Project (such
as a website, platform, program, protocol, framework, practice, or even a
reference to a version number), the documentation is likely to become outdated
when that external thing changes. It's also important to periodically review
and update this documentation, especially when a new Qubes release comes out.
Periodically, there may be technical or policy changes that affect all the core
documentation. The more documentation there is relative to maintainers, the
harder all of this will be. Since there are many more people who are willing to
write documentation than to maintain it, these individually small incremental
additions amount to a significant maintenance burden for the project.

On the positive side, we consider the existence of community documentation to
be a sign of a healthy ecosystem, and this is quite common in the software
world. The community is better positioned to write and maintain documentation
that applies, combines, and simplifies the official documentation, e.g.,
tutorials that explain how to install and use various programs in Qubes, how to
create custom VM setups, and introductory tutorials that teach basic Linux
concepts and commands in the context of Qubes. In addition, just because the
Qubes OS Project has officially written and maintains some flexible framework,
such as `qrexec`, it does not make sense to include every tutorial that says
"here's how to do something cool with `qrexec`" in the core docs. Such
tutorials generally also belong in the community documentation.

See [#4693](https://github.com/QubesOS/qubes-issues/issues/4693) for more
background information.

### Version-specific documentation

*See [#5308](https://github.com/QubesOS/qubes-issues/issues/5308) for potential
changes to this policy.*

We maintain only one set of documentation for Qubes OS. We do not maintain a
different set of documentation for each version of Qubes. Our single set of
Qubes OS documentation is updated on a continual, rolling basis. Our first
priority is to document all **current, stable releases** of Qubes. Our second
priority is to document the next, upcoming release (if any) that is currently
in the beta or release candidate stage.

In cases where a documentation page covers functionality that differs
considerably between Qubes OS versions, the page should be subdivided into
clearly-labeled sections that cover the different functionality in different
versions:

#### Incorrect Example

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

#### Correct Example

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

Subdividing the page into clearly-labeled sections for each version has several
benefits:

* It preserves good content for older (but still supported) versions. Many
  documentation contributors are also people who prefer to use the latest
  version. Many of them are tempted to *replace* existing content that applies
  to an older, supported version with content that applies only to the latest
  version. This is somewhat understandable. Since they only use the latest
  version, they may be focused on their own experience, and they may even
  regard the older version as deprecated, even when it's actually still
  supported. However, allowing this replacement of content would do a great
  disservice to those who still rely on the older, supported version. In many
  cases, these users value the stability and reliability of the older,
  supported version. With the older, supported version, there has been more
  time to fix bugs and make improvements in both the software and the
  documentation. Consequently, much of the documentation content for this
  version may have gone through several rounds of editing, review, and
  revision. It would be a tragedy for this content to vanish while the very set
  of users who most prize stability and reliability are depending on it.
* It's easy for readers to quickly find the information they're looking for,
  since they can go directly to the section that applies to their version.
* It's hard for readers to miss information they need, since it's all in one
  place. In the incorrect example, information that the reader needs could be
  in any paragraph in the entire document, and there's no way to tell without
  reading the entire page. In the correct example, the reader can simply skim
  the headings in order to know which parts of the page need to be read and
  which can be safely ignored. The fact that some content is repeated in the
  two version-specific sections is not a problem, since no reader has to read
  the same thing twice. Moreover, as one version gets updated, it's likely that
  the documentation for that version will also be updated. Therefore, content
  that is initially duplicated between version-specific sections will not
  necessarily stay that way, and this is a good thing: We want the
  documentation for a version that *doesn't* change to stay the same, and we
  want the documentation for a version that *does* change to change along with
  the software.
* It's easy for documentation contributors and maintainers to know which file
  to edit and update, since there's only one page for all Qubes OS versions.
  Initially creating the new headings and duplicating content that applies to
  both is only a one-time cost for each page, and many pages don't even require
  this treatment, since they apply to all currently-supported Qubes OS
  versions.

By contrast, an alternative approach, such as segregating the documentation
into two different branches, would mean that contributions that apply to both
Qubes versions would only end up in one branch, unless someone remembered to
manually submit the same thing to the other branch and actually made the effort
to do so. Most of the time, this wouldn't happen. When it did, it would mean a
second pull request that would have to be reviewed. Over time, the different
branches would diverge in non-version-specific content. Good general content
that was submitted only to one branch would effectively disappear once that
version was deprecated. (Even if it were still on the website, no one would
look at it, since it would explicitly be in the subdirectory of a  deprecated
version, and there would be a motivation to remove it from the website so that
search results wouldn't be populated with out-of-date information.)

For further discussion about version-specific documentation in Qubes, see
[here](https://groups.google.com/d/topic/qubes-users/H9BZX4K9Ptk/discussion).

## Style guidelines

* Familiarize yourself with the terms defined in the
  [glossary](/doc/glossary/). Use these terms consistently and accurately
  throughout your writing.
* Syntactically distinguish variables in commands. For example, this is
  ambiguous:

      $ qvm-run --dispvm=disposable-template --service qubes.StartApp+xterm

  It should instead be:

      $ qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+xterm

  Note that we syntactically distinguish variables in three ways:
  1. Surrounding them in angled brackets (`< >`)
  2. Using underscores (`_`) instead of spaces between words
  3. Using all capital letters

  We have observed that many novices make the mistake of typing the surrounding
  angled brackets (`< >`) on the command line, even after substituting the
  desired real value between them. Therefore, in documentation aimed at
  novices, we also recommend clarifying that the angled brackets should not be
  typed. This can be accomplished in one of several ways:
  - Explicitly say something like "without the angled brackets."
  - Provide an example command using real values that excludes the angled
    brackets.
  - If you know that almost all users will want to use (or should use) a
    specific command containing all real values and no variables, you might
    consider providing exactly that command and forgoing the version with
    variables. Novices may not realize which parts of the command they can
    substitute with different values, but if you've correctly judged that they
    should use the command you've provided as is, then this shouldn't matter.

## Markdown conventions

All the documentation is written in Markdown for maximum accessibility. When
making contributions, please try to observe the following style conventions:

* Use spaces instead of tabs.
* Do not write HTML inside Markdown documents (except in rare, unavoidable
  cases, such as alerts). In particular, never include HTML or CSS for styling,
  formatting, or white space control. That belongs in the (S)CSS files instead.
* Link only to images in
  [qubes-attachment](https://github.com/QubesOS/qubes-attachment) (see
  [instructions above](#how-to-add-images)). Do not link to images on other
  websites.
* In order to enable offline browsing and automatic onion redirection, always
  use relative (rather than absolute) links, e.g., `/doc/doc-guidelines/`
  instead of `https://www.qubes-os.org/doc/doc-guidelines/`. Examples of
  exceptions:
  * The signed plain text portions of [QSBs](/security/qsb/) and
    [Canaries](/security/canary/)
  * URLs that appear inside code blocks (e.g., in comments and document
    templates)
  * Files like `README.md` and `CONTRIBUTING.md`
* Hard wrap Markdown lines at 80 characters, unless the line can't be broken
  (e.g., code or a URL).
* If appropriate, make numerals in numbered lists match between Markdown source
  and HTML output.
  * Rationale: In the event that a user is required to read the Markdown source
    directly, this will make it easier to follow, e.g., numbered steps in a set
    of instructions.
* Use hanging indentations where appropriate.
* Do not use `h1` headings (single `#` or `======` underline). These are
  automatically generated from the `title:` line in the YAML frontmatter.
* Use Atx-style headings: , `##h 2`, `### h3`, etc.
* When writing code blocks, use [syntax
  highlighting](https://github.github.com/gfm/#info-string) where
  [possible](https://github.com/jneen/rouge/wiki/List-of-supported-languages-and-lexers)
  and use `[...]` for anything omitted.
* When providing command line examples:
  * Tell the reader where to open a terminal (dom0 or a specific domU), and
    show the command along with its output (if any) in a code block, e.g.:

    ~~~markdown
    Open a terminal in dom0 and run:
    ```shell_session
    $ cd test
    $ echo Hello
    Hello
    ```
    ~~~

 * Precede each command with the appropriate command prompt: At a minimum, the
   prompt should contain a trailing `#` (for the user `root`) or `$` (for
   other users) on Linux systems and `>` on Windows systems, respectively.
 * Don't try to add comments inside the code block. For example, *don't* do
   this:

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

    The `#` symbol preceding each comment is ambiguous with a root command
    prompt. Instead, put your comments *outside* of the code block in normal
    prose.
* Use non-reference-style links like `[website](https://example.com/)`. Do
  *not* use reference links like `[website][example]`, `[website][]` or
  `[website]`.

([This](https://daringfireball.net/projects/markdown/) is a great source for
learning about Markdown.)

## Coding conventions

These conventions apply to the website as a whole, including everything written
in HTML, CSS, YAML, and Liquid. These conventions are intended to keep the
codebase consistent when multiple collaborators are working on it. They should
be understood as a practical set of rules for maintaining order in this
specific codebase rather than as a statement of what is objectively right or
good.

* Always use spaces. Never use tabs.
* Indent by exactly two (2) spaces.
* Whenever you add an opening tag, indent the following line. (Exception: If
  you open and close the tag on the same line, do not indent the following
  line.)
* Indent Liquid the same way as HTML.
* In general, the starting columns of every adjacent pair of lines should be no
  more than two spaces apart (example below).
* No blank or empty lines. (Hint: When you feel you need one, add a comment on
  that line instead.)
* Use comments to indicate the purposes of different blocks of code. This makes
  the file easier to understand and navigate.
* Use descriptive variable names. Never use one or two letter variable names.
  Avoid uncommon abbreviations and made-up words.
* In general, make it easy for others to read your code. Your future self will
  thank you, and so will your collaborators!
* [Don't Repeat Yourself
  (DRY)!](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) Instead of
  repeating the same block of code multiple times, abstract it out into a
  separate file and `include` that file where you need it.

### Indentation example

Here's an example that follows the indentation rules:

{% raw %}
```html
<table>
  <tr>
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    {% for item in secs.htmlsections[0].columns %}
      <th>{{ item.title }}</th>
    {% endfor %}
  </tr>
  {% for canary in site.data.sec-canary reversed %}
    <tr id="{{ canary.canary }}">
      <td><a href="#{{ canary.canary }}" class="fa fa-link black-icon" title="Anchor link to Qubes Canary row: Qubes Canary #{{ canary.canary }}"></a></td>
      <td>{{ canary.date }}</td>
      <td><a href="https://github.com/QubesOS/qubes-secpack/blob/master/canaries/canary-{{ canary.canary }}-{{ canary.date | date: '%Y' }}.txt">Qubes Canary #{{ canary.canary }}</a></td>
    </tr>
  {% endfor %}
</table>
```
{% endraw %}

## Git conventions

Please try to write good commit messages, according to the [instructions in our
coding style guidelines](/doc/coding-style/#commit-message-guidelines).

## Continuous Integration (CI)

The following commands may be useful as a way to interact with our CI
infrastructure. Note that special permissions may be required to use some of
these commands. These commands are generally issued by adding a comment to a
pull request (PR) containing only the command.

- `PipelineRetry`: Attempts to run the entire build pipeline over again. This
  can be useful if CI incorrectly uses a stale branch instead of testing the PR
  as if it were merged into `master`.
