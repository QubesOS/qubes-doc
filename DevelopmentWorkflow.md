---
layout: wiki
title: DevelopmentWorkflow
permalink: /wiki/DevelopmentWorkflow/
---

Development Workflow
====================

A workflow for developing Qubes OS+

First things first, setup [Builder?](/wiki/Qubes). This guide assumes you're using qubes-builder to build Qubes.

Repositories and Committing Code
--------------------------------

Qubes is split into a bunch of git repos. This are all contained in the `qubes-src` directory under qubes-builder.

The best way to write and contribute code is to create a git repo somewhere (e.g., github) for the repo you are interested in editing (e.g., `qubes-manager`, `core`, etc). To integrate your repo with the rest of Qubes, cd to the repo directory and add your repository as a remote in git

**Example:**

``` {.wiki}
$ cd qubes-builder/qubes-src/qubesmanager
$ git remote add abel git@github.com:abeluck/qubes-core.git
```

You can then proceed to easily develop in your own branches, pull in new commits from the dev branches, merge them, and eventually push to your own repo on github.

When you are ready to submit your changes to Qubes to be merged, push your changes, then create a signed git tag (using `git tag -s`). Finally, send a letter to the Qubes listserv describing the changes and including the link to your repository. Don't forget to include your public PGP key you use to sign your tags.
