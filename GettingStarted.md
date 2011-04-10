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

In Qubes you run all your programs in *domains*, also called *AppVMs*, because those domains are implemented as lightweight Virtual Machines (VMs). It's not true that every app runs in its own VM -- that would be a big waste of resources. Instead the VMs represent security domains, such as: *work*, *personal*, *banking*, *random browsing* (we call it *red*), etc.

If you have proceeded with the default installation options, Qubes has already pre-created 3 domains for you:

-   work
-   personal
-   red (for all the untrusted activity, such as random web browsing)

Each domain, apart form having a distinct name, is also assigned a **label**, which basically is one of the several per-defined colors. These colors, which are used for drawing window decorations by the trusted Window Manager (color frames), are supposed to be user friendly, easy noticeable, indicators of how trusted a given window is. It's totally up to the user how he or she interprets these colors. For me, it has been somehow obvious to associate the red color with something that is untrusted and dangerous (the “red light” -- stop! danger!), green with something that is safe and trusted, while yellow and orange with something in the middle. I have also extended this scheme, to also include blue, and black, which I interpret as indicating progressively more trusted domains than green, with black being something ultimately trusted.

There is, however, one special domain that is called *Dom0* which is where the Desktop Manager (currently KDE) runs, and this is where you log into. This domain doesn't have any networking connectivity and is essentially only dedicated for running the Window and Desktop Manager, nothing else.

Starting apps in domains
------------------------

TODO

Adding/Removing domains
-----------------------

TODO

How many domains do I need?
---------------------------

TODO
