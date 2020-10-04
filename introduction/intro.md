---
layout: default
title: Introduction
permalink: /intro/
redirect_from:
- /tour/
- /en/tour/
- /tour/#what-is-qubes-os
- /about/
- /en/about/
---

## What is Qubes OS?

Qubes OS is a free and open-source, security-oriented operating system for single-user desktop computing.
Qubes OS leverages [Xen-based virtualization](https://wiki.xen.org/wiki/Xen_Project_Software_Overview) to allow for the creation and management of isolated compartments called [qubes](/doc/glossary#qube).

These qubes, which are implemented as [virtual machines (VMs)](/doc/glossary#vm), have specific:

 - **Purposes:** with a predefined set of one or many isolated applications, for personal or professional projects, to manage the [network stack](/doc/networking/), [the firewall](/doc/firewall/), or to fulfill other user-defined purposes. 
 - **Natures:** [full-fledged](/doc/standalone-and-hvm/) or [stripped-down](/getting-started/) virtual machines based on popular operating systems, such as [Fedora](/doc/templates/fedora), [Debian](/doc/templates/debian), and [Windows](/doc/windows/).
 - **Levels of trust:** from complete to non-existent.
   All windows are displayed in a unified desktop environment with [unforgeable colored window borders](/getting-started/) so that different security levels are easily identifiable.

[![Qubes system diagram](/attachment/site/qubes-trust-level-architecture.png)](/attachment/site/qubes-trust-level-architecture.png)

## Features

 - **Strong isolation.**
   Isolate different pieces of software as if they were installed on separate physical machines using [PV](/doc/glossary/#pv) or [HVM](/doc/glossary/#hvm) virtualization techniques.
 - **Template system.**
   Use [AppVMs](/getting-started/) to share a root file system without sacrificing security using the innovative [Template system](/doc/templates/).
 - **Multiple operating systems.**
   Use multiple operating systems at the same time, including [Fedora](/doc/templates/fedora), [Debian](/doc/templates/debian), and [Windows](/doc/windows/).
 - **DisposableVMs.**
   Create [DisposableVMs](/doc/disposablevm/) on the fly that self-destruct when shut down.
 - **Whonix integration.**
   Run [Tor](https://www.torproject.org/) securely system-wide using [Whonix with Qubes](/doc/whonix/).
 - **Device isolation.**
   Secure [device handling](/doc/device-handling/) through isolation of network cards and USB controllers.
 - **Split GPG.**
   Utilize [Split GPG](/doc/split-gpg/) to keep your private keys safe.
 - **U2F proxy.**
   Operate [Qubes U2F proxy](/doc/u2f-proxy/) to use your two-factor authentication devices without exposing your web browser to the full USB stack.
 - **Open-source.**
   Users are free to use, copy, and modify Qubes OS and [are encouraged to do so](/doc/contributing/)!

## Why Qubes OS?

### Physical isolation is a given safeguard that the digital world lacks

Throughout our lives, we engage in various activities, such as going to school, working, voting, taking care of our families, and visiting with friends.
These activities are spatially and temporally bound: They happen in isolation from one another, in their own compartments, which often represent an essential safeguard, as in the case of voting.

In our digital lives, the situation is quite different: All of our activities typically happen on a single device.
This causes us to worry about whether it's safe to click on a link or install an app, since being hacked imperils our entire digital existence.

Qubes eliminates this concern by allowing us to divide a device into many compartments, much as we divide a physical building into many rooms.
Better yet, it allows us to create new compartments whenever we need them, and it gives us sophisticated tools for securely managing our activities and data across these compartments.

[![Qube Manager](/attachment/wiki/GettingStarted/r2b1-qubes-manager-2.png)](/attachment/wiki/GettingStarted/r2b1-qubes-manager-2.png)

### Qubes allows you to compartmentalize your digital life

Many of us are initially surprised to learn that our devices do not support the kind of secure compartmentalization that our lives demand, and we're disappointed that software vendors rely on generic defenses that repeatedly succumb to new attacks.

In building Qubes, our working assumption is that all software contains bugs.
Not only that, but in their stampeding rush to meet deadlines, the world's stressed-out software developers are pumping out new code at a staggering rate --- far faster than the comparatively smaller population of security experts could ever hope to analyze it for vulnerabilities, much less fix everything.
Rather than pretend that we can prevent these inevitable vulnerabilities from being exploited, we've designed Qubes under the assumption that they *will* be exploited.
It's only a matter of time until the next zero-day attack.

In light of this sobering reality, Qubes takes an eminently practical approach: confine, control, and contain the damage.
It allows you to keep valuable data separate from risky activities, preventing cross-contamination.
This means you you can do everything on the same physical computer without having to worry about a single successful cyberattack taking down your entire digital life in one fell swoop.
In fact, Qubes has [distinct advantages over physical air gaps](https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf).

[![Compartmentalization example](/attachment/site/qubes-partition-data-flows.jpg)](/attachment/site/qubes-partition-data-flows.jpg)

### Made to support vulnerable users and power users alike

Qubes provides practical, usable security to vulnerable and actively-targeted individuals, such as journalists, activists, whistleblowers, and researchers.
Qubes is designed with the understanding that people make mistakes, and it allows you to protect yourself from your own mistakes.
It's a place where you can click on links, open attachments, plug in devices, and install software free from worry.
It's a place where *you* have control over your software, not the other way around.

Qubes is also powerful.
Organizations like the [Freedom of the Press Foundation](/partners/#freedom-of-the-press-foundation), [Mullvad](/partners/#mullvad), and [Let's Encrypt](https://twitter.com/letsencrypt/status/1239934557710737410) rely on Qubes as they build and maintain critical privacy and security internet technologies that are in turn relied upon by countless users around the world every day.
Renowned security [experts](/experts/) like Edward Snowden, Daniel J. Bernstein, Micah Lee, Christopher Soghoian, Isis Agora Lovecruft, Peter Todd, Bill Budington, and Kenn White use and recommend Qubes.

Qubes is one of the few operating systems that places the security of its users above all else.
It is, and always will be, free and open-source software, because the fundamental operating system that constitutes the core infrastructure of our digital lives *must* be free and open-source in order to be trustworthy.

[![Qubes desktop screenshot](/attachment/wiki/GettingStarted/snapshot12.png)](/attachment/wiki/GettingStarted/snapshot12.png)

## More information

This page is just a brief introduction to what Qubes is all about, and many technical details have been omitted here for the sake of presentation.

 - Want to see Qubes OS in action?
   Sit back and watch a [video tour](/video-tours/)!
 - See what using Qubes actually looks like with these [screenshots](/screenshots/) of various applications running in Qubes.
 - Ready to get started with Qubes? [Here's what you need to know after installing.](/getting-started/)
 - If you're a current or potential Qubes user, you may want to check out the [documentation](/doc/), [user FAQ](/faq/#users), and [glossary](/doc/glossary/).
 - If you're a developer, there's dedicated [developer documentation](/doc/#developer-documentation) and a [developer FAQ](/faq/#developers) just for you.
 - Ready to give Qubes a try?
   Head on over to the [downloads](/downloads/) page, and read the [installation guide](/doc/installation-guide).
 - Need help, or just want to join the conversation?
   Learn more about [help, support, the mailing lists, and the forum](/support/).

