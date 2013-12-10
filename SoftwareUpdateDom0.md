---
layout: wiki
title: SoftwareUpdateDom0
permalink: /wiki/SoftwareUpdateDom0/
---

Updating software in Dom0
=========================

Why would one want to update software in Dom0?
----------------------------------------------

Normally there should be few reasons for updating software in Dom0. This is because there is no networking in Dom0, which means that even if some bugs will be discovered e.g. in the Dom0 Desktop Manager, this really is not a problem for Qubes, because all the 3rd party software running in Dom0 is not accessible from VMs or network in any way. Some exceptions to the above include: Qubes GUI daemon, Xen store daemon, and disk back-ends (we plan move the disk backends to untrusted domain in Qubes 2.0). Of course we believe this software is reasonably secure and we hope it will not need patching.

However, we anticipate some other situations when updating Dom0 software might be required:

-   Updating drivers/libs for new hardware support
-   Correcting non-security related bugs (e.g. new buttons for qubes manager)
-   Adding new features (e.g. GUI backup tool)

How to do that?
---------------

Start a console in Dom0 and then run one of the following command:

1) To check and install updates for Dom0 software:

``` {.wiki}
$ sudo qubes-dom0-update
```

2) To install additional packages in Dom0 (usually not recommended):

``` {.wiki}
$ sudo qubes-dom0-update anti-evil-maid
```

You can also pass --enablerepo= option in order to enable optional repositories (see yum configuration in Dom0). This is only for advanced users who really understand what they are doing.

### How to downgrade specific package?

1.  Download older version of package:

    ``` {.wiki}
    sudo qubes-dom0-update package-version
    ```

    Yum will say that there is no update, but package will be downloaded to dom0.

2.  Downgrade packge:

    ``` {.wiki}
    sudo yum downgrade package-version
    ```


