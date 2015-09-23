---
layout: doc
title: Introduction
permalink: /intro/
redirect_from:
- "/doc/SimpleIntro/"
- "/wiki/SimpleIntro/"
---

A Simple Introduction to Qubes
==============================

This is a short, non-technical introduction to Qubes intended for a popular audience. (If you just want to quickly gain a basic understanding of what Qubes is all about, you're in the right place!)

What is Qubes?
--------------

Qubes is a security-oriented operating system (OS). The OS is the software which runs all the other programs on a computer. Some examples of popular OSes are Microsoft Windows, Mac OS X, Android, and iOS. Qubes is free and open-source software (FOSS). This means that everyone is free to use, copy, and change the software in any way. It also means that the source code is openly available so others can contribute to and audit it.

Why is OS security important?
-----------------------------

Most people use an operating system like Windows or OS X on their desktop and laptop computers. These OSes are popular because they tend to be easy to use and usually come pre-installed on the computers people buy. However, they present problems when it comes to security. For example, you might open an innocent-looking email attachment or website, not realizing that you're actually allowing malware (malicious software) to run on your computer. Depending on what kind of malware it is, it might do anything from showing you unwanted advertisements to logging your keystrokes to taking over your entire computer. This could jeopardize all the information stored on or accessed by this computer, such as health records, confidential communications, or thoughts written in a private journal. Malware can also interfere with the activities you perform with your computer. For example, if you use your computer to conduct financial transactions, the malware might allow its creator to make fradulent transactions in your name.

Aren't antivirus programs and firewalls enough?
-----------------------------------------------

Unfortunately, conventional security approaches like antivirus programs and (software and/or hardware) firewalls are no longer enough to keep out sophisticated attackers. For example, nowadays it's common for malware creators to check to see if their malware is recognized by any popular antivirus programs. If it's recognized, they scramble their code until it's no longer recognizable by the antivirus programs, then send it out. The best antivirus programs will subsequently get updated once the antivirus programmers discover the new threat, but this usually occurs at least a few days after the new attacks start to appear in the wild. By then, it's typically too late for those who have already been compromised. In addition, bugs are inevitably discovered in the common software we all use (such as our web browsers), and no antivirus program or firewall can prevent all of these bugs from being exploited.

How does Qubes provide security?
--------------------------------

Qubes allows you to separate the various parts of your digital life into securely isolated virtual machines (VMs). A VM is basically a simulated computer with its own OS which runs as software on your physical computer. You can think of a VM as a *computer within a computer*. This allows you to have, for example, one VM for visiting untrusted websites and a different VM for doing online banking. This way, if your untrusted browsing VM get compromised by a malware-laden website, your online banking activities won't be at risk. Similarly, if you're concerned about risky email attachments, Qubes can make it so that every attachment gets opened in its own single-use, "disposable" VM.

In general, Qubes takes an approach called **security by isolation**, which in this context means keeping the things you do on your computer securely isolated in different VMs so that one VM getting compromised won't affect the others. This allows you to do everything on a single physical computer without having to worry about one successful cyberattack taking down your entire digital life in one fell swoop.

How does Qubes compare to using a "live CD" OS?
-----------------------------------------------

Booting your computer from a live CD (or DVD) when you need to perform sensitive activities can certainly be more secure than simply using your main OS, but this method still preserves many of the risks of conventional OSes. For example, popular live OSes (such as [Tails](https://tails.boum.org/) and other Linux distributions) are still **monolithic** in the sense that all software is still running in the same OS. This means, once again, that if your session is compromised, then all the data and activities performed within that same session are also potentially compromised.

How does Qubes compare to running VMs in a convential OS?
---------------------------------------------------------

Not all virtual machine software is equal when it comes to security. You may have used or heard of VMs in relation to software like VirtualBox or VMware Workstation. These are known as "Type 2" or "hosted" hypervisors. (The **hypervisor** is the software, firmare, or hardware that creates and runs virtual machines.) These programs are popular because they're designed primarily to be easy to use and run under popular OSes like Windows (which is called the **host** OS, since it "hosts" the VMs). However, the fact that Type 2 hypervisors run under the host OS means that they're really only as secure as the host OS itself. If the host OS is ever compromised, then any VMs it hosts are also effectively compromised.

By contrast, Qubes uses a "Type 1" or "bare metal" hypervisor called [Xen](http://www.xenproject.org). Instead of running inside an OS, Type 1 hypervisors run directly on the "bare metal" of the hardware. This means that an attacker must be capable of subverting the hypervisor itself in order to compromise the entire system, which is vastly more difficult.

Qubes makes it so that multiple VMs running under a Type 1 hypervisor can be securely used as an integrated OS. For example, it puts all of your application windows on the same desktop with special colored borders indicating the trust levels of their respective VMs. It also allows for things like secure copy/paste operations between VMs, securely copying and transferring files between VMs, and secure networking between VMs and the Internet.

How does Qubes compare to using a separate physical machine?
------------------------------------------------------------

Using a separate physical computer for sensitive activities can certainly be more secure than using one computer with a conventional OS for everything, but there are still risks to consider. Briefly, here are some of the main pros and cons of this approach relative to Qubes:

Pros:

-   Physical separation doesn't rely on a hypervisor. (It's very unlikely that an attacker will break out of Qubes' hypervisor, but if she were to manage to do so, she could potentially gain control over the entire system.)
-   Physical seaparation can be a natural complement to physical security. (For example, you might find it natural to lock your secure laptop in a safe when you take your unsecure laptop out with you.)

Cons:

-   Physical separation can be cumbersome and expensive, since we may have to obtain and set up a separate physical machine for each security level we need.
-   There's generally no secure way to transfer data between physically separate computers running conventional OSes. (Qubes has a secure inter-VM file transfer system to handle this.)
-   Physically separate computers running conventional OSes are still independently vulnerable to most conventional attacks due to their monolithic nature.
-   Malware which can bridge air gaps has existed for several years now and is becoming increasingly common.

(For more on this topic, please see the paper [Software compartmentalization vs. physical separation](http://www.invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf).)

More information
----------------

This page is just a brief sketch of what Qubes is all about, and many technical details have been omitted here for the sake of presentation.

-   If you're a current or potential Qubes user, you may want to check out the [documentation](/doc/UserDoc/) and the [FAQ](/doc/UserFaq/).
-   If you're a developer, there's dedicated [documentation](/doc/SystemDoc/) and an [FAQ](/doc/DevelFaq/) just for you.
-   Ready to give Qubes a try? Head on over to the [downloads page](/downloads/).
-   Once you've installed Qubes, here's a guide on [getting started](/doc/GettingStarted/).

