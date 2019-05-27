---
layout: doc
title: Testing New Releases and Updates
permalink: /doc/testing/
---

Testing New Releases and Updates
================================

Testing new Qubes OS releases and updates is one of the most helpful ways in which you can [contribute] to the Qubes OS Project.
However, you should only attempt to do this if you know what you're doing.
Never rely on code that is in testing for critical work!

Releases
--------
How to test upcoming Qubes OS releases:

 * Use [qubes-builder] to build the latest release.
 * Test the latest release candidate (RC), if any is currently available.

See [Version Scheme] for details about release versions and schedules.
See [Release Checklist] for details about the RC process.

Updates
-------
How to test updates:

 * Enable [dom0 testing repositories].
 * Enable [TemplateVM testing repositories].

Providing Feedback
------------------
If you're testing new releases or updates, we would be grateful for your feedback.

We use an [automated build process].
For every package that is uploaded to a testing repository, a GitHub issue is created in the [updates-status] repository for tracking purposes.
We welcome any kind of feedback on any package in any testing repository.
Even a simple <span class="fa fa-thumbs-up" title="Thumbs Up"></span> or <span class="fa fa-thumbs-down" title="Thumbs Down"></span> on the package's associated issue would help us to decide whether the package is ready to be migrated to a stable repository.
If you [report a bug] in a package that is in a testing repository, please reference the appropriate issue in [updates-status].

[contribute]: /doc/contributing/
[qubes-builder]: /doc/qubes-builder/
[Version Scheme]: /doc/version-scheme/
[Release Checklist]: /doc/releases/todo/
[dom0 testing repositories]: /doc/software-update-dom0/#testing-repositories
[TemplateVM testing repositories]: /doc/software-update-vm/#testing-repositories
[automated build process]: https://github.com/QubesOS/qubes-infrastructure/blob/master/README.md
[updates-status]: https://github.com/QubesOS/updates-status/issues
[report a bug]: /doc/reporting-bugs/

