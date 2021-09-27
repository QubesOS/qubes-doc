---
lang: en
release: 4.0
reviewed: yes
layout: doc
permalink: /doc/continuous-integration/
title: Continuous integration (CI)
---

This page explains the [continuous integration
(CI)](https://en.wikipedia.org/wiki/Continuous_integration) infrastructure that
the Qubes OS Project uses.

## Website and documentation

The following commands may be useful as a way to interact with our CI
infrastructure on website
([qubesos.github.io](https://github.com/QubesOS/qubesos.github.io)) and
documentation ([qubes-doc](https://github.com/QubesOS/qubes-doc)) pull requests
(PRs). Note that special permissions may be required to use some of these
commands. These commands are generally issued by adding a comment to a PR
containing only the command.

- `PipelineRetry`: Attempts to run the entire build pipeline over again. This
  can be useful if CI incorrectly uses a stale branch instead of testing the PR
  as if it were merged into `master`.

- `PipelineRefresh`: Like `PipelineRetry`, except it only fetches the job status
   from GitLab. It doesn't schedule a new build.

- `TestDeploy`: Deploys a test website, which is a live version of the Qubes
  website as if this PR had been merged. This can be useful for previewing a PR
  on a live public website. **Note:** You must wait for the site to finish
  building before issuing this command, or else it will deploy an empty
  website. To find the URL of the test website, look for text similar to "This
  branch was successfully deployed" and a button named something like "View
  deployment." Note that there are two different testing sites: `wwwtest` is
  manually updated, whereas `wwwpreview` is managed by the `TestDeploy`
  command.
