=====================
Managing qube kernels
=====================

.. warning::

      This page is intended for advanced users.

By default, VMs kernels are provided by dom0. (See :ref:`here <user/advanced-topics/how-to-install-software-in-dom0:kernel upgrade>` for information about upgrading kernels in dom0.) This means that:

1. You can select the kernel version (using GUI VM Settings tool or ``qvm-prefs`` commandline tool);

2. You can modify kernel options (using ``qvm-prefs`` commandline tool);

3. You can **not** modify any of the above from inside a VM;

4. Installing additional kernel modules is cumbersome.



*Note*: In the examples below, although the specific version numbers might be old, the commands have been verified on R3.2 and R4.0 with debian-9 and fedora-26 templates.

To select which kernel a given VM will use, you can either use Qubes Manager (VM settings, advanced tab), or the ``qvm-prefs`` tool:

.. code:: console

      [user@dom0 ~]$ dnf list --installed kernel
      Installed Packages
      kernel.x86_64            1000:6.12.47-1.qubes.fc37             @qubes-dom0-cached
      kernel.x86_64            1000:6.12.54-1.qubes.fc37             @qubes-dom0-cached
      kernel.x86_64            1000:6.12.59-1.qubes.fc37             @qubes-dom0-cached
      [user@dom0 ~]$ qvm-prefs my-appvm kernel
      6.12.59-1.fc37
      [user@dom0 ~]$ qvm-prefs my-appvm kernel 6.12.54-1.fc37
      [user@dom0 ~]$ qvm-prefs -D my-appvm kernel


To check/change the default kernel you can either go to “Global settings” in Qubes Manager, or use the ``qubes-prefs`` tool:

.. code:: console

      [user@dom0 ~]$ qubes-prefs default-kernel
      6.12.59-1.fc37
      [user@dom0 ~]$ qubes-prefs default-kernel 6.12.54-1.fc37


To view kernel options, you can use the GUI VM Settings tool; to view and change them, use ``qvm-prefs`` commandline tool:

.. code:: console

      [user@dom0 ~]$ qvm-prefs my-appvm kernelopts
      swiotlb=2048
      [user@dom0 ~]$ qvm-prefs my-appvm kernelopts "swiotlb=10240 apparmor=1 security=apparmor"


Installing different kernel using Qubes kernel package
------------------------------------------------------


VM kernels are packaged by the Qubes team in the ``kernel`` packages. Generally, the system will keep the three newest available versions. You can list them using ``rpm`` or ``dnf`` commands:

.. code:: console

      [user@dom0 ~]$ rpm -qa 'kernel'
      kernel-6.12.47-1.qubes.fc37.x86_64
      kernel-6.12.54-1.qubes.fc37.x86_64
      kernel-6.12.59-1.qubes.fc37.x86_64
      [user@dom0 ~]$ dnf list --installed kernel
      Installed Packages
      kernel.x86_64            1000:6.12.47-1.qubes.fc37             @qubes-dom0-cached
      kernel.x86_64            1000:6.12.54-1.qubes.fc37             @qubes-dom0-cached
      kernel.x86_64            1000:6.12.59-1.qubes.fc37             @qubes-dom0-cached


If you want a more recent version, you can check ``qubes-dom0-unstable`` and ``qubes-dom0-current-testing`` repositories. There is also ``kernel-latest`` package which should provide a more recent (non-LTS) kernel, but has received much less testing. As the names suggest, keep in mind that those packages may be less stable than the default ones.

To check available versions in the ``qubes-dom0-current-testing`` repository:

.. code:: console

      [root@dom0 ~]# qubes-dom0-update --enablerepo=qubes-dom0-current-testing --action=list kernel-latest kernel
      Using sys-whonix as UpdateVM for Dom0
      Updating package lists. This may take a while...
      Fedora 37 - x86_64                              3.1 kB/s | 5.1 kB     00:01    
      Fedora 37 - x86_64 - Updates                    3.2 kB/s | 5.0 kB     00:01                    
      Qubes Host Repository (updates)                 2.4 kB/s | 2.7 kB     00:01                    
      Qubes Host Repository (updates-testing)         3.1 kB/s | 2.8 kB     00:00                    
      Installed Packages                                                                             
      kernel.x86_64           1000:6.12.47-1.qubes.fc37     @System                                  
      kernel.x86_64           1000:6.12.54-1.qubes.fc37     @System                                  
      kernel.x86_64           1000:6.12.59-1.qubes.fc37     @System                                  
      Available Packages                                                                             
      kernel.src              1000:6.12.63-1.qubes.fc37     qubes-dom0-current-testing               
      kernel.x86_64           1000:6.12.63-1.qubes.fc37     qubes-dom0-current-testing               
      kernel-latest.src       1000:6.18.2-1.qubes.fc37      qubes-dom0-current-testing               
      kernel-latest.x86_64    1000:6.18.2-1.qubes.fc37      qubes-dom0-current-testing               
      No packages downloaded


Installing a new version from ``qubes-dom0-current-testing`` repository:

.. code:: console

      [root@dom0 ~]# qubes-dom0-update --enablerepo=qubes-dom0-current-testing kernel
      Using sys-whonix as UpdateVM for Dom0
      Downloading packages. This may take a while...
      Fedora 37 - x86_64                              1.8 kB/s | 5.1 kB     00:02    
      Fedora 37 - x86_64 - Updates                    3.5 kB/s | 5.0 kB     00:01                    
      Qubes Host Repository (updates)                 2.1 kB/s | 2.7 kB     00:01                    
      Qubes Host Repository (updates-testing)         2.2 kB/s | 2.8 kB     00:01                    
      Last metadata expiration check: 0:00:01 ago on Fri Dec 26 21:49:54 2025.                       
      Package kernel-1000:6.12.47-1.qubes.fc37.x86_64 is already installed.                          
      Package kernel-1000:6.12.54-1.qubes.fc37.x86_64 is already installed.                          
      Package kernel-1000:6.12.59-1.qubes.fc37.x86_64 is already installed.                          
      Dependencies resolved.                                                                         
      ================================================================================               
       Package      Arch   Version                   Repository                  Size                
      ================================================================================               
      Installing:                                                                                    
       kernel       x86_64 1000:6.12.63-1.qubes.fc37 qubes-dom0-current-testing  13 M                
       kernel-modules                                                                                
                    x86_64 1000:6.12.63-1.qubes.fc37 qubes-dom0-current-testing  84 M                
      Removing:                                                                                      
       kernel       x86_64 1000:6.12.47-1.qubes.fc37 @System                     42 M                
       kernel-modules                                                                                
                    x86_64 1000:6.12.47-1.qubes.fc37 @System                    508 M                
                                                                                                     
      Transaction Summary                                                                            
      ================================================================================               
      Install  2 Packages                                                                            
      Remove   2 Packages                                                                            
                                                                                               
      Total download size: 97 M                                                                      
      DNF will only download packages for the transaction.
      Downloading Packages:

      ...

      Complete!                                                                         
      The downloaded packages were saved in cache until the next successful transaction.
      You can remove cached packages by executing 'dnf clean packages'.                 
      Qubes OS Repository for Dom0                      2.9 MB/s | 3.0 kB     00:00     
      Qubes OS Repository for Dom0                      2.2 MB/s |  66 kB     00:00    
      Package kernel-1000:6.12.47-1.qubes.fc37.x86_64 is already installed.
      Package kernel-1000:6.12.54-1.qubes.fc37.x86_64 is already installed.
      Package kernel-1000:6.12.59-1.qubes.fc37.x86_64 is already installed.
      Dependencies resolved.
      Nothing to do.
      Complete!
      [root@dom0 ~]# dnf list kernel
      Qubes OS Repository for Dom0                      2.9 MB/s | 3.0 kB     00:00    
      Installed Packages
      kernel.x86_64             1000:6.12.47-1.qubes.fc37             @qubes-dom0-cached
      kernel.x86_64             1000:6.12.54-1.qubes.fc37             @qubes-dom0-cached
      kernel.x86_64             1000:6.12.59-1.qubes.fc37             @qubes-dom0-cached
      Available Packages
      kernel.x86_64             1000:6.12.63-1.qubes.fc37             qubes-dom0-cached
      [root@dom0 ~]# dnf install kernel-1000:6.12.63-1.qubes.fc37
      Qubes OS Repository for Dom0                      2.9 MB/s | 3.0 kB     00:00    
      Dependencies resolved.
      ==================================================================================
       Package          Arch     Version                     Repository            Size
      ==================================================================================
      Installing:
       kernel           x86_64   1000:6.12.63-1.qubes.fc37   qubes-dom0-cached     13 M
       kernel-modules   x86_64   1000:6.12.63-1.qubes.fc37   qubes-dom0-cached     84 M
      Removing:
       kernel           x86_64   1000:6.12.47-1.qubes.fc37   @qubes-dom0-cached    42 M
       kernel-modules   x86_64   1000:6.12.47-1.qubes.fc37   @qubes-dom0-cached   508 M

      Transaction Summary
      ==================================================================================
      Install  2 Packages
      Remove   2 Packages
      
      Total size: 97 M
      Is this ok [y/N]: y
      Downloading Packages:
      Running transaction check
      Transaction check succeeded.
      Running transaction test
      Transaction test succeeded.
      Running transaction

      ...

      Installed:
        kernel-1000:6.12.63-1.qubes.fc37.x86_64                                         
        kernel-modules-1000:6.12.63-1.qubes.fc37.x86_64                                 
      Removed:
        kernel-1000:6.12.47-1.qubes.fc37.x86_64                                         
        kernel-modules-1000:6.12.47-1.qubes.fc37.x86_64                                 

      Complete!


The newly installed package is set as the default VM kernel.

Installing different VM kernel based on dom0 kernel
---------------------------------------------------


It is possible to package a kernel installed in dom0 as a VM kernel. This makes it possible to use a VM kernel which is not packaged by the Qubes team. This includes:

- using a Fedora kernel package

- using a manually compiled kernel



To prepare such a VM kernel, you need to install the ``qubes-kernel-vm-support`` package in dom0 and also have matching kernel headers installed (``kernel-devel`` package in the case of a Fedora kernel package). You can install requirements using ``qubes-dom0-update``:

.. code:: console

      [user@dom0 ~]$ sudo qubes-dom0-update qubes-kernel-vm-support kernel-devel
      Using sys-firewall as UpdateVM to download updates for Dom0; this may take some time...
      Running command on VM: 'sys-firewall'...
      Loaded plugins: langpacks, post-transaction-actions, yum-qubes-hooks
      Package 1000:kernel-devel-4.1.9-6.pvops.qubes.x86_64 already installed and latest version
      Resolving Dependencies
      (...)

      ================================================================================
       Package                      Arch        Version        Repository        Size
      ================================================================================
      Installing:
       qubes-kernel-vm-support      x86_64      3.1.2-1.fc20   qubes-dom0-cached 9.2 k

      Transaction Summary
      ================================================================================
      Install  1 Package

      Total download size: 9.2 k
      Installed size: 13 k
      Is this ok [y/d/N]: y
      Downloading packages:
      Running transaction check
      Running transaction test
      Transaction test succeeded
      Running transaction (shutdown inhibited)
        Installing : qubes-kernel-vm-support-3.1.2-1.fc20.x86_64                  1/1

      Creating symlink /var/lib/dkms/u2mfn/3.1.2/source ->
                       /usr/src/u2mfn-3.1.2

      DKMS: add completed.
        Verifying  : qubes-kernel-vm-support-3.1.2-1.fc20.x86_64                  1/1

      Installed:
        qubes-kernel-vm-support.x86_64 0:3.1.2-1.fc20

      Complete!


Then you can call the ``qubes-prepare-vm-kernel`` tool to actually package the kernel. The first parameter is kernel version (exactly as seen by the kernel), the second one (optional) is short name. This is visible in Qubes Manager and the ``qvm-prefs`` tool.

.. code:: console

      [user@dom0 ~]$ sudo qubes-prepare-vm-kernel 4.1.9-6.pvops.qubes.x86_64 4.1.qubes
      --> Building files for 4.1.9-6.pvops.qubes.x86_64 in /var/lib/qubes/vm-kernels/4.1.qubes
      ---> Recompiling kernel module (u2mfn)
      ---> Generating modules.img
      mke2fs 1.42.12 (29-Aug-2014)
      ---> Generating initramfs
      --> Done.


Kernel files structure
----------------------


Kernel for a VM is stored in ``/var/lib/qubes/vm-kernels/KERNEL_VERSION`` directory (``KERNEL_VERSION`` replaced with actual version). Qubes 4.x supports the following files there:

- ``vmlinuz`` - kernel binary (may not be a Linux kernel)

- ``initramfs`` - initramfs for the kernel to load

- ``modules.img`` - ext4 filesystem image containing Linux kernel modules (to be mounted at ``/lib/modules``); additionally it should contain a copy of ``vmlinuz`` and ``initramfs`` in its root directory (for loading by qemu inside stubdomain)

- ``default-kernelopts-common.txt`` - default kernel options, in addition to those specified with ``kernelopts`` qube property (can be disabled with ``no-default-kernelopts`` feature)



All the files besides ``vmlinuz`` are optional in Qubes R4.2 or newer.

Using kernel installed in the VM
--------------------------------


Non-minimal debian and fedora templates already have grub and related tools preinstalled so if you want to use one of the distribution kernels, all you need to do is clone either template to a new one, then:

.. code:: console

      [user@dom0 ~]$ qvm-prefs <clonetemplatename> virt_mode hvm
      [user@dom0 ~]$ qvm-prefs <clonetemplatename> kernel ''



Installing kernel in Fedora VM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Distribution kernel
^^^^^^^^^^^^^^^^^^^

Install kernel and the packages required to run vm with its own kernel:

.. code:: console

  [root@fedora-vm ~]# dnf install kernel qubes-kernel-vm-support grub2



Once the kernel is installed, you need to setup ``grub2`` by running:

.. code:: console

  [root@fedora-vm ~]# grub2-install /dev/xvda



Finally, you need to create a GRUB configuration. You may want to adjust some settings in ``/etc/default/grub``; for example, lower ``GRUB_TIMEOUT`` to speed up VM startup. Then, you need to generate the actual configuration. In Fedora it can be done using the ``grub2-mkconfig`` tool:

.. code:: console

  [root@fedora-vm ~]# grub2-mkconfig -o /boot/grub2/grub.cfg



Custom kernel
^^^^^^^^^^^^^

If you are using a manually built kernel, you need to handle the initramfs and kernel modules on your own. Take a look at the ``dkms`` documentation, especially the ``dkms autoinstall`` command may be useful. If you did not see the ``kernel`` install rebuild your initramfs, or are using a manually built kernel, you will need to rebuild it yourself. Replace the version numbers in the example below with the ones appropriate to the kernel you are installing:

.. code:: console

  [root@fedora-vm ~]# dracut -f /boot/initramfs-4.15.14-200.fc26.x86_64.img 4.15.14-200.fc26.x86_64



Once the kernel is installed, you need to setup ``grub2`` by running:

.. code:: console

  [root@fedora-vm ~]# grub2-install /dev/xvda



Finally, you need to create a GRUB configuration. You may want to adjust some settings in ``/etc/default/grub``; for example, lower ``GRUB_TIMEOUT`` to speed up VM startup. Then, you need to generate the actual configuration. In Fedora it can be done using the ``grub2-mkconfig`` tool:

.. code:: console

  [root@fedora-vm ~]# grub2-mkconfig -o /boot/grub2/grub.cfg



You can safely ignore this error message:

.. code:: output

      grub2-probe: error: cannot find a GRUB drive for /dev/mapper/dmroot. Check your device.map



Then shutdown the VM.

**Notes:**

- You may also use ``PV`` mode instead of ``HVM`` but this is not recommended for security purposes.

- If you require ``PV`` mode, install ``grub2-xen-pvh`` in dom0 and change the template’s kernel to ``pvgrub2-pvh``.

- If you require ``PVH`` mode, install ``grub2-xen-pvh`` in dom0 and change the kernel to ``pvgrub2-pvh``.

- To install ``grub2-xen-pvh`` run the command ``sudo qubes-dom0-update pvgrub2-pvh`` in dom0.



Installing kernel in Debian VM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Distribution kernel
^^^^^^^^^^^^^^^^^^^


Apply the following instruction in a Debian template or in a Debian standalone.

Using a distribution kernel package the initramfs and kernel modules should be handled automatically.

Install distribution kernel image, kernel headers and the grub.

.. code:: console

  [root@debian-vm ~]# apt install linux-image-amd64 linux-headers-amd64 grub2 qubes-kernel-vm-support



If you are doing that on a qube based on “Debian Minimal” template, a grub gui will popup during the installation, asking you where you want to install the grub loader. You must select ``/dev/xvda`` (check the box using the space bar, and validate your choice with “Enter”.) If this popup does not appear during the installation, you must manually setup ``grub2`` by running:

.. code:: console

  [root@debian-vm ~]# grub-install /dev/xvda



You can safely ignore this error message: ``grub2-probe: error: cannot find a GRUB drive for /dev/mapper/dmroot. Check your device.map``

You may want to adjust some settings in ``/etc/default/grub`` (or better ``/etc/default/grub.d``). For example, lower ``GRUB_TIMEOUT`` to speed up VM startup. You need to re-run ``sudo update-grub`` after making grub configuration changes.

Then shutdown the VM.

Go to dom0: :menuselection:`Qubes VM Manager --> right click on the VM --> Qube settings --> Advanced`

Depends on ``Virtualization`` mode setting:

- ``Virtualization`` mode ``PV``: Possible, however use of ``Virtualization`` mode ``PV`` is discouraged for security purposes.

  - If you require ``Virtualization`` mode ``PV``, install ``grub2-xen-pvh`` in dom0. This can be done by running command ``sudo qubes-dom0-update pvgrub2-pvh`` in dom0.



- ``Virtualization`` mode ``PVH``: Possible. Install ``grub2-xen-pvh`` in dom0.

- ``Virtualization`` mode ``HVM``: Possible.



The ``Kernel`` setting of the ``Virtualization`` mode setting:

- If ``Virtualization`` is set to ``PVH`` -> ``Kernel`` -> choose ``pvgrub2-pvh`` -> OK

- If ``Virtualization`` is set to ``PV`` -> ``Kernel`` -> choose ``pvgrub2`` -> OK

- If ``Virtualization`` is set to ``HVM`` -> ``Kernel`` -> choose ``none`` -> OK



Start the VM.

The process of using Qubes VM kernel with distribution kernel is complete.

Custom kernel
^^^^^^^^^^^^^


Any kernel can be installed. Just make sure to install kernel headers as well.

If you are building the kernel manually, do this using ``dkms`` and ``initramfs-tools``.

Run DKMS. Replace this with actual kernel version.



.. code:: console

  [root@debian-vm ~]# dkms autoinstall -k <kernel-version>


For example.



.. code:: console

  [root@debian-vm ~]# dkms autoinstall -k 4.19.0-6-amd64


Update initramfs.



.. code:: console

  [root@debian-vm ~]# update-initramfs -u


The output should look like this:

.. code:: console

  [root@debian-vm ~]# dkms autoinstall -k 3.16.0-4-amd64

      u2mfn:
      Running module version sanity check.
        - Original module
          - No original module exists within this kernel
        - Installation
          - Installing to /lib/modules/3.16.0-4-amd64/updates/dkms/

      depmod....

        DKMS: install completed.
      $ sudo update-initramfs -u
      update-initramfs: Generating /boot/initrd.img-3.16.0-4-amd64


Troubleshooting
^^^^^^^^^^^^^^^


In case of problems, visit the :ref:`VM Troubleshooting guide <user/troubleshooting/vm-troubleshooting:vm kernel troubleshooting>` to learn how to access the VM console, view logs and fix a VM kernel installation.
