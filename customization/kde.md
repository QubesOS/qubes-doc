---
layout: doc
title: KDE
permalink: /doc/kde/
redirect_from: /en/doc/kde/
---

Using KDE in dom0
=================

Window Management
-----------------

You can set each window's position and size like this:

~~~
Right click title bar --> More actions --> Special window settings...

  Window matching tab
    Window class (application): Exact Match: <vm_name>
    Window title: Substring Match: <partial or full program name>

  Size & Position tab
    [x] Position: Apply Initially: x,y
    [x] Size: Apply Initially: x,y
~~~

You can also use `kstart` to control virtual desktop placement like this:

~~~
  kstart --desktop 3 --windowclass <vm_name> -q --tray -a <vm_name> '<run_program_command>'
~~~

(Replace "3" with whichever virtual desktop you want the window to be
on.)

This can be useful for creating a simple shell script which will set up your
workspace the way you like.


Mailing List Threads
--------------------

 * [Nalu's KDE customization thread](https://groups.google.com/d/topic/qubes-users/KhfzF19NG1s/discussion)
