---
layout: default
title: Get Started
permalink: /getting-started/
redirect_from:
- /doc/getting-started/
- /en/doc/getting-started/
- /doc/GettingStarted/
- /wiki/GettingStarted/
---

<a name="already-installed"></a>Now that you've installed Qubes, let's cover some basic concepts. 
You might also like to refer to the [Glossary](/doc/glossary/).

AppVMs (qubes) and TemplateVMs
--------------------------------

In Qubes, you run all your programs in lightweight Virtual Machines called **qubes**. 
Not every app runs in its own qube. 
(That would be a big waste of resources!) 
Instead, each qube represents a *security domain* (e.g., "work," "personal," "banking," etc.). 
By default all qubes are based on a single, common **TemplateVM** , although you can create more TemplateVMs if you wish. 
When you create a new qube, you don't copy the whole root filesystem needed for this qube to work (which would include copying all the programs). 
Instead, each qube *shares* the root filesystem with its respective TemplateVM. 
A qube has read-only access to the filesystem of the Template on which it's based, so a qube cannot modify a TemplateVM in any way. 
This is important, as it means that if a qube is ever compromised, the TemplateVM on which it's based (and any other qubes based on that TemplateVM) will still be safe. 
So creating a large number of domains is cheap: each one needs only as much disk space as is necessary to store its private files (e.g., the "home" folder).

If you've installed Qubes using the default options, a few qubes have already been created for you:

-   work
-   personal
-   untrusted

Each qube, apart from having a distinct name, is also assigned a **label**, which is one of several pre-defined colors. 
The trusted window manager uses these colors in order to draw window decorations (color frames) around the windows of applications running in each qube. 
It's totally up to you how you'd like to interpret these colors. 
You might like to use them to quickly and easily identify the trust level of a given window at a glance. 
Personally, I find it natural to associate red with that which is untrusted and dangerous (the “red light” -- stop! danger!), green with that which is safe and trusted, and yellow and orange with things in the middle. 
I've also extended this scheme to include blue and black, which I interpret as indicating progressively more trusted domains than green, with black being ultimately trusted.
Alternatively you might use the colors to show that qubes belong to the same domain - for example, you might use 3 or 4 qubes for work activities, and give them all the same distinct color label. It's entirely up to you.

![snapshot12.png](/attachment/wiki/GettingStarted/snapshot12.png)

In addition to qubes and TemplateVMs, there's one special domain called "dom0," which is where the Desktop Manager runs. 
This is where you log in to the system. 
Dom0 is more trusted than any other domain (including TemplateVMs and black-labeled qubes). 
If dom0 were ever compromised, it would be Game Over<sup>TM</sup>. 
(The entire system would effectively be compromised.) 
Due to its overarching importance, dom0 has no network connectivity and is used only for running the Window and Desktop Managers. 
Dom0 shouldn't be used for anything else. 
In particular, [you should never run user applications in dom0](/doc/security-guidelines/#dom0-precautions). 
(That's what your qubes are for!)

Qubes VM Manager and Command Line Tools
---------------------------------------

All aspects of the Qubes system can be controlled using command line tools run under a dom0 console. 
To open a console window in dom0, either go to Start-\>System Tools-\>Konsole or press Alt-F2 and type `konsole`.

Various command line tools are described as part of this guide, and the whole reference can be found [here](/doc/dom0-tools/).

![r2b1-dom0-konsole.png](/attachment/wiki/GettingStarted/r2b1-dom0-konsole.png)

Alternatively, you can use a rather intuitive GUI tool called **Qubes VM Manager**. 
It supports most of the functionality that command line tools provide. 
The Qubes VM Manager starts and opens automatically when Qubes starts up, but you can also start it by going to Start-\>System Tools-\>Qubes Manager. 
Once the Qubes VM Manager is running, you can open the window at any time by clicking on the Qubes tray icon, which typically resides in the bottom-right corner of the screen.

![r2b1-qubes-manager-2.png](/attachment/wiki/GettingStarted/r2b1-qubes-manager-2.png)

Starting Apps in qubes
------------------------

Apps can be started either by using the shortcuts in the Desktop Manager's menu or by using the command line (i.e., a console running in dom0).

You can start apps directly from the start menu. 
Each qube has its own menu directory under the scheme **Domain: \<name\>**. 
After navigating into one of these directories, simply click on the application you'd like to start:

![r2b1-appsmenu-1.png](/attachment/wiki/GettingStarted/r2b1-appsmenu-1.png) ![r2b1-appsmenu-3.png](/attachment/wiki/GettingStarted/r2b1-appsmenu-3.png)

By default, each qube's menu contains only a few shortcuts. 
If you'd like to add more, simply click **Add more shortcuts...**, select the desired applications, and click **OK**. 
You can also add shortcuts manually. 
(This is sometimes necessary if the desired application doesn't show up in the Qubes VM Manager window.) 
To do this in KDE, right-click on the **Start** button and click **Menu Editor**. 
Click the qube directory in which you'd like the menu to appear, click **New Item**, enter its name as **\<qube name\>: \<app name\>**, and provide the command for starting the app (see below). 
Then click **Save** and wait approximately 15 seconds for the changes to propagate to the KDE menu.

To start apps from the console in dom0, type:

    qvm-run -a <qube> "<app name> [arguments]"

e.g.:

    qvm-run -a untrusted firefox
    
The -a parameter will start the qube if it is not already running.

Adding, Removing, and Listing qubes
-------------------------------------

A qube can easily be added and removed by clicking on the **Add** and **Remove** buttons in the Qubes VM Manager.

A qube can also be added, removed, and qubes may be listed from the command line (i.e., a console running in dom0) using the following tools:

-   `qvm-create`
-   `qvm-remove`
-   `qvm-ls`

How Many Qubes Do I Need?
---------------------------

That's a great question, but there's no one-size-fits-all answer. 
It depends on the structure of your digital life, and this is at least a little different for everyone. 
If you plan on using your system for work, then it also depends on what kind of job you do.

It's a good idea to start out with the three qubes created automatically by the installer: work, personal, and untrusted. 
Then, if and when you start to feel that some activity just doesn't fit into any of your existing qubes, or you want to partition some part of your life, you can easily create a new qube for it. 
You'll also be able to easily copy any files you need to the newly created qube, as explained [here](/doc/copying-files/).

More paranoid people might find it worthwhile to read [this article](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html), which describes how one of the Qubes authors partitions her digital life into security domains.

Running an application Full Screen
----------------------------------

By default, Qubes doesn't allow any application window to occupy the entire screen such that its window name (which includes the name of the qube to which it belongs) and colored window border are no longer visible. 
This is a security precaution designed to prevent a situation in which an application which has been allowed to enter full screen mode begins to emulate the entire Qubes system. 
The user should always be able to identify which qube is displaying any given window. 
Otherwise, a compromised qube which is able to occupy the entire screen could trick the user into thinking that she is interacting with a variety of different qubes (including dom0), when in fact she is interacting with only a single, compromised qube pretending to be the whole system.

**Note:** A similar attack is possible even *without* fullscreen mode. 
Since a compromised qube can draw pixels within its own windows however it likes, it could draw a fake password prompt, for example, which appears to have a different colored border so that it looks like it belongs to a different qube. 
This is why you should always drag such prompts away from other windows (or use some other means of manipulating the windows) to ensure that they belong to the qube to which they appear to belong.

However, if the user makes use of an "expose-like" desktop switcher, such as the "Desktop Grid" effect that is enabled by default under KDE (default activation command: Ctrl-F8), then we can safely allow qubes to enter full screen mode, as we have assurance that we can always "preempt" them by hitting the magic key combination (e.g., Ctrl-F8), which will be consumed by the trusted window manager and not passed down to the fullscreen qube. 
This means that the qube has no way of effectively "faking" the fullscreen view of the system, as the user can easily identify it as "just another qube." 
Theoretically, this could be achieved even with primitive Alt-Tab like switching, which should be available on simpler Window Managers (such as Xfce4, which we also support as an alternative dom0 Desktop Environment), but this might be less obvious to the user.

To allow a qube to enter full screen mode, one should edit the `/etc/qubes/guid.conf` file in dom0.

To allow all qubes to enter full screen mode, set `allow_fullscreen` flag to `true` in the `global` section:

    global: {
      # default values
      allow_fullscreen = false;
      #allow_utf8_titles = false;
      #secure_copy_sequence = "Ctrl-Shift-c";
      #secure_paste_sequence = "Ctrl-Shift-v";
      #windows_count_limit = 500;
    };

To allow only select qubes to enter full screen mode, create a per-VM section, and set `allow_fullscreen` flag there to `true`:

    VM: {
      work: {
       allow_fullscreen = true;
      };

    };

In order for the changes to take effect, restart the qube(s).

More details can be found [here](/doc/full-screen-mode/).

<div class="row">
  <div class="col-lg-4 col-md-4">
    <h2>Compatible Hardware</h2>
    <p>Ready to install Qubes? Make sure your hardware is compatible, as Qubes cannot run on every type of computer. Also, check out <a href="/doc/certified-laptops/">Qubes-certified Laptops</a>.</p>
    <a href="/hcl/" class="btn btn-primary">
      <i class="fa fa-laptop"></i> Hardware Compatibility List
    </a>
  </div>
  <div class="col-lg-4 col-md-4">
    <h2>Downloads</h2>
    <p>Download an ISO, learn how to verify its authenticity and integrity, and follow our guides to install Qubes. Looking for the source code? You'll find it on <a href="https://github.com/QubesOS">GitHub</a>.</p>
    <a href="/downloads/" class="btn btn-primary">
      <i class="fa fa-download"></i> Downloads
    </a>
  </div>
  <div class="col-lg-4 col-md-4">
    <h2>Documentation</h2>
    <p>Peruse our extensive library of documentation for users and developers of Qubes. You can even help us <a href="/doc/doc-guidelines/">improve</a> it!</p>
    <a href="/doc/" class="btn btn-primary">
      <i class="fa fa-book"></i> Documentation
    </a>
  </div>
</div>
<hr class="more-top more-bottom">
