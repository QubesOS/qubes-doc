---
lang: en
layout: doc
permalink: /doc/documentation-style-guide/
redirect_from:
- /doc/doc-guidelines/
- /en/doc/doc-guidelines/
- /wiki/DocStyle/
- /doc/DocStyle/
ref: 30
title: Documentation style guide
---

_Also see [how to edit the documentation](/doc/how-to-edit-the-documentation/)._

Qubes OS documentation pages are stored as plain text Markdown files in the [qubes-doc](https://github.com/QubesOS/qubes-doc) repository. By cloning and regularly pulling from this repo, users can maintain their own up-to-date offline copy of all Qubes documentation rather than relying solely on the web.

The documentation is a volunteer community effort. People like you are constantly working to make it better. If you notice something that can be fixed or improved, please [edit the documentation](/doc/how-to-edit-the-documentation/)!

This page explains the standards we follow for writing, formatting, and organizing the documentation. Please follow these guidelines and conventions when editing the documentation. For the standards governing the website as a whole, please see the [website style guide](/doc/website-style-guide).

## Markdown conventions

All the documentation is written in Markdown for maximum accessibility. When making contributions, please observe the following style conventions. If you're not familiar with Markdown syntax, [this](https://daringfireball.net/projects/markdown/) is a great resource.

### Hyperlink syntax

Use non-reference-style links like `[website](https://example.com/)`. Do *not* use reference-style links like `[website][example]`, `[website][]` or `[website]`. This facilitates the localization process.

### Relative vs. absolute links

Always use relative rather than absolute paths for internal website links. For example, use `/doc/documentation-style-guide/` instead of `https://www.qubes-os.org/doc/documentation-style-guide/`.

You may use absolute URLs in the following cases:

- External links
- URLs that appear inside code blocks (e.g., in comments and document templates, and the plain text reproductions of [QSBs](/security/qsb/) and [Canaries](/security/canary/)), since they're not hyperlinks
- Git repo files like `README.md` and `CONTRIBUTING.md`, since they're not part of the website itself but rather of the auxiliary infrastructure supporting the website

This rule is important because using absolute URLs for internal website links breaks:

- Serving the website offline
- Website localization
- Generating offline documentation
- Automatically redirecting Tor Browser visitors to the correct page on the onion service mirror

### Image linking

See [how to add images](/doc/how-to-edit-the-documentation/#how-to-add-images) for the required syntax. This will make the image a hyperlink to the image file, allowing the reader to click on the image in order to view the full image by itself. This is important. Following best practices, our website has a responsive design, which allows the website to render appropriately across all screen sizes. When viewing this page on a smaller screen, such as on a mobile device, the image will automatically shrink down to fit the screen. If visitors cannot click on the image to view it in full size, then, depending on their device, they may have no way see the details in the image clearly.

In addition, make sure to link only to images in the [qubes-attachment](https://github.com/QubesOS/qubes-attachment) repository. Do not attempt to link to images hosted on other websites.

### HTML and CSS

Do not write HTML inside Markdown documents (except in rare, unavoidable cases, such as [alerts](#alerts)). In particular, never include HTML or CSS for styling, formatting, or white space control. That belongs in the (S)CSS files instead.

### Headings

Do not use `h1` headings (single `#` or `======` underline). These are automatically generated from the `title:` line in the YAML front matter.

Use Atx-style syntax for headings: `##h2`, `### h3`, etc. Do not use underlining syntax (`-----`).

### Indentation

Use spaces instead of tabs. Use hanging indentations where appropriate.

### Lists

If appropriate, make numerals in numbered lists match between Markdown source and HTML output. Some users read the Markdown source directly, and this makes numbered lists easier to follow.

### Code blocks

When writing code blocks, use [syntax highlighting](https://github.github.com/gfm/#info-string) where possible (see [here](https://github.com/jneen/rouge/wiki/List-of-supported-languages-and-lexers) for a list of supported languages). Use `[...]` for anything omitted.

### Line wrapping

Do not hard wrap text, except where necessary (e.g., inside code blocks).

### Do not use Markdown syntax for styling

For example, there is a common temptation to use block quotations (created by beginning lines with the `>` character) in order to stylistically distinguish some portion of text from the rest of the document, e.g.:

```
> Note: This is an important note!
```

This renders as:

> Note: This is an important note!

There are two problems with this:

1. It is a violation of the [separation of content and presentation](https://en.wikipedia.org/wiki/Separation_of_content_and_presentation), since it abuses markup syntax in order to achieve unintended stylistic results. The Markdown (and HTML, if any) should embody the *content* of the documentation, while the *presentation* is handled by (S)CSS.

2. It is an abuse of quotation syntax for text that is not actually a quotation. (You are not quoting anyone here. You're just telling the reader to note something and trying to draw their attention to your note visually.)

Instead, an example of an appropriate way to stylistically distinguish a portion of text is by using [alerts](#alerts). Consider also that extra styling and visual distinction may not even be necessary. In most cases, traditional writing methods are perfectly sufficient, e.g.,:

```
**Note:** This is an important note.
```

This renders as:

**Note:** This is an important note.

### Alerts

Alerts are sections of HTML used to draw the reader's attention to important information, such as warnings, and for stylistic purposes. They are typically styled as colored text boxes, usually accompanied by icons. Alerts should generally be used somewhat sparingly, so as not to cause [alert fatigue](https://en.wikipedia.org/wiki/Alarm_fatigue) and since they must be written in HTML instead of Markdown, which makes the source less readable and more difficult to work with for localization and automation purposes. Here are examples of several types of alerts and their recommended icons:

```
<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>Did you know?</b> The Qubes OS installer is completely offline. It doesn't
  even load any networking drivers, so there is no possibility of
  internet-based data leaks or attacks during the installation process.
</div>

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>Note:</b> Using Rufus to create the installation medium means that you <a
  href="https://github.com/QubesOS/qubes-issues/issues/2051">won't be able</a>
  to choose the "Test this media and install Qubes OS" option mentioned in the
  example below. Instead, choose the "Install Qubes OS" option.
</div>

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> Qubes OS is not meant to be installed inside a virtual machine
  as a guest hypervisor. In other words, <b>nested virtualization</b> is not
  supported. In order for a strict compartmentalization to be enforced, Qubes
  OS needs to be able to manage the hardware directly.
</div>

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Qubes has no control over what happens on your computer
  before you install it. No software can provide security if it is installed on
  compromised hardware. Do not install Qubes on a computer you don't trust. See
  <a href="/doc/install-security/">installation security</a> for more
  information.
</div>
```

These render as:

<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>Did you know?</b> The Qubes OS installer is completely offline. It doesn't
  even load any networking drivers, so there is no possibility of
  internet-based data leaks or attacks during the installation process.
</div>

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>Note:</b> Using Rufus to create the installation medium means that you <a
  href="https://github.com/QubesOS/qubes-issues/issues/2051">won't be able</a>
  to choose the "Test this media and install Qubes OS" option mentioned in the
  example below. Instead, choose the "Install Qubes OS" option.
</div>

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> Qubes OS is not meant to be installed inside a virtual machine
  as a guest hypervisor. In other words, <b>nested virtualization</b> is not
  supported. In order for a strict compartmentalization to be enforced, Qubes
  OS needs to be able to manage the hardware directly.
</div>

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Qubes has no control over what happens on your computer
  before you install it. No software can provide security if it is installed on
  compromised hardware. Do not install Qubes on a computer you don't trust. See
  <a href="/doc/install-security/">installation security</a> for more
  information.
</div>

## Writing guidelines

### Correct use of terminology

Familiarize yourself with the terms defined in the [glossary](/doc/glossary/). Use these terms consistently and accurately throughout your writing.

### Sentence case in headings

Use sentence case (rather than title case) in headings for the reasons explained [here](https://www.sallybagshaw.com.au/articles/sentence-case-v-title-case/). In particular, since the authorship of the Qubes documentation is decentralized and widely distributed among users from around the world, many contributors come from regions with different conventions for implementing title case, not to mention that there are often differing style guide recommendations even within a single region. It is much easier for all of us to implement sentence case consistently across our growing body of pages, which is very important for managing the ongoing maintenance burden and sustainability of the documentation.

### Writing command-line examples

When providing command-line examples:

- Tell the reader where to open a terminal (dom0 or a specific domU), and show the command along with its output (if any) in a code block, e.g.:

  ~~~markdown
  Open a terminal in dom0 and run:
  ```shell_session
  $ cd test
  $ echo Hello
  Hello
  ```
  ~~~

- Precede each command with the appropriate command prompt: At a minimum, the prompt should contain a trailing `#` (for the user `root`) or `$` (for other users) on Linux systems and `>` on Windows systems, respectively.

- Don't try to add comments inside the code block. For example, *don't* do this:

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

   The `#` symbol preceding each comment is ambiguous with a root command prompt. Instead, put your comments *outside* of the code block in normal prose.

### Variable names in commands

Syntactically distinguish variables in commands. For example, this is ambiguous:

    $ qvm-run --dispvm=disposable-template --service qubes.StartApp+xterm

It should instead be:

    $ qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+xterm

Note that we syntactically distinguish variables in three ways:

1. Surrounding them in angled brackets (`< >`)
2. Using underscores (`_`) instead of spaces between words
3. Using all capital letters

We have observed that many novices make the mistake of typing the surrounding angled brackets (`< >`) on the command line, even after substituting the desired real value between them. Therefore, in documentation aimed at novices, we also recommend clarifying that the angled brackets should not be typed. This can be accomplished in one of several ways:

- Explicitly say something like "without the angled brackets."
- Provide an example command using real values that excludes the angled brackets.
- If you know that almost all users will want to use (or should use) a specific command containing all real values and no variables, you might consider providing exactly that command and forgoing the version with variables. Novices may not realize which parts of the command they can substitute with different values, but if you've correctly judged that they should use the command you've provided as is, then this shouldn't matter.

### Capitalization of "qube"

We introduced the term ["qube"](/doc/glossary/#qube) as a user-friendly alternative to the term ["virtual machine" ("VM")](/doc/glossary/#vm) in the context of Qubes OS. Nonetheless, "qube" is a common noun like the words "compartment" and "container." Therefore, in English, "qube" follows the standard capitalization rules for common nouns. For example, "I have three qubes" is correct, while "I have three Qubes" is incorrect. Like other common nouns, "qube" should still be capitalized at the beginnings of sentences, the beginnings of sentence-case headings, and in title-case headings. Note, however, that starting a sentence with the plural of "qube" (e.g., "Qubes can be shut down...") can be ambiguous, since it may not be clear whether the referent is a plurality of qubes, [Qubes OS](/doc/glossary/#qubes-os), or even the Qubes OS Project itself. Hence, it is generally a good idea to rephrase such sentences in order to avoid this ambiguity.

Many people feel a strong temptation to capitalize the word "qube" all the time, like a proper noun, perhaps because it's a new and unfamiliar term that's closely associated with a particular piece of software (namely, Qubes OS). However, these factors are not relevant to the capitalization rules of English. In fact, it's not unusual for new common nouns to be introduced into English, especially in the context of technology. For example, "blockchain" is a relatively recent technical term that's a common noun. Why is it a common noun rather than a proper noun? Because proper nouns refer to *particular* people, places, things, and ideas. There are many different blockchains. However, even when there was just one, the word still denoted a collection of things rather than a particular thing. It happened to be the case that there was only one member in that collection at the time. For example, if there happened to be only one tree in the world, that wouldn't change the way we capitalize sentences like, "John sat under a tree." Intuitively, it makes sense that the addition and removal of objects from the world shouldn't cause published books to become orthographicallly incorrect while sitting on their shelves.

Accordingly, the reason "qube" is a common noun rather than a proper noun is because it doesn't refer to any one specific thing (in this case, any one specific virtual machine). Rather, it's the term for any virtual machine in a Qubes OS installation. (Technically, while qubes are currently implemented as virtual machines, Qubes OS is independent of its underlying compartmentalization technology. Virtual machines could be replaced with a different technology, and qubes would still be called "qubes.")

I have several qubes in my Qubes OS installation, and you have several in yours. Every Qubes OS user has their own set of qubes, just as each of us lives in some neighborhood on some street. Yet we aren't tempted to treat words like "neighborhood" or "street" as proper nouns (unless, of course, they're part of a name, like "Acorn Street"). Again, while this might seem odd because "qube" is a new word that we invented, that doesn't change how English works. After all, *every* word was a new word that someone invented at some point (otherwise we wouldn't have any words at all). We treat "telephone," "computer," "network," "program," and so on as common nouns, even though those were all new technological inventions in the not-too-distant past (on a historical scale, at least). So, we shouldn't allow ourselves to be confused by irrelevant factors, like the fact that the inventors happened to be *us* or that the invention was *recent* or is not in widespread use among humanity.

### English language conventions

For the sake of consistency and uniformity, the Qubes documentation aims to follow the conventions of American English, where applicable. (Please note that this is an arbitrary convention for the sake consistency and not a value judgment about the relative merits of British versus American English.)

## Organizational guidelines

### Do not duplicate documentation

Duplicating documentation is almost always a bad idea. There are many reasons for this. The main one is that almost all documentation has to be updated as some point. When similar documentation appears in more than one place, it is very easy for it to get updated in one place but not the others (perhaps because the person updating it doesn't realize it's in more than once place). When this happens, the documentation as a whole is now inconsistent, and the outdated documentation becomes a trap, especially for novice users. Such traps are often more harmful than if the documentation never existed in the first place. The solution is to **link** to existing documentation rather than duplicating it. There are some exceptions to this policy (e.g., information that is certain not to change for a very long time), but they are rare.

### Core vs. external documentation

Core documentation resides in the [Qubes OS Project's official repositories](https://github.com/QubesOS/), mainly in [qubes-doc](https://github.com/QubesOS/qubes-doc). External documentation can be anywhere else (such as forums, community websites, and blogs), but there is an especially large collection in the [Qubes Forum](https://forum.qubes-os.org/docs). External documentation should not be submitted to [qubes-doc](https://github.com/QubesOS/qubes-doc). If you've written a piece of documentation that is not appropriate for [qubes-doc](https://github.com/QubesOS/qubes-doc), we encourage you to submit it to the [Qubes Forum](https://forum.qubes-os.org/docs) instead. However, *linking* to external documentation from [qubes-doc](https://github.com/QubesOS/qubes-doc) is perfectly fine. Indeed, the maintainers of the [Qubes Forum](https://forum.qubes-os.org/) should regularly submit PRs against the documentation index (see [How to edit the documentation index](/doc/how-to-edit-the-documentation/#how-to-edit-the-documentation-index)) to add and update Qubes Forum links in the ["External documentation"](/doc/#external-documentation) section of the documentation table of contents.

The main difference between **core** (or **official**) and **external** (or **community** or **unofficial**) documentation is whether it documents software that is officially written and maintained by the Qubes OS Project. The purpose of this distinction is to keep the core docs maintainable and high-quality by limiting them to the software output by the Qubes OS Project. In other words, we take responsibility for documenting all of the software we put out into the world, but it doesn't make sense for us to take on the responsibility of documenting or maintaining documentation for anything else. For example, Qubes OS may use a popular Linux distribution for an official [TemplateVM](/doc/templates/). However, it would not make sense for a comparatively small project like ours, with modest funding and a lean workforce, to attempt to document software belonging to a large, richly-funded project with an army of paid and volunteer contributors, especially when they probably already have documentation of their own. This is particularly true when it comes to Linux in general. Although many users who are new to Qubes are also new to Linux, it makes absolutely no sense for our comparatively tiny project to try to document Linux in general when there is already a plethora of documentation out there.

Many contributors do not realize that there is a significant amount of work involved in *maintaining* documentation after it has been written. They may wish to write documentation and submit it to the core docs, but they see only their own writing process and fail to consider that it will have to be kept up-to-date and consistent with the rest of the docs for years afterward. Submissions to the core docs also have to [undergo a review process](/doc/how-to-edit-the-documentation/#security) to ensure accuracy before being merged, which takes up valuable time from the team. We aim to maintain high quality standards for the core docs (style and mechanics, formatting), which also takes up a lot of time. If the documentation involves anything external to the Qubes OS Project (such as a website, platform, program, protocol, framework, practice, or even a reference to a version number), the documentation is likely to become outdated when that external thing changes. It's also important to periodically review and update this documentation, especially when a new Qubes release comes out. Periodically, there may be technical or policy changes that affect all the core documentation. The more documentation there is relative to maintainers, the harder all of this will be. Since there are many more people who are willing to write documentation than to maintain it, these individually small incremental additions amount to a significant maintenance burden for the project.

On the positive side, we consider the existence of community documentation to be a sign of a healthy ecosystem, and this is quite common in the software world. The community is better positioned to write and maintain documentation that applies, combines, and simplifies the official documentation, e.g., tutorials that explain how to install and use various programs in Qubes, how to create custom VM setups, and introductory tutorials that teach basic Linux concepts and commands in the context of Qubes. In addition, just because the Qubes OS Project has officially written and maintains some flexible framework, such as `qrexec`, it does not make sense to include every tutorial that says "here's how to do something cool with `qrexec`" in the core docs. Such tutorials generally also belong in the community documentation.

See [#4693](https://github.com/QubesOS/qubes-issues/issues/4693) for more background information.

### Release-specific documentation

*See [#5308](https://github.com/QubesOS/qubes-issues/issues/5308) for pending changes to this policy.*

We maintain only one set of documentation for Qubes OS. We do not maintain a different set of documentation for each release of Qubes. Our single set of Qubes OS documentation is updated on a continual, rolling basis. Our first priority is to document all **current, stable releases** of Qubes. Our second priority is to document the next, upcoming release (if any) that is currently in the beta or release candidate stage.

In cases where a documentation page covers functionality that differs considerably between Qubes OS releases, the page should be subdivided into clearly-labeled sections that cover the different functionality in different releases (examples below).

In general, avoid mentioning specific Qubes versions in the body text of documentation, as these references rapidly go out of date and become misleading to readers.

#### Incorrect Example

```
## How to Foo

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
## Qubes 3.2

### How to Foo

Fooing is the process by which one foos. There are both general and specific
versions of fooing, which vary in usefulness depending on your goals, but for
the most part, all fooing is fooing.

To foo:

   $ qvm-foo <foo-bar>

Once you foo, make sure to close the baz before fooing the next bar.

## Qubes 4.0

### How to Foo

Fooing is the process by which one foos. There are both general and specific
versions of fooing, which vary in usefulness depending on your goals, but for
the most part, all fooing is fooing.

There is a special widget for fooing, which you can find in the lower-right
corner of the screen in the Foo Manager. Alternatively, you can use the
general `qubes-baz` command:

   $ qubes-baz --foo <bar>

Once you foo, make sure to close the baz before fooing the next bar.
```

Subdividing the page into clearly-labeled sections for each release has several benefits:

- It preserves good content for older (but still supported) releases. Many documentation contributors are also people who prefer to use the latest release. Many of them are tempted to *replace* existing content that applies to an older, supported release with content that applies only to the latest release. This is somewhat understandable. Since they only use the latest release, they may be focused on their own experience, and they may even regard the older release as deprecated, even when it's actually still supported. However, allowing this replacement of content would do a great disservice to those who still rely on the older, supported release. In many cases, these users value the stability and reliability of the older, supported release. With the older, supported release, there has been more time to fix bugs and make improvements in both the software and the documentation. Consequently, much of the documentation content for this release may have gone through several rounds of editing, review, and revision. It would be a tragedy for this content to vanish while the very set of users who most prize stability and reliability are depending on it.
- It's easy for readers to quickly find the information they're looking for, since they can go directly to the section that applies to their release.
- It's hard for readers to miss information they need, since it's all in one place. In the incorrect example, information that the reader needs could be in any paragraph in the entire document, and there's no way to tell without reading the entire page. In the correct example, the reader can simply skim the headings in order to know which parts of the page need to be read and which can be safely ignored. The fact that some content is repeated in the two release-specific sections is not a problem, since no reader has to read the same thing twice. Moreover, as one release gets updated, it's likely that the documentation for that release will also be updated. Therefore, content that is initially duplicated between release-specific sections will not necessarily stay that way, and this is a good thing: We want the documentation for a release that *doesn't* change to stay the same, and we want the documentation for a release that *does* change to change along with the software.
- It's easy for documentation contributors and maintainers to know which file to edit and update, since there's only one page for all Qubes OS releases. Initially creating the new headings and duplicating content that applies to both is only a one-time cost for each page, and many pages don't even require this treatment, since they apply to all currently-supported Qubes OS releases.

By contrast, an alternative approach, such as segregating the documentation into two different branches, would mean that contributions that apply to both Qubes releases would only end up in one branch, unless someone remembered to manually submit the same thing to the other branch and actually made the effort to do so. Most of the time, this wouldn't happen. When it did, it would mean a second pull request that would have to be reviewed. Over time, the different branches would diverge in non-release-specific content. Good general content that was submitted only to one branch would effectively disappear once that release was deprecated. (Even if it were still on the website, no one would look at it, since it would explicitly be in the subdirectory of a deprecated release, and there would be a motivation to remove it from the website so that search results wouldn't be populated with out-of-date information.)

For further discussion about release-specific documentation in Qubes, see [here](https://groups.google.com/d/topic/qubes-users/H9BZX4K9Ptk/discussion).

## Git conventions

Please follow our [Git commit message guidelines](/doc/coding-style/#commit-message-guidelines).
