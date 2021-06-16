---
lang: en
layout: doc
permalink: /doc/reinstall-template/
redirect_from:
- /doc/whonix/reinstall/
ref: 128
---

How to Reinstall a TemplateVM
=============================

If you suspect your [TemplateVM](/doc/templates/) is broken, misconfigured, or compromised, you can reinstall any TemplateVM that was installed from the Qubes repository.

Automatic Method
----------------

First, copy any files that you wish to keep from the TemplateVM's `/home` and `/rw` folders to a safe storage location.
Then, in a dom0 terminal, run:

```
$ sudo qubes-dom0-update --action=reinstall qubes-template-package-name
```

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

```
$ sudo qubes-dom0-update --enablerepo=qubes-templates-community --action=reinstall qubes-template-whonix-ws
```

**Note:** VMs that are using the reinstalled template will not be affected until they are restarted.

Manual Method
-------------

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

    ```
    $ sudo dnf remove <template-package-name>
    ```

   For example, to uninstall the `whonix-gw` template:

    ```
    $ sudo dnf remove qubes-template-whonix-gw
    ```

4. Reinstall the target TemplateVM in dom0:

    ```shell_session
    $ sudo qubes-dom0-update --enablerepo=<optional-additional-repo> \
       <template-package-name>
    ```

   For example, to install the `whonix-gw` template:

    ```shell_session
    $ sudo qubes-dom0-update --enablerepo=qubes-templates-community \
       qubes-template-whonix-gw
    ```

5. If you temporarily changed all VMs based on the target TemplateVM to the clone template in step 3, change them back to the new target TemplateVM now.
   If you instead removed all VMs based on the old target TemplateVM, you can recreate your desired VMs from the newly reinstalled target TemplateVM now.

6. Delete the cloned template.
   You can do this in Qubes Manager by right-clicking on the VM and clicking **Remove VM**, or you can use the
   command `qvm-remove <vm-name>` in dom0.

