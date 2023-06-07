---
lang: en
layout: doc
permalink: /doc/how-to-reinstall-a-template/
redirect_from:
- /doc/reinstall-template/
- /doc/whonix/reinstall/
ref: 128
title: How to reinstall a template
---

If you suspect your [template](/doc/templates/) is broken, misconfigured, or compromised, you can reinstall any template that was installed from the Qubes repository.

Automatic Method
----------------

First, copy any files that you wish to keep from the template's `/home` and `/rw` folders to a safe storage location.
Then, in a dom0 terminal, run:

```
$ qvm-template reinstall <qubes-template-name>
```

Replace `qubes-template-name` with the name of the template you wish to reinstall.
Only one template can be reinstalled at a time.

Note that Qubes may initially refuse to perform the reinstall if the exact revision of the template package on your system is no longer in the Qubes online repository.
In this case, you can specify `upgrade` as the action instead and the newer version will be used.


If you prefer to use a GUI tool, open `qvm-template-gui` from a dom0 terminal.

**Reminder:** If you're trying to reinstall a template that is not in an enabled repo, you must enable that repo.
For example:

```
$ qvm-template --enablerepo=qubes-templates-community reinstall whonix-ws-16
```

**Note:** VMs that are using the reinstalled template will not be affected until they are restarted.

Manual Method
-------------

In what follows, the term "target template" refers to whichever template you want to reinstall.
If you want to reinstall more than one template, repeat these instructions for each one.

1. Clone the existing target template.

   This can be a good idea if you've customized the existing template and want to keep your customizations.
   On the other hand, if you suspect that this template is broken, misconfigured, or compromised, be certain you do not start any VMs using it in the below procedure.

2. Temporarily change all VMs based on the target template to the new clone template, or remove them.

   This can be a good idea if you have user data in these VMs that you want to keep.
   On the other hand, if you suspect that these VMs (or the templates on which they are based) are broken, misconfigured, or compromised, you may want to remove them instead.
   You can do this in Qubes Manager by right-clicking on the VM and clicking **Remove VM**, or you can use the command `qvm-remove <vm-name>` in dom0.

3. Uninstall the target template from dom0:

    ```
    $ qvm-template remove <template-name>
    ```

   For example, to uninstall the `whonix-gw-16` template:

    ```
    $ qvm-template remove whonix-gw-16
    ```

4. Reinstall the target template in dom0:

    ```shell_session
    $ qvm-template  --enablerepo=<optional-additional-repo> \
       <template-name>
    ```

   For example, to install the `whonix-gw-16` template:

    ```shell_session
    $ qvm-template install --enablerepo=qubes-templates-community \
       whonix-gw-16
    ```

5. If you temporarily changed all VMs based on the target template to the clone template in step 3, change them back to the new target template now.
   If you instead removed all VMs based on the old target template, you can recreate your desired VMs from the newly reinstalled target template now.

6. Delete the cloned template.
   You can do this in Qubes Manager by right-clicking on the VM and clicking **Remove VM**, or you can use the
   command `qvm-remove <vm-name>` in dom0.
