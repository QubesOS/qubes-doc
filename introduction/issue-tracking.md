---
lang: en
layout: doc
permalink: /doc/issue-tracking/
redirect_from:
- /doc/reporting-bugs/
- /en/doc/reporting-bugs/
- /doc/BugReportingGuide/
- /wiki/BugReportingGuide/
- /reporting-bugs/
- /bug/
- /bugs/
- /bug-report/
- /bug-reports/
ref: 121
title: Issue tracking
---

We use [GitHub Issues](https://docs.github.com/en/issues) as our [issue
tracking system](https://en.wikipedia.org/wiki/Issue_tracking_system). All
issues pertaining to the Qubes OS Project (including auxiliary infrastructure
such as this website) are tracked in
[qubes-issues](https://github.com/QubesOS/qubes-issues/issues).

## How to open a new issue

First, let's make sure the issue tracker is the right place.

### I need help, have a question, or want to discuss something.

We're happy to help, answer questions, and have discussions, but the issue
tracker is not the right place for these activities. Instead, please see [Help,
Support, Mailing Lists, and Forum](/support/).

### I see something that should be changed in the documentation.

We encourage you to submit the change yourself! Please see the [how to edit the
documentation](/doc/how-to-edit-the-documentation/) for instructions on how to
do so. If it's something you can't do yourself, please proceed to open an issue.

### I would like to report a security vulnerability.

Thank you! If the vulnerability is confidential, please do not report it in our
public issue tracker. Instead, please see [Reporting Security Issues in Qubes
OS](/security/#reporting-security-issues-in-qubes-os).

### I still want to open an issue.

Great! Thank you for taking the time and effort to help improve Qubes! To
ensure the process is efficient and productive for everyone involved, please
follow these steps:

 1. Carefully read our issue tracking [guidelines](#guidelines). If your issue
    would violate any of the guidelines, **stop**. Please do not submit it.
 2. [Search through the existing issues](#search-tips), both open and closed,
    to see if your issue already exists. If it does, **stop**. [Do not open a
    duplicate.](/doc/issue-tracking/#new-issues-should-not-be-duplicates-of-existing-issues)
    Instead, comment on the existing issue.
 3. Go [here](https://github.com/QubesOS/qubes-issues/issues/new/choose).
 4. Select the [type](#type) of issue you want to open.
 5. Enter a descriptive title.
 6. Do not delete the provided issue template. Fill out every applicable
    section.
 7. Make sure to mention any relevant documentation and other issues you've
    already seen. We don't know what you've seen unless you tell us. If you
    don't list it, we'll assume you haven't seen it.
 8. If any sections of the issue template are *truly* not applicable, you may
    remove them, **except for the documentation and related issues sections**.
 9. Submit your issue.
10. Respond to any questions the official team asks. For example, you may be
    asked to provide specific logs or other additional information.

Eventually, your issue may be closed. See [how issues get
closed](/doc/issue-tracking/#how-issues-get-closed) for details about when,
why, and how this occurs.

## Labels, Milestones, and Projects

Labels, milestones, and projects are features of GitHub's issue tracking system
that we use to keep
[qubes-issues](https://github.com/QubesOS/qubes-issues/issues) organized.

### Labels

Only Qubes team members have permission to modify
[labels](https://github.com/QubesOS/qubes-issues/labels) and
[milestones](https://github.com/QubesOS/qubes-issues/milestones). Many labels
and milestones have descriptions on them that can be viewed either in their
respective lists or by hovering over them. Let's go over some of the most
important ones.

#### Type

There are three **types**: `T: bug`, `T: enhancement`, and `T: task`.

- `T: bug` --- Type: bug report. A problem or defect resulting in unintended
  behavior in something that exists.
- `T: enhancement` --- Type: enhancement. A new feature that does not yet exist
  **or** improvement of existing functionality.
- `T: task` --- Type: task. An action item that is neither a bug nor an
  enhancement.

Every open issue should have **exactly one** type. An open issue should not
have more than one type, and it should not lack a type entirely. Bug reports
are for things that already exist. If something doesn't exist yet, but you
think it should exist, then `T: enhancement`. If something already exists and
could be improved in some way, `T: enhancement` is appropriate. `T: task` is
for issues that fall under under neither `T: bug` nor `T: enhancement`.

#### Priority

There are several **priority** levels ranging from `P: minor` to `P: blocker`
(see [here](https://github.com/QubesOS/qubes-issues/labels?q=P%3A) for the full
list). Every open issue should have **exactly one** priority. An open issue
should not have more than one priority, and it should not lack a priority
entirely.

#### Component

There are many **component** labels, each beginning with `C:` (see
[here](https://github.com/QubesOS/qubes-issues/labels?page=2&q=C%3A) for the
full list). Every open issue should have **at least one** component. An open
issue may have more than one component, but it should not lack a component
entirely. When no other component applies, use `C: other`.

### Milestones

The issue tracker has several
[milestones](https://github.com/QubesOS/qubes-issues/milestones). Every issue
should be assigned to **exactly one** milestone. The issue tracker does not
allow assigning an issue to more than one milestone. If an issue is already
assigned to a milestone, assigning it to a different one will *replace* the
existing milestone assignment. No open issue should lack a milestone
assignment.

Most milestones correspond to specific Qubes OS releases. A bug report assigned
to a release milestone indicates an alleged bug *in* that Qubes OS release. A
task or enhancement assigned to a release milestone indicates that the goal is
to implement or do that thing *in* or *for* that Qubes OS release.

The `TBD` (To Be Determined) milestone is for enhancements or tasks that will
be specific to a Qubes OS release but have yet to be assigned to a specific
release milestone. Bug reports should never be assigned to this milestone,
because every bug is a problem or defect in something that already exists.

The `Ongoing` milestone is for issues that are independent of the Qubes OS
release cycle, including (but not limited to) website, documentation, and
project management issues. These are issues that will never be assigned to a
specific Qubes OS release milestone.

### Projects

The issue tracker has several
[projects](https://github.com/QubesOS/qubes-issues/projects). A project is a
way to create a group of multiple related issues. This is the preferred method
of grouping issues, whereas trying to use normal issues as "meta-issues" or
"epics" is discouraged.

## Search Tips

[Search both open and closed
issues.](https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aissue)
For example, you may be experiencing a bug that was just fixed, in which case
the report for that bug is probably closed. In this case, it would be useful to
view [all bug reports, both open and closed, with the most recently updated
sorted to the
top](https://github.com/QubesOS/qubes-issues/issues?q=label%3Abug+sort%3Aupdated-desc).

[Search using labels.](https://github.com/QubesOS/qubes-issues/labels) For
example, you can search issues by priority
([blocker](https://github.com/QubesOS/qubes-issues/labels/P%3A%20blocker),
[critical](https://github.com/QubesOS/qubes-issues/labels/P%3A%20critical),
[major](https://github.com/QubesOS/qubes-issues/labels/P%3A%20major), etc.) and
by component
([core](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+core%22),
[manager/widget](https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A%22C%3A+manager%2Fwidget%22+),
[Xen](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+Xen%22),
etc.).

You can also try searching by
[milestone](https://github.com/QubesOS/qubes-issues/milestones) and by
[project](https://github.com/QubesOS/qubes-issues/projects).

## Guidelines

### The issue tracker is not a discussion forum

The issue tracker is a tool to help the developers be more productive and
efficient in their work. It is not a place for discussion. If you wish to
discuss something in the issue tracker, please do so on the forum or mailing
lists (see [Help, Support, Mailing Lists, and Forum](/support/)). You can
simply link to the relevant issue in your discussion post.

This guideline is important for keeping issues focused on *actionable
information*, which helps the developers to stay focused on their work. When
developers come back to an issue to work on it, we do not want them to have to
sift through a large number of unnecessary comments before they can get
started. In many cases, an issue that gets "too big" essentially becomes more
trouble than it's worth, and no developer will touch it (also see [every issue
must be about a single, actionable
thing](#every-issue-must-be-about-a-single-actionable-thing)). In these cases,
we sometimes have to close the issue and open a new one. This is a waste of
energy for everyone involved, so we ask that everyone help to avoid repeating
this pattern.

### Do not submit questions

[qubes-issues](https://github.com/QubesOS/qubes-issues/issues) is not the place
to ask questions. This includes, but is not limited to, troubleshooting
questions and questions about how to do things with Qubes. Instead, see [Help,
Support, Mailing Lists, and Forum](/support/) for appropriate place to ask
questions. By contrast,
[qubes-issues](https://github.com/QubesOS/qubes-issues/issues) is meant for
tracking more general bugs, enhancements, and tasks that affect a broad range
of Qubes users.

### Use the issue template

When you open a new issue, an issue template is provided for you. Please use
it. Do not delete it. The issue template is carefully designed to elicit
important information. Without this information, the issue is likely to be
incomplete. (If certain sections are not applicable, you may remove them, but
please do so only sparingly and only if they are *truly* not applicable.)

It is also important to note the placement and content of the HTML comments in
the issue template. These help us to have issues with a consistent format.

### Every issue must be about a single, actionable thing

If your issue is not actionable, please see [Help, Support, Mailing Lists, and
Forum](/support/) for the appropriate place to post it. If your issue would be
about more than one thing, file them as separate issues instead. This means we
should generally not try to use a single issue as a "meta" or "epic" issue that
exists only to group, contain, or track other issues. Instead, when there is a
need to group multiple related issues together, use
[projects](https://github.com/QubesOS/qubes-issues/projects).

This guideline is extremely important for making the issue tracker a useful
tool for the developers. When an issue is too big and composite, it becomes
intractable and drastically increases the likelihood that nothing will get
done. Such issues also tend to encourage an excessive amount of general
discussion that is simply not appropriate for a technical issue tracker (see
[the issue tracker is not a discussion
forum](#the-issue-tracker-is-not-a-discussion-forum)).

### New issues should not be duplicates of existing issues

Before you submit an issue, check to see whether it has already been reported.
Search through the existing issues -- both open and closed -- by typing your
key words in the **Filters** box. If you find an issue that seems to be similar
to yours, read through it. If you find an issue that is the same as or subsumes
yours, leave a comment on the existing issue rather than filing a new one, even
if the existing issue is closed. If an issue affects more than one Qubes
version, we usually keep only one issue for all versions. The Qubes team will
see your comment and reopen the issue, if appropriate. For example, you can
leave a comment with additional information to help the maintainer debug it.
Adding a comment will subscribe you to email notifications, which can be
helpful in getting important updates regarding the issue. If you don't have
anything to add but still want to receive email updates, you can click the
"Subscribe" button at the side or bottom of the comments.

### Every issue must be of a single type

Every issue must be exactly one of the following types: a bug report (`bug`), a
feature or improvement request (`enhancement`), or a task (`task`). Do not file
multi-typed issues. Instead, file multiple issues of distinct types. The Qubes
team will classify your issue according to its type.

### New issues should include all relevant information

When you file a new issue, you should be sure to include the version of Qubes
you're using, as well as versions of related software packages ([how to copy
information out of dom0](/doc/how-to-copy-from-dom0/)). If your issue is
related to hardware, provide as many details as possible about the hardware. A
great way to do this is by [generating and submitting a Hardware Compatibility
List (HCL) report](/doc/hcl/#generating-and-submitting-new-reports), then
linking to it in your issue. You may also need to use command-line tools such
as `lspci`. If you're reporting a bug in a package that is in a
[testing](/doc/testing/) repository, please reference the appropriate issue in
the [updates-status](https://github.com/QubesOS/updates-status/issues)
repository. Project maintainers really appreciate thorough explanations. It
usually helps them address the problem more quickly, so everyone wins!

### There are no guarantees that your issue will be addressed

Keep in mind that
[qubes-issues](https://github.com/QubesOS/qubes-issues/issues) is an issue
tracker, not a support system. Creating a new issue is simply a way for you to
submit an item for the Qubes team's consideration. It is up to the Qubes team
to decide whether or how to address your issue, which may include closing the
issue without taking any action on it. Even if your issue is kept open,
however, you should not expect it to be addressed within any particular time
frame, or at all. At the time of this writing, there are well over one thousand
open issues in [qubes-issues](https://github.com/QubesOS/qubes-issues/issues).
The Qubes team has its own roadmap and priorities, which will govern the manner
and order in which open issues are addressed.

## How issues get closed

If the Qubes developers make a code change that resolves an issue, then the
issue will typically be [closed from the relevant commit or merged pull request
(PR)](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/linking-a-pull-request-to-an-issue).

### Bug reports

In the case of bugs, the package containing the change will move to the
appropriate [testing](/doc/testing/) repository, then to the appropriate stable
repository. If you so choose, you can test the fix while it's in the
[testing](/doc/testing/) repository, or you can wait for it to land in the
stable repository. If, after testing the fix, you find that it does not really
fix the reported bug, please leave a comment on the issue explaining the
situation. When you do, we will receive a notification and respond on the issue
or reopen it (or both). Please **do not** create a duplicate issue or attempt
to contact the developers individually about a problem.

### Resolution

In other cases, an issue may be closed with a specific resolution, such as `R:
invalid`, `R: duplicate`, or `R: won't fix`. Each of these labels has a
description that explains the label. We'll also leave a comment explaining why
we're closing the issue with one of these specific resolutions. If the issue is
closed without one of these specific resolutions, then it means, by default,
that the reported bug was fixed or the requested enhancement was implemented.

### Backports

Issues in GitHub can only be open or closed, but, when it comes to bugs that
affect multiple versions of Qubes OS, there are several possible states:

1. Not fixed yet
2. Fix developed but not yet committed (PR open)
3. Fix committed (PR merged), but update not yet pushed to any repo
4. Update pushed to testing repo for the most recent development version
5. Update pushed to stable repo for the most recent development version
6. Update backported to stable version(s) and pushed to the testing repo
7. Update pushed to stable repo of stable version(s)

We close issues at step 3. Then, as updates are released, the issue
automatically gets the appropriate `current-testing` (`rX.Y-*-cur-test`) and
`stable` (`rX.Y-*-stable`) labels. Based on these labels, it's possible to
select issues waiting for step 6 (see [issues by
release](https://github.com/QubesOS/qubes-issues#issues-by-release)).

Therefore, if you see that an issue is closed, but the fix is not yet available
to you, be aware that it may be at an intermediate stage of this process
between issue closure and the update being available in whichever repos you
have enabled in whichever version of Qubes you're using.

In order to assist with this, we have a label called [backport
pending](https://github.com/QubesOS/qubes-issues/labels/backport%20pending),
which means, "The fix has been released for the testing release but is pending
backport to the stable release." Our infrastructure will attempt to apply this
label automatically, when appropriate, but it is not perfect, and the
developers may be need to adjust it manually.
