---
layout: doc
title: Upgrading the Whonix 14 TemplateVM to Whonix 15
permalink: /doc/whonix/whonix-upgrade-14-to-15/
---

Upgrading the Whonix 14 TemplateVM to Whonix 15
===============================================

This page provides instructions on upgrading the Whonix 14 [TemplateVM] to Whonix 15, along with updating the default Whonix [DispVM].

Detailed Instructions for Upgrading Whonix TemplateVMs with `qubesctl`
-----------------------------------------------------

These instructions will show you how to upgrade Whonix 14 to 15.

These instructions are taken from the [Whonix](https://whonix.org/wiki/) wiki, for more information, please read the entry about upgrading [Qubes-Whonix](https://whonix.org/wiki/Qubes/Install).

**Note:** The command-line prompt on each line indicates where each command should be entered (`@dom0`).

 1. Ensure the existing template(s) are not running.

For Whonix 14 Workstation
        [user@dom0 ~]$ qvm-shutdown whonix-ws-14

For Whonix 14 Gateway
	[user@dom0 ~]$ qvm-shutdown whonix-gw-14

 2. Upgrade the software in dom0.

        [user@dom0 ~]$ sudo qubes-dom0-update

 3. Change the Whonix version to download using your favorite editor.

        [user@dom0 ~]$ sudo nano /srv/formulas/base/virtual-machines-formula/qvm/whonix.jinja

 4. Make sure to save the file.

 5. Download the new Whonix templates, and set up the respective Qubes.

    The following command will set up `whonix-15-gw`, `whonix-15-ws`, `sys-whonix`, and `anon-whonix`.

    **Note:** This command will download the files and configure everything *without* giving any form of progress to the user.
    When this command is running, please be patient. Interrupting the command may cause an unstable system.
    The time it will take is a few minutes to twenty or more.
        sudo qubesctl state.sls qvm.anon-whonix

 Installing an upgraded Whonix 15 DispVM Template
 ---------------------------------------------------

To upgrade the default Whonix DVM template, run the following command.

        [user@dom0 ~]$ sudo qubesctl state.sls qvm.whonix-ws-dvm

[TemplateVM]: /doc/templates/
[DispVM]: /doc/dispvm/
