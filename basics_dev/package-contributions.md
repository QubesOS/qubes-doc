---
layout: doc
title: Package Contributions
permalink: /doc/package-contributions/
---

Package Contributions
=====================

We're very grateful to the talented and hard-working community members who contribute software packages to Qubes OS.
This page explains the inclusion criteria and procedures for such packages, as well as the roles and responsibilities of those involved.

Inclusion Criteria
------------------
In order to be accepted, packages must:

 * In no way weaken the security of Qubes OS.
 * Be published under an open-source license (read about the [Qubes OS License]).
 * Follow our [coding guidelines].
 * Be thoroughly tested.
 * Have a clearly-defined use case for Qubes users.
 * Not be unduly burdensome to review.

(Please note that we always reserve the right to add criteria to this list.)

Contribution Procedure
----------------------
Before you start putting serious work into a package, we recommend that you discuss your idea with the Qubes developers and the broader community on the [qubes-devel mailing list].
Once you have a package that's ready to become part of Qubes OS, please follow this procedure:

 1. Ensure that your package satisfies the [Inclusion Criteria].
 2. If your code isn't already on GitHub, create a GitHub repo that contains your code.
 3. If you haven't already, [sign your code][sig].
 4. Create an issue in [qubes-issues] with the title `[Contribution] your-package-name`.
    Include a link to your repo, a brief description of your package, and a brief explanation of why you think it should be included in Qubes.
    Please note that the Qubes core developers are very busy.
    If they are under heavy load when you submit your contribution, it may be a very long time before they have time to review your package.
    If this happens, please do not be discouraged.
    If you think they may have forgotten about your pending contribution, you may "bump" your request by commenting on your issue, but please do this *very* sparingly (i.e., no more than once a month).
    We appreciate your understanding!
 5. You may be asked followup questions.
    If we decide to accept your contribution, you will be invited to join the [QubesOS-contrib] organization on GitHub as public recognition of your contribution (but without push access; see [Review Procedure]), and [QubesOS-contrib] will fork your repo.
    If we decide not to accept your contribution, we will state the reason and close the issue.

Update Procedure
----------------
*Anyone* can provide an update (patch) to a contributed package, not just the person who contributed that package!
The update procedure is the same for everyone, including the original package contributor.

If you would like to update an already-contributed package (specifically, a fork owned by [QubesOS-contrib]), please submit a [signed][sig], fast-forwardable pull request to that repo with your changes.
Please note that your pull request **must** be both [signed][sig] and fast-forwardable, or else it will be closed without further review.
One or more reviewers may post comments on your pull request.
Please be prepared to read and respond to these comments.

Review Procedure
----------------
This review procedure covers both original package contributions (see [Contribution Procedure]) and all subsequent updates to those packages, including updates from the original package contributor (see [Update Procedure]).
All changes will be reviewed by a Qubes Core Reviewer (QCR) and the [Package Maintainer] (PM).
In all cases, the QCR will be a core Qubes developer.
In some cases, the QCR and the PM will be the same person.
For example, if someone contributes a package, then disappears, and no suitable replacement has been found, then it is likely that a core Qubes developer will play both the QCR and PM roles for that package, at least until another suitable candidate volunteers to become the PM for that package.

The review procedure is as follows:

 1. Someone, S, wishes to make a change to a package, P.
 2. S submits a fast-forwardable pull request against the fork of P's repo owned by [QubesOS-contrib].
 3. The PM reviews the pull request.
    If the the pull request passes the PM's review, the PM adds a [signed][sig] *comment* on the pull request stating that it has passed review.
    (In cases in which S = PM, the PM can simply add a [signed][sig] *tag* to the HEAD commit prior to submitting the pull request.)
    If the pull request does not pass the PM's review, the PM leaves a comment on the pull request explaining why not.
 4. The QCR reviews the pull request.
    If the pull request passes the QCR's review, the QCR pushes a [signed][sig] tag to the HEAD commit stating that it has passed review and fast-forward merges the pull request.
    If the pull request does not pass the QCR's review, the QCR leaves a comment on the pull request explaining why not, and the QCR may decide to close the pull request.

Package Maintainers
-------------------
If you contribute a package, we assume that you will be the maintainer of that package, unless you tell us otherwise.
As the maintainer of the package, it is your privilege and responsibility to:

 * [Review][Review Procedure] each pull request made against the package.
 * Decide when the package has reached a new version, and notify the Qubes core developers when this occurs.

If you do not wish to be the maintainer of your package, please let us know.
If you do not act on your maintainer duties for a given package for an extended period of time and after at least one reminder, we will assume that you no longer wish to be the maintainer for that package.


[Inclusion Criteria]: #inclusion-criteria
[Contribution Procedure]: #contribution-procedure
[Update Procedure]: #update-procedure
[Review Procedure]: #review-procedure
[Package Maintainer]: #package-maintainers
[Qubes OS License]: /doc/license/
[sig]: /doc/code-signing/
[coding guidelines]: /doc/coding-style/
[qubes-devel mailing list]: /support/#qubes-devel
[QubesOS-contrib]: https://github.com/QubesOS-contrib
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues/

