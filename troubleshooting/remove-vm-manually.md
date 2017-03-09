---
layout: doc
title: How to Remove VMs Manually
permalink: /doc/remove-vm-manually/
---

How to Remove VMs Manually
==========================

How to Remove a TemplateVM Manually
-----------------------------------

All commands should be executed in a dom0 terminal.

1. Remove the TemplateVM's directory:

        $ rm -rf /var/lib/qubes/vm-templates/<template-name>

2. Remove the TemplateVM from qubes.xml:

        $ qvm-remove --just-db <template-name>

3. Remove the TemplateVM's `*.desktop` files from `~/.local/share/applications`:

        $ rm ~/.local/share/applications/<template-name>*

4. Remove the TemplateVM's Applications Menu entry from '/etc/xdg/menus/applications-merged'
        
        $ sudo rm /etc/xdg/menus/applications-merged/<template-name>*
