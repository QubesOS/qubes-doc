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

Every new update is first uploaded to the `security-testing` repository if it is a security update or `current-testing` if it is a normal update.
The update remains in `security-testing` or `current-testing` for a minimum of one week.
On occasion, an exception is made for a particularly critical security update, which is immediately pushed to the `current` stable repository.
In general, however, security updates remain in `security-testing` for two weeks before migrating to `current`.
Normal updates generally remain in `current-testing` until they have been sufficiently tested by the community, which can weeks or even months, depending on the amount of feedback received (see [Providing Feedback]).
"Sufficient testing" is, in practice, a fluid term that is up the developers' judgment. In general, it means either that no negative feedback and at least one piece of positive feedback has been received or that the package has been in `current-testing` for long enough, depending on the component and the complexity of the changes.

A limitation of the current testing setup is that it is only possible to migrate the *most recent version* of a package from `current-testing` to `current`.
This means that, if a newer version of a package is uploaded to `current-testing`, it will no longer be possible to migrate any older versions of that same package from `current-testing` to `current`, even if one of those older versions has been deemed stable enough.
While this limitation can be inconvenient, the benefits outweigh the costs, since it greatly simplifies the testing and reporting process.

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
[Providing Feedback]: #providing-feedback

