---
layout: doc
title: Live USB
permalink: /doc/live-usb/
---

Qubes Live USB (alpha)
======================

NOTE: This content applies to Qubes versions earlier than R3.2. See the
[Installation Guide](/doc/installation-guide/) for instructions and warnings
on creating a USB boot drive for testing purposes with Qubes R3.2, R4.0, and
higher.

Qubes Live USB allows you to run and try Qubes OS without having to install it
anywhere. Qubes Live USB is currently in alpha. If you use it, please consider
running the [HCL reporting tool](/hcl/) and sending us the results so that we
can continue to improve it. If  would like to contribute to the Qubes OS
Project by improving Qubes Live USB and integrating it with the installer,
please consider applying for a [Google Summer of Code][gsoc-page] scholarship
(if you are eligible) and choosing the QubesOS Project as a mentor
organization. You can find our list of project ideas [here][project-page].

Introduction
------------

When making this Live USB edition of Qubes OS, we faced several challenges which
traditional Linux distros don't have to bother with:

1. We needed to ensure Xen is properly started when booting the stick. In fact
   we still don't support UEFI boot for the stick for this reason, even though
   the Fedora liveusb creator we used does support it. Only legacy boot for this
   version, sorry.
2. We discovered that the Fedora liveusb-create does *not* verify signatures on
   downloaded packages. We have temporarily fixed that by creating a local repo,
   verifying the signatures manually (ok, with a script ;) ) and then building
   from there. Sigh.
3. We had to solve the problem of Qubes too easily triggering an Out Of Memory
   condition in Dom0 when running as Live OS.

This last problem has been a result of Qubes using the copy-on-write backing for
the VMs' root filesystems, which is used to implement our cool
[Template-based scheme](/doc/software-update-vm/). Normally these are backed by
regular files on disk. Even though these files are discardable upon VM reboots,
they must be preserved during the VM's life span, and they can easily grow to a
few tens of MBs per VM, sometimes even more. Also, each VM's private
image, which essentially holds just the user home directory, typically starts
with a few tens of MBs for an "empty VM". Now, while these represent rather
insignificant numbers on a disk-basked system, in the case of a live USB all
these files must be stored in RAM, which is a scarce resource on any OS, but
especially on Qubes.

We have implemented some quick optimizations in order to minimize the above
problem, but this is still far from a proper solution. We're planning to work
more on this next.

There are three directions in which we want to do further work on this Qubes
Live USB variant:

1. Introduce an easy, clickable "install to disk" option, merging this with the
   Qubes installation ISO. So, e.g. make it possible to first see if the given
   hardware is compatible with Qubes (by running the HCL reporting tool) and
   only then install on the main disk. Also, ensure UEFI boot works well.

2. Introduce options for persistence while still running this out of a USB
   stick. This would be achieved by allowing (select) VMs' private images to be
   stored on the r/w partition (or on another stick).

   A nice variant of this persistence option, especially for frequent
   travelers, would be to augment our backup tools so that it was
   possible to create a LiveUSB-hosted backups of select VMs. One could then
   pick a few of their VMs, necessary for a specific trip, back them up to a
   LiveUSB stick, and take this stick when traveling to a hostile country (not
   risking taking other, more sensitive ones for the travel). This should make
   life a bit simpler
   [for some](https://twitter.com/rootkovska/status/541980196849872896).

3. Introduce more useful preconfigured VMs setup, especially including
   Whonix/Tor VMs.


Current limitations
-------------------

(Remember that Qubes Live USB is currently in alpha, so please meter your
expectations accordingly.)

1. Currently just the 3 example VMs (untrusted, personal, work), plus the
   default net and firewall VMs are created automatically.
2. The user has an option to manually (i.e. via command line) create an
   additional partition, e.g. for storing GPG keyring, and then mounting it to
   select VMs. This is to add poor-man's persistence. We will be working on
   improving/automating that, of course.
3. Currently there is no "install to disk" option. We will be adding this
   in the future.
4. The amount of "disk" space is limited by the amount of RAM the laptop
   has. This has a side effect of e.g. not being able to restore (even a few) VMs
   from a large Qubes backup blob.
5. It's easy to generate Out Of Memory (OOM) in Dom0 by creating lots of VMs
   which are writing a lot into the VMs filesystem.
6. There is no DispVM savefile, so if you start a DispVM the savefile must be
   regenerated, which takes about 1-2 minutes.
7. UEFI boot doesn't work, and if you try booting Qubes Live USB via UEFI, Xen
   will not be started, rendering the whole experiment unusable.


Downloading and burning
-----------------------

1. Download the ISO (and its signature for verification) from the
   [downloads page](/downloads/#qubes-live-usb-alpha).
2. "Burn" (copy) the ISO onto a USB drive (replace `/dev/sdX` with your USB
   drive device):

        $ sudo dd if=Qubes-R3.0-rc2-x86_64-LIVE.iso of=/dev/sdX

   Note that you should specify the whole device, (e.g. `/dev/sdc`, not a single
   partition, e.g. `/dev/sdc1`).

   **Caution:** It is very easy to misuse the `dd` command. If you mix up `if`
   and `of` or specify an incorrect device, you could accidentally overwrite
   your primary system drive. Please be careful!

[project-page]: /gsoc/
[gsoc-page]: https://summerofcode.withgoogle.com/organizations/6239659689508864/
