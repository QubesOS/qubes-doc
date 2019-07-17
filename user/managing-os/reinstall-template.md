---
layout: doc
title: How to Reinstall a TemplateVM
permalink: /doc/reinstall-template/
redirect_from:
- /doc/whonix/reinstall/
---

How to Reinstall a TemplateVM
=============================

If you suspect your [TemplateVM] is broken, misconfigured, or compromised, you can reinstall any TemplateVM that was installed from the Qubes repository.

The procedure varies by Qubes version; see the appropriate section below.

Automated Reinstallation Method (R3.1+)
----------------------------

First, copy any files that you wish to keep from the TemplateVM's `/home` and `/rw` folders to a safe storage location.
Then, in a dom0 terminal, run:

    $ sudo qubes-dom0-update --action=reinstall qubes-template-package-name

Replace `qubes-template-package-name` with the name of the *package* of the template you wish to reinstall.
For example, use `qubes-template-fedora-25` if you wish to reinstall the `fedora-25` template.
Only one template can be reinstalled at a time.

Note that Qubes may initially refuse to perform the reinstall if the exact revision of the template package on your system is no longer in the Qubes online repository.
In this case, you can specify `upgrade` as the action instead and the newer version will be used. 
The other `dnf` package actions that are supported in addition to `reinstall` and `upgrade` are `upgrade-to` and `downgrade`.
Note that the `upgrade`, `upgrade-to`, and `downgrade` commands are only supported under Fedora based UpdateVMs.
If you receive a message about them being unsupported, review the manual reinstallation method below.

**Reminder:** If you're trying to reinstall a template that is not in an enabled repo, you must enable that repo.
For example:

    $ sudo qubes-dom0-update --enablerepo=qubes-templates-community --action=reinstall qubes-template-whonix-ws

**Note:** VMs that are using the reinstalled template will not be affected until they are restarted.


Manual Reinstallation Method (R3.1+)
----------------------------

In what follows, the term "target TemplateVM" refers to whichever TemplateVM you want to reinstall.
If you want to reinstall more than one TemplateVM, repeat these instructions for each one.

1. Clone the existing target TemplateVM.

   This can be a good idea if you've customized the existing template and want to keep your customizations.
   On the other hand, if you suspect that this template is broken, misconfigured, or compromised, be certain you do not start any VMs using it in the below procedure.

2. Temporarily change all VMs based on the target TemplateVM to the new clone template, or remove them.

   This can be a good idea if you have user data in these VMs that you want to keep.
   On the other hand, if you suspect that these VMs (or the templates on which they are based) are broken, misconfigured, or compromised, you may want to remove them instead. 
   You can do this in Qubes Manager by right-clicking on the VM and clicking **Remove VM**, or you can use the command `qvm-remove <vm-name>` in dom0.

3. Uninstall the target TemplateVM from dom0:

        $ sudo dnf remove <template-package-name>

   For example, to uninstall the `whonix-gw` template:

        $ sudo dnf remove qubes-template-whonix-gw

4. Reinstall the target TemplateVM in dom0:

        $ sudo qubes-dom0-update --enablerepo=<optional-additional-repo> \
          <template-package-name>

   For example, to install the `whonix-gw` template:

        $ sudo qubes-dom0-update --enablerepo=qubes-templates-community \
          qubes-template-whonix-gw

5. If you temporarily changed all VMs based on the target TemplateVM to the clone template in step 3, change them back to the new target TemplateVM now.
   If you instead removed all VMs based on the old target TemplateVM, you can recreate your desired VMs from the newly reinstalled target TemplateVM now.
   
6. Delete the cloned template.
   You can do this in Qubes Manager by right-clicking on the VM and clicking **Remove VM**, or you can use the
   command `qvm-remove <vm-name>` in dom0.
   
   
Manual Reinstallation Method (R3.0 or earlier)
----------------------------

If you're using Qubes 3.0 or older, you should use the manual reinstallation method. 
You can also use this method on later Qubes versions if, for any reason, you want to reinstall a template manually.

In what follows, the term "target TemplateVM" refers to whichever TemplateVM you want to reinstall. 
If you want to reinstall more than one TemplateVM, repeat these instructions for each one.

1. (Optional) Clone the existing target TemplateVM.

   This can be a good idea if you've customized the existing template and want to keep your customizations. 
   On the other hand, if you suspect that this template is broken, misconfigured, or compromised, you may want to remove it without cloning it.

2. Create a temporary dummy template:

        mkdir /var/lib/qubes/vm-templates/dummy
        touch /var/lib/qubes/vm-templates/dummy/{root.img,private.img}
        qvm-add-template dummy

3. Temporarily change all VMs based on the target TemplateVM to the new dummy template, or remove them.

   This can be a good idea if you have user data in these VMs that you want to keep. 
   On the other hand, if you suspect that these VMs (or the templates on which they are based) are broken, misconfigured, or compromised, you may want to remove them instead.
   You can do this in Qubes Manager by right-clicking on the VM and clicking **Remove VM**, or you can use the command `qvm-remove <vm-name>` in dom0.

   Using a dummy template as a temporary template is preferable to using another real TemplateVM because you can't accidentally boot any VMs from the dummy template.
   (There is no OS in the dummy template, so the boot will fail.)

4. Uninstall the target TemplateVM from dom0:

        $ sudo yum remove <template-package-name>

   For example, to uninstall the `whonix-gw` template:

        $ sudo yum remove qubes-template-whonix-gw

5. Reinstall the target TemplateVM in dom0:

        $ sudo qubes-dom0-update --enablerepo=<optional-additional-repo> \
          <template-package-name>

   For example, to install the `whonix-gw` template:

        $ sudo qubes-dom0-update --enablerepo=qubes-templates-community \
          qubes-template-whonix-gw

6. If you temporarily changed all VMs based on the target TemplateVM to the dummy template in step 3, change them back to the new target TemplateVM now.
   If you instead removed all VMs based on the old target TemplateVM, you can recreate your desired VMs from the newly reinstalled target TemplateVM now.

[TemplateVM]: /doc/templates/

