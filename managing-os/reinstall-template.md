---
layout: doc
title: How to Reinstall a TemplateVM
permalink: /doc/reinstall-template/
redirect_from:
- /doc/whonix/reinstall/
---

How to Reinstall a TemplateVM
=============================

If you suspect your [TemplateVM] is broken, misconfigured, or compromised,
or if you wish to do a clean reinstall in order to upgrade to a new version, you
can reinstall any TemplateVM from the Qubes repository. In what follows, the
phrase "target TemplateVM" refers to whichever TemplateVM you want to reinstall.
If you want to reinstall more than one TemplateVM, repeat these instructions for
each one.

1. (Optional) Clone the existing target TemplateVM.

   This can be a good idea if you've customized the existing template and want
   to keep your customizations. On the other hand, if you suspect that this
   template is broken, misconfigured, or compromised, you may want to remove it
   without cloning it.

2. Create a temporary dummy template:

        mkdir /var/lib/qubes/vm-templates/dummy
        touch /var/lib/qubes/vm-templates/dummy/{root.img,private.img}
        qvm-add-template dummy

3. Temporarily change all VMs based on the target TemplateVM to the new dummy
   template, or remove them.

   This can be a good idea if you have user data in these VMs that you want to
   keep. On the other hand, if you suspect that these VMs (or the templates on
   which they are based) are broken, misconfigured, or compromised, you may
   want to remove them instead. You can do this in Qubes Manager by
   right-clicking on the VM and clicking **Remove VM**, or you can use the
   command `qvm-remove <vm-name>` in dom0.

   Using a dummy template as a temporary template is preferable to using another
   real TemplateVM because you can't accidentally boot any VMs from the dummy
   template. (There is no OS in the dummy template, so the boot will fail.)

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

6. If you temporarily changed all VMs based on the target TemplateVM to the
   dummy template in step 3, change them back to the new target TemplateVM now.
   If you instead removed all VMs based on the old target TemplateVM, you can
   recreate your desired VMs from the newly reinstalled target TemplateVM now.

[TemplateVM]: /doc/templates/

