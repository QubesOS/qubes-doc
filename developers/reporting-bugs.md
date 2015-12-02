---
layout: doc
title: Reporting Bugs
permalink: /doc/reporting-bugs/
redirect_from:
- /en/doc/reporting-bugs/
- /doc/BugReportingGuide/
- /wiki/BugReportingGuide/
---

Bug Reporting Guide
===================

One of the most important contribution task is reporting the bugs you have found.

Asking a Question
-----------------

Before you ask, do some searching and reading. Check [the
docs](https://www.qubes-os.org/doc/), Google, GitHub, and StackOverflow. If
your question is something that has been answered many times before, the
project maintainers might be tired of repeating themselves.

Whenever possible, ask your question on the Qubes mailing list which is
located [here](https://groups.google.com/forum/#!forum/qubes-users). This
allows anyone to answer and makes the answer available for the next person
with the same question.

Submitting a Bug Report (or "Issue")
------------------------------------

On GitHub, "Bug Reports" are called "Issues."

Issues can be submitted to the Qubes project located at
[https://github.com/QubesOS/qubes-issues](https://github.com/QubesOS/qubes-issues).

### Has This Been Asked Before?

Before you submit a bug report, you should search existing issues. Be sure
to check both currently open issues, as well as issues that are already
closed. If you find an issue that seems to be similar to yours, read
through it.

If this issue is the same as yours, you can comment with additional
information to help the maintainer debug it. Adding a comment will
subscribe you to email notifications, which can be helpful in getting
important updates regarding the issue. If you don't have anything to add
but still want to receive email updates, you can click the "watch" button
at the bottom of the comments.

### Nope, Hasn't Been Asked Before

If you can't find anything in the existing issues, don't be shy about
filing a new one.

You should be sure to include the version the project, as well as versions
of related software. For example, be sure to include the Qubes release
version (R2, R3) and specific version numbers of package causing problems
(if known).
If your issue is related to hardware, provide as many details as possible
about the hardware, which could include using commandline tools such as
`lspci`.

Project maintainers really appreciate thorough explanations. It usually
helps them address the problem more quickly, so everyone wins!

Improving the Code
------------------

The best way is to "Fork" the repo on GitHub. This will create a copy of
the repo on your GitHub account.

Before you set out to improve the code, you should have a focused idea in
mind of what you want to do.

Each commit should do one thing, and each PR should be one specific
improvement. Each PR needs to be signed.

* [How can I contribute to the Qubes Project?](https://www.qubes-os.org/doc/ContributingHowto/)
* [Developer Documentation](https://www.qubes-os.org/doc/)
* [Package Release Workflow](https://github.com/QubesOS/qubes-builder/blob/master/doc/ReleaseManagerWorkflow.md)
