---
layout: doc
title: Reinstall Whonix in Qubes
permalink: /doc/whonix/reinstall/
---

Reinstall Whonix in Qubes
===========================

If you suspect your Whonix templates are broken, misconfigured, or compromised,
or if you wish to do a clean reinstall in order to upgrade to a new version, you
can reinstall the Whonix templates from the Qubes repository. This procedure
involves [uninstalling] your Whonix templates, then [installing] them again.

1. (Optional) Clone your existing `whonix-gw` and `whonix-ws` templates.

   This can be a good idea if you've customized the existing templates and want
   to keep them. On the other hand, if you suspect that these templates are
   broken, misconfigured, or compromised, you may want to remove them
   without cloning them.

2. (Optional) Temporarily change all VMs based on `whonix-gw` and `whonix-ws` to
   another template (e.g., the ones created in the previous step).

   This can be a good idea if you have user data in these VMs that you want to
   keep. On the other hand, if you suspect that these VMs (or the templates on
   which they are based) are broken, misconfigured, or compromised, you may
   want to remove them instead. You can do this in Qubes Manager by
   right-clicking on the VM and clicking **Remove VM**, or you can use the
   command `qvm-remove <vm-name>` in dom0.

3. Uninstall the Whonix templates from dom0:

        $ sudo yum remove qubes-template-whonix-gw
        $ sudo yum remove qubes-template-whonix-ws

4. Reinstall the Whonix templates in dom0:

        $ sudo qubes-dom0-update --enablerepo=qubes-templates-community \
          qubes-template-whonix-gw qubes-template-whonix-ws

5. If you followed step 2, change the VMs from step 2 back to the new
   `whonix-gw` and `whonix-ws`. If you instead removed all VMs based on the old
   `whonix-gw` and `whonix-ws`, simply create your desired VMs from the new
   templates.

   At a minimum, you'll want a ProxyVM (conventionally called `sys-whonix`)
   based on `whonix-gw` and an AppVM based on `whonix-ws` that uses `sys-whonix`
   as its NetVM.


[uninstalling]: /doc/whonix/uninstall/
[installing]: /doc/whonix/install/

