---
layout: doc
title: KDE
permalink: /en/doc/kde/
---

KDE Tips
========

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
