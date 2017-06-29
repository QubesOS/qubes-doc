---
layout: doc
title: Package Contributions
permalink: /doc/package-contributions/
---

Package Contributions
=====================

**Notice:** *This is an unofficial draft. Once this information is official, this notice will be removed.*

Procedure
---------
If you would like to contribute a package to Qubes, please follow this procedure:

 1. Ensure that your package satisfies the [Inclusion Criteria].
 2. If your code isn't already on GitHub, create a GitHub repo that contains your code.
 3. If you haven't already, [sign your code][sig].
 4. Create an issue in [qubes-issues] with the title `[Contribution] your-package-name`.
    Include a link to your repo, a brief description of your package, and a brief explanation of why you think it should be included in Qubes.
 5. You may be asked followup questions.
    If we decide to accept your contribution, you will be invited to join the [QubesOS-contrib] organization on GitHub, and [QubesOS-contrib] will fork your repo.
    If we decide not to accept your contribution, we will state the reason and close the issue.

Inclusion Criteria
------------------
In order to be accepted, packages must:

 * In no way weaken the security of Qubes OS.
 * Be published under an open-source license.
 * Follow our [coding guidelines].
 * Be thoroughly tested.
 * Have a clearly defined use case for Qubes users.
 * Not be unduly burdensome to review.

(Please note that we always reserve the right add criteria to this list.)

Updates
-------
If you would like to update or patch an existing contributed package (i.e., code in a fork owned by [QubesOS-contrib]), whether it is your contribution or someone else's, please submit a [signed][sig], fast-forwardable pull request to that repo with your changes.
Please note that your pull request **must** be both [signed][sig] and fast-forwardable, or else it will be closed without further review.

[Inclusion Criteria]: #inclusion-criteria
[sig]: /doc/code-signing/
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues/
[QubesOS-contrib]: https://github.com/QubesOS-contrib
[coding guidelines]: /doc/coding-style/

