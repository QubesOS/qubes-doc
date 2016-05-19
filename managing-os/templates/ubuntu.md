---
layout: doc
title: Ubuntu Template
permalink: /doc/templates/ubuntu/
redirect_from:
- /en/doc/templates/ubuntu/
- /doc/Templates/Ubuntu/
- /wiki/Templates/Ubuntu/
---

Ubuntu template(s)
==================

If you like to use Ubuntu Linux distribution in your AppVMs, you can build and
install one of available Ubuntu templates. Those template currently are not
available in ready to use binary packages, because Canonical does not allow
to redistribute a modified Ubuntu. The redistribution is not allowed by their
[Intellectual property rights policy](http://www.ubuntu.com/legal/terms-and-policies/intellectual-property-policy).


Install
-------

It can built using [Qubes Builder](/doc/qubes-builder/). You can also access its
documentation in the [source code
repository](https://github.com/QubesOS/qubes-builder/blob/master/README.md).

To quickly prepare the builder configuration, you can use `setup` script
available in the repository - it will interactively ask you which templates you
want to build.

Known issues
------------
Building an Ubuntu 14.4 LTS template can be difficult ([see](https://groups.google.com/forum/#!topic/qubes-users/w0uZNr8nno8)).
A workaround is creating an ubuntu HVM A and use X over ssh from a second vm B ([see](https://groups.google.com/forum/#!topic/qubes-users/-wkG7E55PUI)). </br>
To do this you have to enable networking between A and B, or set B as netvm of A. 
If B supports copy and paste or seamless mode so does (indirectly) A. (you will be missing some features. e.g.: send file to vm A)</br>
Doing this reduces the security of A to the security of B!
This is no problem if B's only purpose is providing X over ssh only for vm A.

If you want to help in improving the template, feel free to
[contribute](/wiki/ContributingHowto).
