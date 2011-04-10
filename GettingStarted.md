---
layout: wiki
title: GettingStarted
permalink: /wiki/GettingStarted/
---

Getting Started with Qubes OS
=============================

So, you just installed a fresh Qubes OS, huh? Let's see what your next steps could be...

What are AppVMs (domains)?
--------------------------

In Qubes you run all your programs in *domains*, also called *AppVMs*, because those domains are implemented as lightweight Virtual Machines (VMs). It's not true that every app runs in its own VM -- that would be a big waste of resources. Instead the VMs represent security domains, such as: *work*, *personal*, *banking*, *random browsing* (we call it *red*), etc. Each domain is based, by default, on the common Template VM, which means that whenever you create a new domain you don't copy all the files needed for this VM to work (such as all the programs, etc) -- you just share the root filesystem with the template VM (each VM has read-only access to the Template VM's files, so cannot modify them in any way). This means that creating many domains is cheap -- they need disk space only to hold your private files (home folder).

If you have proceeded with the default installation options, Qubes has already pre-created 3 domains for you:

-   work
-   personal
-   red (for all the untrusted activity, such as random web browsing)

Each domain, apart form having a distinct name, is also assigned a **label**, which basically is one of the several per-defined colors. These colors, which are used for drawing window decorations by the trusted Window Manager (color frames), are supposed to be user friendly, easy noticeable, indicators of how trusted a given window is. It's totally up to the user how he or she interprets these colors. For me, it has been somehow obvious to associate the red color with something that is untrusted and dangerous (the “red light” -- stop! danger!), green with something that is safe and trusted, while yellow and orange with something in the middle. I have also extended this scheme, to also include blue, and black, which I interpret as indicating progressively more trusted domains than green, with black being something ultimately trusted.

\<screenshot of a window with decoration\>

There is, however, one special domain that is called *Dom0* which is where the Desktop Manager (currently KDE) runs, and this is where you log into. This domain doesn't have any networking connectivity and is essentially only dedicated for running the Window and Desktop Manager, nothing else.

Starting apps in domains
------------------------

There are two way to start an app: using the short-cut icons from the Desktop Manager's menu, or from the command line (from console running in Dom).

You can start apps directly from the KDE menu. Each domain has its own menu directory called *Domain: \<name\>*, that is reachable via Start-\>Applications menu. When you enter into this directory, you can select a specific application that you would like to start:

\<screenshot of apps menu\>

Note that the menus contain only a few short-cuts, if you would like to be able to start more apps via menu (e.g. if you install new app), you would need to add more short-cuts manually. In order to do that you should righ-click on the "Start" button and choose "Menu Editor". Then choose the domain directory where you want the menu to appear, choose "New Item", enter its name as '\<domain name\>: \<app name\>' and provide command line for starting the app (see below). Then choose "Save" and wait some 15 sec for the changes to propagate to the KDE menu.

If you would like to start apps from the console, you just need to type:

``` {.wiki}
qvm-run -a <domain> "<app name> [arguments]"
```

e.g.:

``` {.wiki}
qvm-run -a red firefox
```

Adding/Removing domains
-----------------------

You can easily add/remove domains by clicking buttons in the Qubes Manager (you can find it in the tray -- it's the colourful icon with three little cubes: red, green and blue).

\<screenshot of creating a domain\>

You can also create/remove domains from command line (console under Dom0) using the following tools:

-   ```qvm-create```
-   ```qvm-remove```

The ```qvm-create``` is more powerful way of creating domains than the "Add" button in the manager, because it allows you to pass a few special options that allow to create special types of domains, such as **Standalone VM** (that is not based on a Template) or **NetVMs** or **ProxyVMs** -- you can read more on this in other chapters of this guide.

How many domains do I need?
---------------------------

So, how many and what domains do I need? That's a great question, but there is no good answer that would fit all. This all depends on how does your digital life look like, what type of job you do, etc.

For start it's reasonable to try the three domains created automatically by the installer (work, personal, red). Then, when you start feeling that some things/activities just don't fit, you can easily create a new domain for them. You will be able to easily copy files to the newly created domains, as it is covered in one of the [next chapters](/wiki/CopyingFiles) of this guide.

For more paranoid people, it might be worth checking [​this article](http://theinvisiblethings.blogspot.com/2011/03/partitioning-my-digital-life-into.html) that describes how one of the Qubes authors partitions her digital life into security domains.
