---
layout: doc
title: KdeDom0
permalink: /doc/KdeDom0/
redirect_from: /wiki/KdeDom0/
---

Qubes-customized KDE packages for Dom0
======================================

The Qubes kde-dom0 project (see [Source Code](/doc/SourceCode/)) contains the source code needed for building the customized KDE packages for use in Qubes Dom0 (the user desktop). The packages are based on Fedora 12 KDE packages, but are heavily slimmed down (Qubes doesn't need lots of KDE functionality in Dom0, such as most of the KDE apps). In the near future those KDE packages will also get some Qubes specific extensions, such as coloured titlebars/frames nicely integrated into the KDE Window Manager. And, of course, custom themes, e.g. for KDM :)

Getting the sources
-------------------

{% highlight trac-wiki %}
git clone git://qubes-os.org/mainstream/kde-dom0.git kde-dom0
{% endhighlight %}

Building the packages
---------------------

It's best to use Fedora 12 or 13 as a development system.

First, you should download and verify the original KDE sources (not part of the kde-dom0 repository):

{% highlight trac-wiki %}
make get-sources verify-sources
{% endhighlight %}

Now, check if you have all the required build dependencies:

{% highlight trac-wiki %}
make prep
{% endhighlight %}

Install any required packages that `make` might have complained about. Then you're ready to build the rpms (you might want to adjust the release of each rpm package by editing the `rel` variable at the beginning of each `.spec` file):

{% highlight trac-wiki %}
make rpms
{% endhighlight %}

**Note:** The `kdebase-*` packages build process requires corresponding `kdelibs-devel` package to be installed first. If your build system is based on Fedora 12/13, and if the `kdelibs-devel` package exist in Fedora repo that is based the same KDE software version (e.g. 4.4.3) as the KDE packages you're building (see the `version` file), than you should be able to use the Fedora package:

{% highlight trac-wiki %}
yum install kdelibs-devel-{version}
{% endhighlight %}

If not, then you should build your `kdelibs-devel` first (`cd kdelibs-devel && make rpms`), then install it on your build system, and then you can build all the rest (`make rpms`).

Installing KDE packages from Qubes repository
---------------------------------------------

TODO
