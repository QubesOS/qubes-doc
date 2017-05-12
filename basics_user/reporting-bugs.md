---
layout: doc
title: Reporting Bugs
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

Reporting Bugs
==============

One of the most important ways in which you can [contribute to the Qubes OS Project] is by reporting any bugs you have found. 
Please note that there is a separate process for [reporting security issues](/security/).


Before you submit a report
--------------------------

Before you submit a bug report, please take a moment to:

 * Check whether your issue has already been reported.
 
 * Determine which venue is most appropriate for it.

 * Read the [documentation] to see whether what you've found is really a bug.

 * Search through the existing [Qubes issues][qubes-issues] by typing your key
   words in the **Filters** box. Make sure to check both currently open issues,
   as well as issues that are already closed. If you find an issue that seems to
   be similar to yours, read through it. If this issue is the same as yours, you
   can comment with additional information to help the maintainer debug it.
   Adding a comment will subscribe you to email notifications, which can be
   helpful in getting important updates regarding the issue. If you don't have
   anything to add but still want to receive email updates, you can click the
   "watch" button at the bottom of the comments.

 * Search through our [mailing list] archives by visiting the Google Groups web
   interfaces for both [qubes-users] and [qubes-devel].


Where to submit your report
---------------------------

Our [GitHub issues][qubes-issues] tracker is not intended for personal,
localized troubleshooting questions, such as problems that affect only a
specific laptop model. Those questions are more likely to be answered in
[qubes-users], which receives much more traffic. Instead, GitHub issues are
meant to track more general bugs and enhancements that affect a broad range of
Qubes users.


How to copy information out of Dom0
-----------------------------------

See [Copying from (and to) dom0](/doc/copy-from-dom0/).


How to submit a report on the mailing lists
-------------------------------------------

Please see the [mailing list guidelines][mailing list].


How to submit a report on GitHub
--------------------------------

We track all bugs in the [qubes-issues] tracker on GitHub.

When you file a new issue, you should be sure to include the version of Qubes
you're using, as well as versions of related software packages. If your issue is
related to hardware, provide as many details as possible about the hardware,
which could include using command-line tools such as `lspci`.
If you're reporting a bug in a package that is in a [testing] repository, please reference the appropriate issue in the [updates-status] repository.

Project maintainers really appreciate thorough explanations. It usually
helps them address the problem more quickly, so everyone wins!


Testing new releases and updates
--------------------------------

Please see [Testing New Releases and Updates][testing].


Improving the code
------------------

Please see our guidelines on [how to contribute code].


[contribute to the Qubes OS Project]: /doc/contributing/
[documentation]: /doc/
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues
[mailing list]: https://www.qubes-os.org/mailing-lists/
[qubes-users]: https://groups.google.com/group/qubes-users
[qubes-devel]: https://groups.google.com/group/qubes-devel
[testing]: /doc/testing/
[updates-status]: https://github.com/QubesOS/updates-status/issues
[how to contribute code]: /doc/contributing/#contributing-code

