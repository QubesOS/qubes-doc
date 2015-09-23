---
layout: doc
title: SourceCode
permalink: /doc/SourceCode/
redirect_from: /wiki/SourceCode/
---

Qubes Source Code Repositories
==============================

All the Qubes code is kept in GIT repositories. We divided the project into several components, each of which has its own separate repository, some of them:

-   `core-admin.git` -- the core Qubes infrastructure responsible for VM management, VM templates, fs sharing, etc.
-   `gui-daemon.git` -- GUI virtualization, Dom0 side.
-   `gui-agent-linux.git` -- GUI virtualization, Linux VM side.
-   `linux-template-builder.git` - scripts and other files used to create Qubes templates images.

You can browse the repositories [online on
GitHub](https://github.com/QubesOS/). The Qubes official repositories are on
this `QubesOS` github account.

To clone a repository:

```
git clone git://github.com/QubesOS/<repo_name>.git <repo_name>
```

e.g.:

```
git clone git://github.com/QubesOS/qubes-core-admin.git core-admin
```

## Sending a patch

If you want to contribute to the project, there are two ways:

*  **Preferred**: Use github [fork & pull requests](https://guides.github.com/activities/forking/)
*  Sending a patch via the project's mailing list (`git format-patch`).

    1.  Make all the changes in your working directory, i.e. edit files, move them around (you can use 'git mv' for this), etc.
    2.  Add the changes and commit them (git add, git commit). Never mix different changes into one commit! Write a good description of the commit. The first line should contain a short summary, and then, if you feel like more explanations are needed, enter an empty new line, and then start the long, detailed description (optional).
    3.  Test your changes NOW: check if RPMs build fine, etc.
    4.  Create the patch using 'git format-patch'. This has an advantage over 'git diff', because the former will also include your commit message, your name and email, so that \*your\* name will be used as a commit's author.
    5.  Send your patch to qubes-devel. Start the message subject with the '[PATCH]' string.
