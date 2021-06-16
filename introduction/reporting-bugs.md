---
lang: en
layout: doc
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
---

# Reporting bugs and other issues #

All issues pertaining to the Qubes OS Project (including auxiliary infrastructure such as the [website](/)) are tracked in [qubes-issues](https://github.com/QubesOS/qubes-issues/issues), our GitHub issue tracker.
If you're looking for help, please see [Help, Support, Mailing Lists, and Forum](/support/).

## Important ##

- **To disclose a security issue confidentially, please see the [Security](/security/) page.**
- **In all other cases, please do not email individual developers about issues.**
- **Please note that many issues can be resolved by reading the [documentation](/doc/).**
- **If you see something that should be changed in the documentation, [submit a change](/doc/doc-guidelines/).**

## Search Tips ##

[Search both open and closed issues.](https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aissue)
For example, you may be experiencing a bug that was just fixed, in which case the report for that bug is probably closed.
In this case, it would be useful to view [all bug reports, both open and closed, with the most recently updated sorted to the top](https://github.com/QubesOS/qubes-issues/issues?q=label%3Abug+sort%3Aupdated-desc).

[Search using labels.](https://github.com/QubesOS/qubes-issues/labels)
For example, you can search issues by priority ([blocker](https://github.com/QubesOS/qubes-issues/labels/P%3A%20blocker), [critical](https://github.com/QubesOS/qubes-issues/labels/P%3A%20critical), [major](https://github.com/QubesOS/qubes-issues/labels/P%3A%20major), etc.) and by component ([core](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+core%22), [manager/widget](https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A%22C%3A+manager%2Fwidget%22+), [Xen](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+Xen%22), etc.).

Only Qubes team members can apply labels.
Every issue must have exactly one **type** (`T: bug`, `T: enhancement`, or `T: task`), exactly one **priority** (e.g., `P: major`), and at least one **component** (e.g., `C: core`).
Issues may have additional labels, if applicable (e.g., `crypto`, `ux`).

## Issue tracker guidelines ##

### The issue tracker is not a discussion forum ###

The issue tracker is a tool to help the developers be more productive and efficient in their work.
It is not a place for discussion.
If you wish to discuss something in the issue tracker, please do so on the forum or mailing lists (see [Help, Support, Mailing Lists, and Forum](/support/)).
You can simply link to the relevant issue in your discussion post.

This guideline is important for keeping issues focused on *actionable information*, which helps the developers to stay focused on their work.
When developers come back to an issue to work on it, we do not want them to have to sift through a large number of unnecessary comments before they can get started.
In many cases, an issue that gets "too big" essentially becomes more trouble than it's worth, and no developer will touch it (also see [every issue must be about a single, actionable thing](#every-issue-must-be-about-a-single-actionable-thing)).
In these cases, we sometimes have to close the issue and open a new one.
This is a waste of energy for everyone involved, so we ask that everyone help to avoid repeating this pattern.

### Do not submit questions ###

[qubes-issues](https://github.com/QubesOS/qubes-issues/issues) is not the place to ask questions.
This includes, but is not limited to, troubleshooting questions and questions about how to do things with Qubes.
Instead, see [Help, Support, Mailing Lists, and Forum](/support/) for appropriate place to ask questions.
By contrast, [qubes-issues](https://github.com/QubesOS/qubes-issues/issues) is meant for tracking more general bugs, enhancements, and tasks that affect a broad range of Qubes users.

### Use the issue template ###

When you open a new issue, an issue template is provided for you.
Please use it.
Do not delete it.
The issue template is carefully designed to elicit important information.
Without this information, the issue is likely to be incomplete.
(If certain sections are not applicable, you may remove them, but please do so only sparingly and only if they are *truly* not applicable.)

It is also important to note the placement and content of the HTML comments in the issue template.
These help us to have issues with a consistent format.

### Every issue must be about a single, actionable thing ###

If your issue is not actionable, please see [Help, Support, Mailing Lists, and Forum](/support/) for the appropriate place to post it.
If your issue would be about more than one thing, file them as separate issues instead.
This means we should generally not try to use a single issue as a "meta" or "epic" issue that exists only to group, contain, or track other issues.
Instead, when there is a need to group multiple related issues together, use [projects](https://github.com/QubesOS/qubes-issues/projects).

This guideline is extremely important for making the issue tracker a useful tool for the developers.
When an issue is too big and composite, it becomes intractable and drastically increases the likelihood that nothing will get done.
Such issues also tend to encourage an excessive amount of general discussion that is simply not appropriate for a technical issue tracker (see [the issue tracker is not a discussion forum](#the-issue-tracker-is-not-a-discussion-forum)).

### New issues should not be duplicates of existing issues ###

Before you submit an issue, check to see whether it has already been reported.
Search through the existing issues -- both open and closed -- by typing your key words in the **Filters** box.
If you find an issue that seems to be similar to yours, read through it.
If you find an issue that is the same as or subsumes yours, leave a comment on the existing issue rather than filing a new one, even if the existing issue is closed.
If an issue affects more than one Qubes version, we usually keep only one issue for all versions.
The Qubes team will see your comment and reopen the issue, if appropriate.
For example, you can leave a comment with additional information to help the maintainer debug it.
Adding a comment will subscribe you to email notifications, which can be helpful in getting important updates regarding the issue.
If you don't have anything to add but still want to receive email updates, you can click the "Subscribe" button at the side or bottom of the comments.

### Every issue must be of a single type ###

Every issue must be exactly one of the following types: a bug report (`bug`), a feature or improvement request (`enhancement`), or a task (`task`).
Do not file multi-typed issues.
Instead, file multiple issues of distinct types.
The Qubes team will classify your issue according to its type.

### New issues should include all relevant information ###

When you file a new issue, you should be sure to include the version of Qubes you're using, as well as versions of related software packages ([how to copy information out of dom0](/doc/copy-from-dom0/)).
If your issue is related to hardware, provide as many details as possible about the hardware.
A great way to do this is by [generating and submitting a Hardware Compatibility List (HCL) report](/doc/hcl/#generating-and-submitting-new-reports), then linking to it in your issue.
You may also need to use command-line tools such as `lspci`.
If you're reporting a bug in a package that is in a [testing](/doc/testing/) repository, please reference the appropriate issue in the [updates-status](https://github.com/QubesOS/updates-status/issues) repository.
Project maintainers really appreciate thorough explanations.
It usually helps them address the problem more quickly, so everyone wins!

### There are no guarantees that your issue will be addressed ###

Keep in mind that `qubes-issues` is an issue tracker, not a support system.
Creating a new issue is simply a way for you to submit an item for the Qubes team's consideration.
It is up to the Qubes team to decide whether or how to address your issue, which may include closing the issue without taking any action on it.
Even if your issue is kept open, however, you should not expect it to be addressed within any particular time frame, or at all.
At the time of this writing, there are well over one thousand open issues in `qubes-issues`.
The Qubes team has its own roadmap and priorities, which will govern the manner and order in which open issues are addressed.

## Following up afterward ##

If the Qubes developers make a code change that resolves your issue, then your GitHub issue will typically be closed from the relevant patch message.
After that, the package containing the fix will move to the appropriate [testing](/doc/testing/) repository, then to the appropriate stable repository.
If you so choose, you can test the fix while it's in the [testing](/doc/testing/) repository, or you can wait for it to land in the stable repository.
If, after testing the fix, you find that it does not really fix your bug, please leave a comment on your issue explaining the situation.
When you do, we will receive a notification and respond on your issue or reopen it (or both).
Please **do not** create a duplicate issue or attempt to contact the developers individually about your problem.

In other cases, your issue may be closed with a specific resolution, such as `R: invalid`, `R: duplicate`, or `R: won't fix`.
Each of these labels has a description that explains the label.
We'll also leave a comment explaining why we're closing the issue with one of these specific resolutions.
If the issue is closed without one of these specific resolutions, then it means, by default, that your reported bug was fixed or your requested enhancement was implemented.

## See also ##

- [Help, Support, Mailing Lists, and Forum](/support/)
- [Testing New Releases and Updates](/doc/testing/)
- [How to Contribute](/doc/contributing/)
- [Contributing Code](/doc/contributing/#contributing-code)
- [Package Contributions](/doc/package-contributions/)
- [Documentation Guidelines](/doc/doc-guidelines/)

