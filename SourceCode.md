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

{% highlight trac-wiki %}
git clone git://github.com/QubesOS/<repo_name>.git <repo_name>
{% endhighlight %}

e.g.:

{% highlight trac-wiki %}
git clone git://github.com/QubesOS/core-admin.git core-admin
{% endhighlight %}

If you want to contribute to the project, there are two preferred ways:
1. Use github [fork & pull requests](https://guides.github.com/activities/forking/)
2. [sending a patch](/wiki/DevelFaq#Q:HowdoIsubmitapatch) via the project's mailing list (`git format-patch`).
