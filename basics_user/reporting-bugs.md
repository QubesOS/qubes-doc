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


`qubes-issues` guidelines
-------------------------

All issues pertaining to the Qubes OS Project (including auxiliary infrastructure such as the [website]) are tracked in [qubes-issues], our GitHub issue tracker.

- **Do not submit questions.**
  [qubes-issues] is not the place to ask questions.
  This includes, but is not limited to, troubleshooting questions and questions about how to do things with Qubes.
  These questions should instead be asked in [qubes-users].
  Instead, [qubes-issues] is meant for tracking more general bugs, enhancements, and tasks that affect a broad range of Qubes users.

- **Every issue must be about a single, actionable thing.**
  If your issue is not actionable, please send it to the appropriate [mailing list][mailing list guidelines] instead.
  If your issue would be about more than one thing, file them as separate issues instead.

- **New issues should not be duplicates of existing issues.**
  Before you submit an issue, check to see whether it has already been reported.
  Search through the existing issues -- both open and closed -- by typing your key words in the **Filters** box.
  If you find an issue that seems to be similar to yours, read through it.
  If you find an issue that is the same as or subsumes yours, leave a comment on the existing issue rather than filing a new one, even if the existing issue is closed.
  The Qubes team will see your comment and reopen the issue, if appropriate.
  For example, you can leave a comment with additional information to help the maintainer debug it.
  Adding a comment will subscribe you to email notifications, which can be helpful in getting important updates regarding the issue.
  If you don't have anything to add but still want to receive email updates, you can click the "watch" button at the bottom of the comments.

- **Every issue must be of a single type.**
  Every issue must be exactly one of the following types: a bug report (`bug`), a feature request (`enhancement`), or a task (`task`).
  Do not file multi-typed issues.
  Instead, file multiple issues of distinct types.
  The Qubes team will classify your issue according to its type.

- **New issues should include all relevant information.**
  When you file a new issue, you should be sure to include the version of Qubes you're using, as well as versions of related software packages.
  If your issue is related to hardware, provide as many details as possible about the hardware, which could include using command-line tools such as `lspci`.
  If you're reporting a bug in a package that is in a [testing] repository, please reference the appropriate issue in the [updates-status] repository.
  Project maintainers really appreciate thorough explanations.
  It usually helps them address the problem more quickly, so everyone wins!

- **There are no guarantees that your issue will be addressed.**
  Keep in mind that `qubes-issues` is an issue tracker, not a support system.
  Creating a new issue is simply a way for you to submit an item for the Qubes team's consideration.
  It is up to the Qubes team to decide whether or how to address your issue, which may include closing the issue without taking any action on it.
  Even if your issue is kept open, however, you should not expect it to be addressed within any particular time frame, or at all.
  At the time of this writing, there are well over one thousand open issues in `qubes-issues`.
  The Qubes team has its own roadmap and priorities, which will govern the manner and order in which open issues are addressed.

If your issue is addressed, your GitHub issue may be closed.
After that, the package containing the fix will move to the appropriate [testing] repository, then to the appropriate stable repository.
If you so choose, you can test the fix while it's in the [testing] repository, or you can wait for it to land in the stable repository.
If, after testing the fix, you find that it does not really fix your bug, please leave a comment on your issue explaining the situation.
When you do, we will receive a notification and respond on your issue or reopen it (or both).
Please **do not** create a duplicate issue or attempt to contact the developers individually about your problem.


Mailing list guidelines
-----------------------

Please see the [Mailing Lists][support] page.


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
[mailing list guidelines]: #mailing-list-guidelines
[support]: /support/
[qubes-users]: /support/#qubes-users
[qubes-devel]: /support/#qubes-devel
[testing]: /doc/testing/
[updates-status]: https://github.com/QubesOS/updates-status/issues
[Copying from (and to) dom0]: /doc/copy-from-dom0/
[how to contribute code]: /doc/contributing/#contributing-code

