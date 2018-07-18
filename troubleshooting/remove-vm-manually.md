---
layout: doc
title: How to Remove VMs Manually
permalink: /doc/remove-vm-manually/
---

How to Remove VMs Manually
==========================

How to Remove a TemplateVM Manually 
------------------------------------------

Try the [normal method] before resorting to these.
All of the following commands should be executed in a dom0 terminal.

### R3.2

1. Remove the TemplateVM's directory:

       $ rm -rf /var/lib/qubes/vm-templates/<template-name>

2. Remove the TemplateVM from qubes.xml:

       $ qvm-remove --just-db <template-name>

3. Remove the TemplateVM's `*.desktop` files from `~/.local/share/applications`:

       $ rm ~/.local/share/applications/<template-name>*

4. Remove the TemplateVM's Applications Menu entry:
        
       $ sudo rm /etc/xdg/menus/applications-merged/<template-name>*


[normal method]: /doc/templates/#how-to-install-uninstall-and-reinstall

### R4.0

When a template is marked as 'installed by package manager', but cannot be uninstalled there, trying to uninstall manually will result in the error "ERROR: VM installed by package manager: template-vm-name". Do as follows to be able to uninstall the template:

1. Check the state of `installed_by_rpm`

       $ qvm-prefs template-vm-name

2. If `installed_by_rpm - True]`, mark the template as not installed by package manager

       $ qvm-prefs template-vm-name installed_by_rpm false

3. Re-check the state of `installed_by_rpm`

- If `installed_by_rpm - False`, remove the template like you would a regular qube:

       $ qvm-remove template-vm-name

- If `installed_by_rpm` remains `True`, reboot your computer to bring qubes.xml in sync with qubesd, and try again to remove the template.
