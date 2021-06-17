---
lang: en
layout: doc
permalink: /doc/how-to-get-started/
redirect_from:
- /doc/getting-started/
- /getting-started/
- /en/doc/getting-started/
- /doc/GettingStarted/
- /wiki/GettingStarted/
ref: 190
title: How to Get Started
---

After [downloading](/downloads/) and [installing](/doc/installation-guide/) Qubes OS, let's cover some basic concepts.

Introduction
------------

In Qubes OS, you run all your programs in lightweight [virtual machines (VMs)](/doc/glossary/#vm) called [qubes](/doc/glossary/#qube).
Not every app runs in its own qube.
(That would be a big waste of resources!)
Instead, each qube represents a [security domain](/doc/glossary/#domain) (e.g., "work," "personal," and "banking").
By default, all qubes are based on a single, common [template](/doc/glossary/#templatevm), although you can create more templates if you wish.
When you create a new qube, you don't copy the whole system needed for this qube to work (which would include copying all the programs).
Instead, each qube *shares* the system with its respective template.
A qube has read-only access to the system of the template on which it's based, so a qube cannot modify a template in any way.
This is important, as it means that if a qube is ever compromised, the template on which it's based (and any other qubes based on that template) will still be safe.
So, creating a large number of qubes is cheap: each one needs only as much disk space as is necessary to store its private files (e.g., the "home" folder).

If you've installed Qubes OS using the default options, a few qubes have already been created for you:

- work
- personal
- untrusted
- vault

Each qube, apart from having a distinct name, is also assigned a **label**, which is one of several predefined colors.
The trusted window manager uses these colors in order to draw colored borders around the windows of applications running in each qube.
This is designed to allow you to quickly and easily identify the trust level of a given window at a glance.
Most Qubes OS users associate red with what's untrusted and dangerous (like a red light -- stop! danger!), green with what's safe and trusted, and yellow and orange with things in the middle.
This color scheme also extends to include blue and black, which are usually interpreted as indicating progressively more trusted domains than green, with black being ultimately trusted.
However, it's totally up to you how you'd like to interpret these colors.
Qubes OS doesn't assume anything about these colors.
When you make a new qube, the system doesn't do anything special to it depending on whether it's black or red, for example.
The only difference is which color you see and the meaning you assign to that color in your mind.
For example, you could use the colors to show that qubes belong to the same domain.
You might use three or four qubes for work activities and give them all the same distinct color label, for instance.
It's entirely up to you.

![snapshot_40.png](/attachment/wiki/GettingStarted/r4.0-snapshot_40.png)

In addition to qubes and templates, there's one special domain called [dom0](/doc/glossary/#dom0), where many system tools and the desktop manager run.
This is where you log in to the system.
Dom0 is more trusted than any other domain (including templates and black-labeled qubes).
If dom0 were ever compromised, it would be "game over."
(The entire system would effectively be compromised.)
Due to its overarching importance, dom0 has no network connectivity and is used only for running the window and desktop managers.
Dom0 shouldn't be used for anything else.
In particular, [you should never run user applications in dom0](https://github.com/Qubes-Community/Contents/blob/master/docs/security/security-guidelines.md#dom0-precautions).
(That's what your qubes are for!)

GUI and command-line tools
--------------------------

All aspects of Qubes OS can be controlled using command-line tools run in a dom0 terminal.
Opening a terminal in dom0 can be done in several ways:

- Go to the Application Launcher and click **Terminal Emulator**.
- Press `Alt+F3`, type `xfce terminal` and press Enter twice.
- Right-click on the desktop and select **Open Terminal Here**.

Various command-line tools are described as part of this guide, and the whole reference can be found [here](/doc/tools/).

Alternatively, you can use a suite of GUI tools, most of which are available through desktop widgets:

- The **Domains Widget** allows you to manage running qubes, turn them on and off, and monitor memory usage.
- The **Devices Widget** allows you to attach and detach devices -- such as USB drives and cameras -- to qubes.
- The **Disk Space Widget** will notify you if you're ever running out of disk space.
- The **Updates Widget** will inform you when template updates are available.

![q40_widgets.png](/attachment/wiki/GettingStarted/r4.0-q40_widgets.png)

For an overview of the entire system, you can use the **Qube Manager** (go to the Application Launcher → System Tools → Qube Manager), which displays the states of all the qubes in your system.

Starting apps
-------------

Apps can be started either by using the shortcuts in the Application Launcher menu or by using the command line (i.e., a terminal running in dom0).

You can start apps directly from the Application Launcher or the Application Finder (`Alt+F3`).
Each qube has its own menu directory under the scheme `Domain: <name>`.
After navigating into one of these directories, simply click on the application you'd like to start:

![menu1.png](/attachment/wiki/GettingStarted/r4.0-menu1.png)

![menu2.png](/attachment/wiki/GettingStarted/r4.0-menu2.png)

By default, each qube's menu contains only a few shortcuts.
If you'd like to add more, enter the qube's **Qube Settings** and add them on the Applications tab.

To start apps from the terminal in dom0, type:

```shell_session
$ qvm-run <qube_name> <app_command> [arguments]
```

e.g.:

```shell_session
$ qvm-run untrusted firefox
```

This command will start the qube if it is not already running.

Adding, removing, and listing qubes
-----------------------------------

You can easily create a new qube with the **Create Qubes VM** option in the Application Launcher.
If you need to add or remove qubes, simply use the Qube Manager's **Add** and **Remove** buttons.

You can also add, remove, and list qubes from the command line using the following tools:

- `qvm-create`
- `qvm-remove`
- `qvm-ls`

How many qubes do I need?
-------------------------

That's a great question, but there's no one-size-fits-all answer.
It depends on the structure of your digital life, and this is at least a little different for everyone.
If you plan on using your system for work, then it also depends on what kind of job you do.

It's a good idea to start out with the three qubes created automatically by the installer: work, personal, and untrusted.
If and when you start to feel that some activity just doesn't fit into any of your existing qubes, or you want to partition some part of your life, you can easily create a new qube for it.
You'll also be able to easily [copy](/doc/how-to-copy-and-move-files/) any files you need to the newly created qube.

Still not sure?
You might find it helpful to read [this article](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html), which describes how one of the Qubes OS architects partitions her digital life into security domains.

Important tasks
---------------

It's very important to [keep Qubes updated](/doc/updating-qubes-os/) to ensure you have the latest security updates.
Frequently updating is one of the best ways to remain secure against new threats.

It's also very important to make regular backups so that you don't lose your data unexpectedly.
The [Qubes backup system](/doc/backup-restore/) allows you to do this securely and easily.

Here are some other tasks you're likely to want to perform.
(A full list is available in the [How-to Guides](/doc/#how-to-guides) section of the documentation.)

- [Copying and Pasting Text Between Domains](/doc/how-to-copy-and-paste-text/)
- [Copying and Moving Files Between Domains](/doc/how-to-copy-and-move-files/)
- [Copying from (and to) dom0](/doc/how-to-copy-from-dom0/)
- [Fullscreen Mode](/doc/full-screen-mode/)
- [DisposableVMs](/doc/disposablevm/)
- [Device Handling](/doc/how-to-use-devices/) (block, USB, and PCI devices)

If you encounter any problems, please visit the [Help, Support, and Mailing Lists](/support/) page.


<hr class="more-top more-bottom">
<div class="row">
  <div class="col-lg-4 col-md-4 more-bottom">
    <h2>Compatible Hardware</h2>
    <p>Make sure your hardware is compatible, as Qubes OS cannot run on every type of computer. Also, check out <a href="/doc/certified-laptops/">Qubes-certified Laptops</a>.</p>
    <a href="/hcl/" class="btn btn-primary">
      <i class="fa fa-laptop"></i> Hardware Compatibility List
    </a>
  </div>
  <div class="col-lg-4 col-md-4 more-bottom">
    <h2>Downloads</h2>
    <p>Download an ISO, learn how to verify its authenticity and integrity, and follow our guides to install Qubes OS. Looking for the source code? You'll find it on <a href="https://github.com/QubesOS">GitHub</a>.</p>
    <a href="/downloads/" class="btn btn-primary">
      <i class="fa fa-download"></i> Downloads
    </a>
  </div>
  <div class="col-lg-4 col-md-4">
    <h2>Documentation</h2>
    <p>Peruse our extensive library of documentation for users and developers of Qubes OS. You can even help us <a href="/doc/doc-guidelines/">improve</a> it!</p>
    <a href="/doc/" class="btn btn-primary">
      <i class="fa fa-book"></i> Documentation
    </a>
  </div>
</div>
