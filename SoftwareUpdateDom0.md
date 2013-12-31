---
layout: wiki
title: SoftwareUpdateDom0
permalink: /wiki/SoftwareUpdateDom0/
---

Updating software in dom0
=========================

Why would one want to update software in dom0?
----------------------------------------------

Normally, there should be few reasons for updating software in dom0. This is because there is no networking in dom0, which means that even if some bugs are discovered e.g. in the dom0 Desktop Manager, this really is not a problem for Qubes, because none of the 3rd party software running in dom0 is accessible from VMs or the network in any way. Some exceptions to this include: Qubes GUI daemon, Xen store daemon, and disk back-ends. (We plan move the disk backends to an untrusted domain in Qubes 2.0.) Of course, we believe this software is reasonably secure, and we hope it will not need patching.

However, we anticipate some other situations in which updating dom0 software might be necessary or desirable:

-   Updating drivers/libs for new hardware support
-   Correcting non-security related bugs (e.g. new buttons for qubes manager)
-   Adding new features (e.g. GUI backup tool)

How to update software in dom0
------------------------------

As of Qubes R2 Beta 3, the main update functions have been integrated into the Qubes VM Manager GUI: Simply select dom0 in the VM list, then click the **Update VM system** button (the blue, downward-pointing arrow). In addition, updating dom0 has been made more convenient: You will be prompted on the desktop whenever new dom0 updates are available and given the choice to run the update with a single click.

Of course, command line tools are still available for accomplishing various update-related tasks (some of which are not available via Qubes VM Manager). In order to update dom0 from the command line, start a console in dom0 and then run one of the following commands:

1.  To check and install updates for dom0 software:

    ``` {.wiki}
    $ sudo qubes-dom0-update
    ```

1.  To install additional packages in dom0 (usually not recommended):

    ``` {.wiki}
    $ sudo qubes-dom0-update anti-evil-maid
    ```

    You may also pass the `--enablerepo=` option in order to enable optional repositories (see yum configuration in dom0). However, this is only for advanced users who really understand what they are doing.

### How to downgrade a specific package

1.  Download an older version of the package:

    ``` {.wiki}
    sudo qubes-dom0-update package-version
    ```

    Yum will say that there is no update, but the package will nonetheless be downloaded to dom0.

1.  Downgrade the packge:

    ``` {.wiki}
    sudo yum downgrade package-version
    ```


