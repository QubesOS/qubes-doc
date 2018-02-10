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


Important
---------

- **To disclose a security issue confidentially, please see the [Security] page.**
- **In all other cases, please do not email individual developers about bugs.**
- **Please note that many issues can be resolved by reading the [documentation].**


Where to submit your report
---------------------------

All issues pertaining to the Qubes OS Project (including auxiliary infrastructure such as the [website]) are tracked in [qubes-issues], our GitHub issues tracker.
However, [qubes-issues] is not intended for personal, localized troubleshooting questions, such as problems that affect only a specific laptop model.
Those questions should instead be asked in [qubes-users], where they are more likely to be answered.
Instead, [qubes-issues] is meant for tracking more general bugs and enhancements that affect a broad range of Qubes users.
Please see the sections [How to submit a report on GitHub] and [How to submit a report on the mailing lists] below for more information.


How to submit a report on GitHub
--------------------------------

**Before you submit an issue in [qubes-issues], please check to see whether it has already been reported.**
Search through the existing issues by typing your key words in the **Filters** box.
Make sure to check both currently open issues, as well as issues that are already closed.
If you find an issue that seems to be similar to yours, read through it.
If this issue is the same as yours, you can comment with additional information to help the maintainer debug it.
Adding a comment will subscribe you to email notifications, which can be helpful in getting important updates regarding the issue.
If you don't have anything to add but still want to receive email updates, you can click the "watch" button at the bottom of the comments.

When you file a new issue, you should be sure to include the version of Qubes you're using, as well as versions of related software packages.
If your issue is related to hardware, provide as many details as possible about the hardware, which could include using command-line tools such as `lspci`.
If you're reporting a bug in a package that is in a [testing] repository, please reference the appropriate issue in the [updates-status] repository.
Project maintainers really appreciate thorough explanations.
It usually helps them address the problem more quickly, so everyone wins!

Once your issue is addressed, your GitHub issue may be closed.
After that, the package containing the fix will move to the appropriate [testing] repository, then to the appropriate stable repository.
If you so choose, you can test the fix while it's in the [testing] repository, or you can wait for it to land in the stable repository.
If, after testing the fix, you find that it does not really fix your bug, please leave a comment on your issue explaining the situation.
When you do, we will receive a notification and respond on your issue or reopen it (or both).
Please **do not** create a duplicate issue or attempt to contact the developers individually about your problem.


How to submit a report on the mailing lists
-------------------------------------------

Before submitting a report on the mailing lists, please check to see whether your issue has already been reported by searching through the archives.
You can do this by visiting the Google Groups web interfaces for both [qubes-users] and [qubes-devel].
Please see the [Mailing Lists] page for further information.


How to copy information out of dom0
-----------------------------------

Copying information out of dom0 can be useful when reporting bugs.
See [Copying from (and to) dom0] for more information.


Testing new releases and updates
--------------------------------

Please see [Testing New Releases and Updates][testing].


Improving the code
------------------

Please see our guidelines on [how to contribute code].


[contribute to the Qubes OS Project]: /doc/contributing/
[Security]: /security/
[documentation]: /doc/
[website]: /
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues
[Mailing List]: /mailing-lists/
[qubes-users]: /mailing-lists/#qubes-users
[qubes-devel]: /mailing-lists/#qubes-devel
[How to submit a report on GitHub]: #how-to-submit-a-report-on-github
[How to submit a report on the mailing lists]: #how-to-submit-a-report-on-the-mailing-lists
[testing]: /doc/testing/
[updates-status]: https://github.com/QubesOS/updates-status/issues
[Copying from (and to) dom0]: /doc/copy-from-dom0/
[how to contribute code]: /doc/contributing/#contributing-code

