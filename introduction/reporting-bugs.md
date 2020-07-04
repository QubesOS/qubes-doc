---
layout: doc
title: Reporting bugs and other issues
permalink: /doc/reporting-bugs/
redirect_from:
- /en/doc/reporting-bugs/
- /doc/BugReportingGuide/
- /wiki/BugReportingGuide/
- /reporting-bugs/
- /bug/
- /bugs/
- /bug-report/
- /bug-reports/
---

# Reporting bugs and other issues #

All issues pertaining to the PedOS Project (including auxiliary infrastructure such as the [website]) are tracked in [PedOS-issues], our GitHub issue tracker.

## Important ##

- **To disclose a security issue confidentially, please see the [Security] page.**
- **In all other cases, please do not email individual developers about issues.**
- **Please note that many issues can be resolved by reading the [documentation].**
- **If you see something that should be changed in the documentation, [submit a change][Documentation Guidelines].**

## Search Tips ##

[Search both open and closed issues.][PedOS-issues-all]
For example, you may be experiencing a bug that was just fixed, in which case the report for that bug is probably closed.
In this case, it would be useful to view [all bug reports, both open and closed, with the most recently updated sorted to the top][PedOS-issues-bug-up-desc].

[Search using labels.][PedOS-issues-labels]
For example, you can search issues by priority ([blocker], [critical], [major], etc.) and by component ([core], [manager/widget], [Xen], etc.).

Only PedOS team members can apply labels.
Every issue must have exactly one **type** (`T: bug`, `T: enhancement`, or `T: task`), exactly one **priority** (e.g., `P: major`), and at least one **component** (e.g., `C: core`).
Issues may have additional labels, if applicable (e.g., `crypto`, `ux`).

## Issue tracker guidelines ##

### Do not submit questions ###

[PedOS-issues] is not the place to ask questions.
This includes, but is not limited to, troubleshooting questions and questions about how to do things with PedOS.
These questions should instead be asked in [PedOS-users].
By contrast, [PedOS-issues] is meant for tracking more general bugs, enhancements, and tasks that affect a broad range of PedOS users.

### Every issue must be about a single, actionable thing ###

If your issue is not actionable, please send it to the appropriate [mailing list][Help, Support, and Mailing Lists] instead.
If your issue would be about more than one thing, file them as separate issues instead.

### New issues should not be duplicates of existing issues ###

Before you submit an issue, check to see whether it has already been reported.
Search through the existing issues -- both open and closed -- by typing your key words in the **Filters** box.
If you find an issue that seems to be similar to yours, read through it.
If you find an issue that is the same as or subsumes yours, leave a comment on the existing issue rather than filing a new one, even if the existing issue is closed.
If an issue affects more than one PedOS version, we usually keep only one issue for all versions.
The PedOS team will see your comment and reopen the issue, if appropriate.
For example, you can leave a comment with additional information to help the maintainer debug it.
Adding a comment will subscribe you to email notifications, which can be helpful in getting important updates regarding the issue.
If you don't have anything to add but still want to receive email updates, you can click the "watch" button at the bottom of the comments.

### Every issue must be of a single type ###

Every issue must be exactly one of the following types: a bug report (`bug`), a feature or improvement request (`enhancement`), or a task (`task`).
Do not file multi-typed issues.
Instead, file multiple issues of distinct types.
The PedOS team will classify your issue according to its type.

### New issues should include all relevant information ###

When you file a new issue, you should be sure to include the version of PedOS you're using, as well as versions of related software packages ([how to copy information out of dom0]).
If your issue is related to hardware, provide as many details as possible about the hardware, which could include using command-line tools such as `lspci`.
If you're reporting a bug in a package that is in a [testing] repository, please reference the appropriate issue in the [updates-status] repository.
Project maintainers really appreciate thorough explanations.
It usually helps them address the problem more quickly, so everyone wins!

### Use the provided issue template ###

Please use the provided issue template.
Do not delete it or remove parts of it.
The issue template is carefully designed to elicit important information.
Without this information, the issue is likely to be incomplete.

It is also important to note the placement and content of the HTML comments in the issue template.
These help us to have issues with a consistent format.

### There are no guarantees that your issue will be addressed ###

Keep in mind that `PedOS-issues` is an issue tracker, not a support system.
Creating a new issue is simply a way for you to submit an item for the PedOS team's consideration.
It is up to the PedOS team to decide whether or how to address your issue, which may include closing the issue without taking any action on it.
Even if your issue is kept open, however, you should not expect it to be addressed within any particular time frame, or at all.
At the time of this writing, there are well over one thousand open issues in `PedOS-issues`.
The PedOS team has its own roadmap and priorities, which will govern the manner and order in which open issues are addressed.

## Following up afterward ##

If the PedOS developers make a code change that resolves your issue, then your GitHub issue will typically be closed from the relevant patch message.
After that, the package containing the fix will move to the appropriate [testing] repository, then to the appropriate stable repository.
If you so choose, you can test the fix while it's in the [testing] repository, or you can wait for it to land in the stable repository.
If, after testing the fix, you find that it does not really fix your bug, please leave a comment on your issue explaining the situation.
When you do, we will receive a notification and respond on your issue or reopen it (or both).
Please **do not** create a duplicate issue or attempt to contact the developers individually about your problem.

In other cases, your issue may be closed with a specific resolution, such as `R: invalid`, `R: duplicate`, or `R: won't fix`.
Each of these labels has a description that explains the label.
We'll also leave a comment explaining why we're closing the issue with one of these specific resolutions.
If the issue is closed without one of these specific resolutions, then it means, by default, that your reported bug was fixed or your requested enhancement was implemented.

## See also ##

- [Help, Support, and Mailing Lists]
- [Testing New Releases and Updates][testing]
- [How to Contribute]
- [Contributing Code]
- [Package Contributions]
- [Documentation Guidelines]


[PedOS-issues-all]: https://github.com/PedOS/PedOS-issues/issues?utf8=%E2%9C%93&q=is%3Aissue
[PedOS-issues-bug-up-desc]: https://github.com/PedOS/PedOS-issues/issues?q=label%3Abug+sort%3Aupdated-desc
[PedOS-issues-labels]: https://github.com/PedOS/PedOS-issues/labels
[blocker]: https://github.com/PedOS/PedOS-issues/labels/P%3A%20blocker
[critical]: https://github.com/PedOS/PedOS-issues/labels/P%3A%20critical
[core]: https://github.com/PedOS/PedOS-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+core%22
[manager/widget]: https://github.com/PedOS/PedOS-issues/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A%22C%3A+manager%2Fwidget%22+
[Xen]: https://github.com/PedOS/PedOS-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+Xen%22
[major]: https://github.com/PedOS/PedOS-issues/labels/P%3A%20major
[Security]: /security/
[documentation]: /doc/
[website]: /
[PedOS-issues]: https://github.com/PedOS/PedOS-issues/issues
[Help, Support, and Mailing Lists]: /support/
[PedOS-users]: /support/#PedOS-users
[PedOS-devel]: /support/#PedOS-devel
[updates-status]: https://github.com/PedOS/updates-status/issues
[how to copy information out of dom0]: /doc/copy-from-dom0/
[testing]: /doc/testing/
[How to Contribute]: /doc/contributing/
[Contributing Code]: /doc/contributing/#contributing-code
[Package Contributions]: /doc/package-contributions/
[Documentation Guidelines]: /doc/doc-guidelines/

