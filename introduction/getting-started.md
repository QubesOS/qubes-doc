---
lang: en
layout: doc
permalink: /doc/getting-started/
redirect_from:
- /doc/how-to-get-started/
- /getting-started/
- /en/doc/getting-started/
- /doc/GettingStarted/
- /wiki/GettingStarted/
ref: 190
title: Getting started
---

After [downloading](/downloads/) and [installing](/doc/installation-guide/)
Qubes OS, it's time to dive in and get to work! (Already know your way around?
Dive right in to [organizing your qubes](/doc/how-to-organize-your-qubes/).)

## The Basics

Qubes OS is an operating system built out of securely-isolated compartments
called [qubes](/doc/glossary/#qube). For example, you might have a work qube, a
personal qube, a banking qube, a web browsing qube, and so on. You can have as
many qubes as you want! Most of the time, you'll be using an [app
qube](/doc/glossary/#app-qube), which is a qube intended for running software
programs like web browsers, email clients, and word processors. Each app qube
is based on another type of qube called a [template](/doc/glossary/#template).
More than one qube can be based on the same template. Importantly, a qube
cannot modify its template in any way. This means that, if a qube is ever
compromised, its template and any other qubes based on that template will
remain safe. This is what makes Qubes OS so secure. Even if an attack is
successful, the damage is limited to a single qube.

Suppose you want to use your favorite web browser in several different qubes.
You'd install the web browser in a template, then every qube based on that
template would be able to run the web browser software (while still being
forbidden from modifying the template and any other qubes). This way, you only
have to install the web browser a single time, and updating the template serves
to update all the qubes based on it. This elegant design saves time and space
while enhancing security.

There are also some "helper" qubes in your system. Each qube that connects to
the Internet does so through a network-providing [service
qube](/doc/glossary/#service-qube). If you need to access USB devices, another
service qube will do that. There's also a [management
qube](/doc/glossary/#management-qube) that automatically handles a lot of
background housekeeping. For the most part, you won't have to worry about it,
but it's nice to know that it's there. As with app qubes, service qubes and
management qubes are also based on templates. Templates are usually named after
their operating system (often a [Linux
distribution](https://en.wikipedia.org/wiki/Linux_distribution)) and
corresponding version number. There are many ready-to-use
[templates](/doc/templates) to choose from, and you can download and have as
many as you like.

Last but not least, there's a very special [admin
qube](/doc/glossary/#admin-qube) which, as the name suggests, is used to
administer your entire system. There's only one admin qube, and it's called
[dom0](/doc/glossary/#dom0). You can think of it as the master qube, holding
ultimate power over everything that happens in Qubes OS. Dom0 is more trusted
than any other qube. If dom0 were ever compromised, it would be "game over."
The entire system would effectively be compromised. That's why everything in
Qubes OS is specifically designed to protect dom0 and ensure that doesn't
happen. Due to its overarching importance, dom0 has no network connectivity and
is used only for running the [desktop
environment](https://en.wikipedia.org/wiki/Desktop_environment) and [window
manager](https://en.wikipedia.org/wiki/Window_manager). Dom0 should never be
used for anything else. In particular, you should never run user applications
in dom0. (That's what your app qubes are for!)

### Color & Security

You'll choose a **color** for each of your qubes out of a predefined set of
colors. Each window on your desktop will have its frame colored according to
the color of that qube. These colored frames help you keep track of which qube
each window belongs to and how trustworthy it is. This is especially helpful
when you have the same app running in multiple qubes at the same time. For
example, if you're logged in to your bank account in one qube while doing some
random web surfing in a different qube, you wouldn't want to accidentally enter
your banking password in the latter! The colored frames help to avoid such
mistakes.

[![snapshot_40.png](/attachment/doc/r4.0-snapshot_40.png)](/attachment/doc/r4.0-snapshot_40.png)

Most Qubes users associate red with what's untrusted and dangerous (like a red
light: stop! danger!), green with what's safe and trusted, and yellow and
orange with things in the middle. This color scheme also extends to include
blue and black, which are usually interpreted as indicating progressively more
trusted domains than green, with black being ultimately trusted. Color and
associated meanings are ultimately up to you, however. The system itself does
not treat the colors differently. If you create two identical qubes --- black
and red, say --- they'll be the same until you start using them differently.
Feel free to use the colors in whatever way is most useful to you. For example,
you might decide to use three or four qubes for work activities and give them
all the same color --- or all different colors. It's entirely up to you.

### User Interface

On operating systems like Windows and macOS, the desktop environment is
unchangeable and part of that operating system. With Linux, any of a number of
desktop environments are an option. Qubes OS is installed with XFCE as its
default desktop environment, but it also supports [KDE](/doc/kde/), as well as
the window managers [i3](/doc/i3/) and [AwesomeWM](/doc/awesomewm/).

[![r4.0-taskbar.png](/attachment/doc/r4.0-taskbar.png)](/attachment/doc/r4.0-taskbar.png)

The bar at the top of your screen in Qubes 4.0 includes the following XFCE
component areas:

- The **Tray**, where many functional widgets live.
- **Spaces**, an interface for [virtual
  desktops](https://en.wikipedia.org/wiki/Virtual_desktop). Virtual desktops do
  not have any inherent security isolation properties, but some users find them
  useful for organizing things.
- The **Task Bar** where buttons for open and hidden windows live.
- The **App Menu**, where you go to open an application within a qube, to open
  a dom0 terminal, to access administrative UI tools such as the Qube Manager,
  or to access settings panels for your desktop environment.

To learn more about how to customize your desktop environment, we recommend you
spend some time going through [XFCE's documentation](https://docs.xfce.org/).

There are several tray widgets that are unique to Qubes OS:

- The **Whonix SDWDate** allows you to control the Tor connection in your
  [`sys-whonix`](https://www.whonix.org/wiki/Qubes) qube.
- The **Qubes Clipboard** lets you easily copy text from dom0.
- The **Qubes Devices** widget allows you to attach and detach devices --- such
  as USB drives and cameras --- to qubes. 
- The **Qubes Disk Space** widget shows you how much storage you're using.
  It'll notify you if you're ever running out of space.
- The **Qubes Domains** widget allows you to manage running qubes, turn them on
  and off, and monitor RAM and CPU usage.
- The **Qubes Updater** widget informs you when updates are available and helps
  you install them.

[![r4.1-widgets.png](/attachment/doc/r4.1-widgets.png)](/attachment/doc/r4.1-widgets.png)

#### Qube Manager

To see all of your qubes at the same time, you can use the **Qube Manager** (go
to the App Menu → Qubes Tools → Qube Manager), which displays the states of
all the qubes in your system, even the ones that aren't running.

[![r4.0-qubes-manager.png](/attachment/doc/r4.0-qubes-manager.png)](/attachment/doc/r4.0-qubes-manager.png)

#### Command-line interface

All aspects of Qubes OS can be controlled using command-line tools. Opening a
terminal emulator in dom0 can be done in several ways:

- Go to the App Menu and select **Terminal Emulator** at the top.
- Press `Alt`+`F3` and search for `xfce terminal`.
- Right-click on the desktop and select **Open Terminal Here**.

Terminal emulators can also be run in other qubes as normal programs. Various
command-line tools are described as part of this guide, and the whole reference
can be found [here](/doc/tools/).

## First boot

When you install Qubes OS, a number of qubes are pre-configured for you:

- **Templates:** `fedora-XX` (`XX` being the version number)
- **Admin qube:** `dom0`
- **Service qubes:** `sys-usb`, `sys-net`, `sys-firewall`, and `sys-whonix`
- **App qubes** configured to prioritize security by compartmentalizing tasks
  and types of data: `work`, `personal`, `untrusted`, and `vault`. (There is
  nothing special about these qubes. If you were to create a black qube and
  name it `vault`, it would be the same as the pre-configured `vault` qube.
  They're just suggestions to get you started. )

A variety of open-source applications such as file managers, command-line
terminals, printer managers, text editors, and "applets" used to configure
different things like audio or parts of the user interface are also installed
by default—most within the templates. Most are bundled with each template.

### Adding, removing, and listing qubes

You can easily create a new qube with the **Create Qubes VM** option in the App
Menu. If you need to add or remove qubes, simply use the Qube Manager's **Add**
and **Remove** buttons. You can also add, remove, and list qubes from the
command line using the following tools:

- `qvm-create`
- `qvm-remove`
- `qvm-ls`

### How many qubes do I need?

That's a great question, but there's no one-size-fits-all answer. It depends on
the structure of your digital life, and this is at least a little different for
everyone. If you plan on using your system for work, then it also depends on
what kind of job you do.

It's a good idea to start out with the qubes created automatically by the
installer: `work`, `personal`, `untrusted`, and `vault`. If and when you start
to feel that some activity just doesn't fit into any of your existing qubes, or
you want to partition some part of your life, you can easily create a new qube
for it. You'll also be able to easily [copy any
files](/doc/how-to-copy-and-move-files) you need to the newly-created qube.

Want to see some examples? Check out our in-depth guide on [how to organize your
qubes](/doc/how-to-organize-your-qubes/), which walks through several common use
cases based on our user research and years of experience from veteran Qubes
users.

## Secure Habits

It is *very important* to [keep Qubes updated](/doc/how-to-update/) to ensure
you have the latest security updates. Frequently updating is one of the best
ways to remain secure against new threats.

It's also *very important* to make regular backups so that you don't lose your
data unexpectedly. The [Qubes backup
system](/doc/how-to-back-up-restore-and-migrate/) allows you to do this
securely and easily.

## How-To Guides

Here are some basic tasks you're likely to want to perform often that are
unique to Qubes as a multi-environment system. A full list is available in the
[How-To Guides](/doc/#how-to-guides) section in the docs.

- [How to organize your qubes](/doc/how-to-organize-your-qubes/)
- [How to Update](/doc/how-to-update/)
- [How to Back Up, Restore, and Migrate](/doc/how-to-back-up-restore-and-migrate/)
- [How to Copy and Paste Text](/doc/how-to-copy-and-paste-text/)
- [How to Copy and Move Files](/doc/how-to-copy-and-move-files/)
- [How to Copy from Dom0](/doc/how-to-copy-from-dom0/)
- [How to Install Software](/doc/how-to-install-software/)
- [How to Use Devices (block storage, USB, and PCI devices)](/doc/how-to-use-devices/)

If you encounter any problems, please visit the [Help, Support, Mailing Lists,
and Forum](/support/) page.

## Compatible Hardware

Make sure your hardware satisfies the [system
requirements](/doc/system-requirements/), as Qubes OS cannot run on every type
of computer. You may also want to check out [Qubes-certified
Hardware](/doc/certified-hardware/) and take a look at the [Hardware
Compatibility List (HCL)](/hcl/).

## Downloads

[Download an ISO](/downloads/), learn how to [verify its
authenticity](/doc/verifying-signatures/), and follow our [guide to install
Qubes OS](/doc/installation-guide/). Looking for the [source
code](/doc/source-code/)? You'll find it [on
GitHub](https://github.com/QubesOS).

## Documentation

Peruse our extensive library of [documentation](/doc/) for users and developers
of Qubes OS. You can even [help us improve it](/doc/how-to-edit-the-documentation/)!
