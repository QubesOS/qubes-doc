---
layout: wiki
title: DispVMCustomization
permalink: /wiki/UserDoc/DispVMCustomization/
---

Customization of Disposable VM
==============================

It is possible to change application settings for each new DispVM. This can be done by customizin DispVM template:

1.  Start terminal in 'fedora-17-x64-dvm' VM (via command line, it is not listed in Qubes Manager nor system menu):

    ``` {.wiki}
    qvm-run -a fedora-17-x64-dvm gnome-terminal
    ```

2.  Change application settings (eg you can start firefox and change default search engine, install some plugins etc).
3.  Create empty /home/user/.qubes-dispvm-customized file:

    ``` {.wiki}
    touch /home/user/.qubes-dispvm-customized file
    ```

4.  Shutdown the VM (either by poweroff from VM terminal, or qvm-shutdown from dom0 terminal).
5.  Regenerate DispVM template:

    ``` {.wiki}
    qvm-create-default-dvm --default-template --default-script
    ```

**Note:** All above require at least qubes-core-vm \>= 2.1.2 installed in template.
