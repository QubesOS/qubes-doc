---
layout: doc
title: Debian
permalink: /doc/Templates/Debian/
redirect_from: /wiki/Templates/Debian/
---

Debian template
===============

Debian template is one of the templates made by Qubes community. It should be considered experimental as Qubes developers team use mainly Fedora-based VMs to test new features/updates.

Install
-------

It can be installed via the following command:

{% highlight trac-wiki %}
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-debian-8-x64
{% endhighlight %}

Known issues
------------

-   gnome-terminal by default is configured to black text on black background
-   GTK applications looks ugly (GTK theme not installed/set?)
-   Probably not working as netvm or proxyvm (untested as of today)
-   Slow VM shutdown - qrexec agent termination takes a while (SIGTERM not handled?)

If you want to help in improving the template, feel free to [contribute](/wiki/ContributingHowto).
