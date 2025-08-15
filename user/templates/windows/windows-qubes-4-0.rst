============================================
How to install Windows qubes in Qubes OS 4.0
============================================


**Warning:** *The content below describes Windows installation in Qubes R4.0. The text has been updated to reflect the newer R4.1 release and QWT recent development. Please see* :doc:`this updated document </user/templates/windows/windows-qubes-4-1>` *for instructions for Qubes R4.1.*

Simple Windows install
----------------------


If you just want something simple and you can live without some features.

Works:

- display (1440x900 or 1280x1024 are a nice fit onto FHD hw display)

- keyboard (incl. correct mapping), pointing device

- network (emulated Realtek NIC)



Does not work:

- copy & paste (the qubes way)

- copying files into / out of the VM (the qubes way)

- assigning USB devices (the qubes way via the tray applet)

- audio output and input

- PCI device 5853:0001 (Xen platform device) - no driver

- all other features/hardware needing special tool/driver support



Installation procedure:

- Have the Windows 10 ISO image (I used the 64-bit version) downloaded in some qube.

- Create a new Qube:

  - Name: Win10, Color: red

  - Standalone Qube not based on a template

  - Networking: sys-firewall (default)

  - Launch settings after creation: check

  - Click “OK”.



- Settings:

  - Basic:

    - System storage: 30000+ MB



  - Advanced:

    - Include in memory balancing: uncheck

    - Initial memory: 4096+ MB

    - Kernel: None

    - Mode: HVM



  - Click “Apply”.

  - Click “Boot from CDROM”:

    - “from file in qube”:

      - Select the qube that has the ISO.

      - Select ISO by clicking “…”.



    - Click “OK” to boot into the windows installer.





- Windows Installer:

  - Mostly as usual, but automatic reboots will halt the qube - just restart it again and again until the installation is finished.

  - Install on first disk.

  - Windows license may be read from flash via root in dom0:
    ``strings < /sys/firmware/acpi/tables/MSDM``
    Alternatively, you can also try a Windows 7 license key (as of 2018/11 they are still accepted for a free upgrade).
    I first installed Windows and all updates, then entered the license key.



- Afterwards:

  - In case you switch from ``sys-network`` to ``sys-whonix``, you’ll need a static IP network configuration, DHCP won’t work for ``sys-whonix``.

  - Use ``powercfg -H off`` and ``disk cleanup`` to save some disk space.





Qubes 4.0 - importing a Windows VM from R3.2
--------------------------------------------


Importing should work, simply make sure that you are not using Xen’s newer linux stubdomain and that the VM is in HVM mode (these steps should be done automatically when importing the VM):

.. code:: console

      $ qvm-features VMNAME linux-stubdom ''
      $ qvm-prefs VMNAME virt_mode hvm



Note however that you are better off creating a new Windows VM to benefit from the more recent emulated hardware: R3.2 uses a MiniOS based stubdomain with an old and mostly unmaintained ‘qemu-traditional’ while R4.0 uses a Linux based stubdomain with a recent version of upstream qemu (see `this post <https://groups.google.com/d/msg/qubes-devel/tBqwJmOAJ94/xmFCGJnuAwAJ>`__).

Windows qube installation
-------------------------


qvm-create-windows-qube
^^^^^^^^^^^^^^^^^^^^^^^


An unofficial, third-party tool for automating this process is available `here <https://github.com/elliotkillick/qvm-create-windows-qube>`__. (Please note that this tool has not been reviewed by the Qubes OS Project. Use it at your own risk.) However, if you are an expert or want to do it manually you may continue below.

Summary
^^^^^^^


.. code:: console

      $ qvm-create --class StandaloneVM --label red --property virt_mode=hvm win7new
      $ qvm-prefs win7new memory 4096
      $ qvm-prefs win7new maxmem 4096
      $ qvm-prefs win7new kernel ''
      $ qvm-volume extend win7new:root 25g
      $ qvm-prefs win7new debug true
      $ qvm-features win7new video-model cirrus
      $ qvm-start --cdrom=untrusted:/home/user/windows_install.iso win7new
      # restart after the first part of the windows installation process ends
      $ qvm-start win7new
      # once Windows is installed and working
      $ qvm-prefs win7new memory 2048
      $ qvm-prefs win7new maxmem 2048
      $ qvm-features --unset win7new video-model
      $ qvm-prefs win7new qrexec_timeout 300
      # with Qubes Windows Tools installed:
      $ qvm-prefs win7new debug false



To install Qubes Windows Tools, follow instructions in :doc:`Qubes Windows Tools </user/templates/windows/qubes-windows-tools-4-0>`.

Detailed instructions
^^^^^^^^^^^^^^^^^^^^^


MS Windows versions considerations:

- The instructions *may* work on other versions than Windows 7 x64 but haven’t been tested.

- Qubes Windows Tools (QWT) only supports Windows 7 x64. Note that there are `known issues <https://github.com/QubesOS/qubes-issues/issues/3585>`__ with QWT on Qubes 4.x

- For Windows 10 under Qubes 4.0, a way to install QWT 4.0.1.3, which has worked in several instances, is described in :doc:`Qubes Windows Tools </user/templates/windows/qubes-windows-tools-4-0>`.



Create a VM named win7new in :doc:`HVM </user/advanced-topics/standalones-and-hvms>` mode (Xen’s current PVH limitations precludes from using PVH):

.. code:: console

      $ qvm-create --class StandaloneVM --label red --property virt_mode=hvm win7new



Windows’ installer requires a significant amount of memory or else the VM will crash with such errors:

``/var/log/xen/console/hypervisor.log``:

.. code:: text

      p2m_pod_demand_populate: Dom120 out of PoD memory! (tot=102411 ents=921600 dom120)
      (XEN) domain_crash called from p2m-pod.c:1218
      (XEN) Domain 120 (vcpu#0) crashed on cpu#3:



So, increase the VM’s memory to 4096MB (memory = maxmem because we don’t use memory balancing).

.. code:: console

      $ qvm-prefs win7new memory 4096
      $ qvm-prefs win7new maxmem 4096



Disable direct boot so that the VM will go through the standard cdrom/HDD boot sequence:

.. code:: console

      $ qvm-prefs win7new kernel ''



A typical Windows 7 installation requires between 15GB up to 19GB of disk space depending on the version (Home/Professional/…). Windows updates also end up using significant space. So, extend the root volume from the default 10GB to 25GB (note: it is straightforward to increase the root volume size after Windows is installed: simply extend the volume again in dom0 and then extend the system partition with Windows’s disk manager).

.. code:: console

      $ qvm-volume extend win7new:root 25g



Set the debug flag in order to have a graphical console:

.. code:: console

      $ qvm-prefs win7new debug true



The second part of the installation process will crash with the standard VGA video adapter and the VM will stay in “transient” mode with the following error in ``guest-win7new-dm.log``:

.. code:: text

      qemu: /home/user/qubes-src/vmm-xen-stubdom-linux/build/qemu/exec.c:1187: cpu_physical_memory_snapshot_get_dirty: Assertion `start + length <= snap->end' failed.



To avoid that error we temporarily have to switch the video adapter to ‘cirrus’:

.. code:: console

      $ qvm-features win7new video-model cirrus



The VM is now ready to be started; the best practice is to use an installation ISO :ref:`located in a VM <user/advanced-topics/standalones-and-hvms:installing an os in an hvm>`:

.. code:: console

      $ qvm-start --cdrom=untrusted:/home/user/windows_install.iso win7new



Given the higher than usual memory requirements of Windows, you may get a ``Not enough memory to start domain 'win7new'`` error. In that case try to shutdown unneeded VMs to free memory before starting the Windows VM.

At this point you may open a tab in dom0 for debugging, in case something goes amiss:

.. code:: console

      tailf /var/log/qubes/vm-win7new.log \
         /var/log/xen/console/hypervisor.log \
         /var/log/xen/console/guest-win7new-dm.log



The VM will shutdown after the installer completes the extraction of Windows installation files. It’s a good idea to clone the VM now (eg. ``qvm-clone win7new win7newbkp1``). Then, (re)start the VM with ``qvm-start win7new``.

The second part of Windows’ installer should then be able to complete successfully. You may then perform the following post-install steps:

Decrease the VM’s memory to a more reasonable value (memory balancing on Windows is unstable so keep ``memory`` equal to ``maxmen``).

.. code:: console

      $ qvm-prefs win7new memory 2048
      $ qvm-prefs win7new maxmem 2048



Revert to the standard VGA adapter: the ‘cirrus’ adapter will limit the maximum screen resolution to 1024x768 pixels, while the default VGA adapter allows for much higher resolutions (up to 2560x1600 pixels).

.. code:: console

      $ qvm-features --unset win7new video-model



Finally, increase the VM’s ``qrexec_timeout``: in case you happen to get a BSOD or a similar crash in the VM, utilities like chkdsk won’t complete on restart before qrexec_timeout automatically halts the VM. That can really put the VM in a totally unrecoverable state, whereas with higher qrexec_timeout, chkdsk or the appropriate utility has plenty of time to fix the VM. Note that Qubes Windows Tools also require a larger timeout to move the user profiles to the private volume the first time the VM reboots after the tools’ installation.

.. code:: console

      $ qvm-prefs win7new qrexec_timeout 300



At that point you should have a functional and stable Windows VM, although without updates, Xen’s PV drivers nor Qubes integration (see sections :ref:`Windows Update <user/templates/windows/windows-qubes-4-0:windows update>` and :ref:`Xen PV drivers and Qubes Windows Tools <user/templates/windows/qubes-windows-tools-4-0:xen pv drivers and qubes windows tools>`). It is a good time to clone the VM again.

Windows as a template
---------------------


Windows 7 and 10 can be installed as TemplateVM by selecting

.. code:: console

      $ qvm-create --class TemplateVM --property virt_mode=HVM --property kernel='' --label black Windows-template



when creating the VM. To have the user data stored in AppVMs depending on this template, Windows 7 and 10 have to be treated differently:

- For Windows 7, the option to move the user directories from drive ``C`` to drive ``D`` works and causes any user data to be stored in the AppVMs based on this template, and not in the template itself.

- After installation of Windows 10 as a TemplateVM, the Windows disk manager may be used to add the private volume as disk ``D:``, and you may, using the documented Windows operations, move the user directories ``C:\users\<username>\Documents`` to this new disk, allowing depending AppVMs to have their own private volumes. Moving the hidden application directories ``AppData``, however, is likely to invite trouble - the same trouble that occurs if, during QWT installation, the option ``Move user profiles`` is selected.



For Windows 10, configuration data like those stored in directories like ``AppData`` still remain in the TemplateVM, such that their changes are lost each time the AppVM shuts down. In order to make permanent changes to these configuration data, they have to be changed in the TemplateVM, meaning that applications have to be started there, which violates and perhaps even endangers the security of the TemplateVM. Such changes should be done only if absolutely necessary and with great care. It is a good idea to test them first in a cloned TemplateVM before applying them in the production VM.

AppVMs based on these templates can be created the normal way by using the Qube Manager or by specifying

.. code:: console

      $ qvm-create --class=AppVM --template=<VMname>



On starting the AppVM, sometimes a message is displayed that the Xen PV Network Class needs to restart the system. This message can be safely ignored and closed by selecting “No”.

**Caution:** These AppVMs must not be started while the corresponding TemplateVM is running, because they share the TemplateVM’s license data. Even if this could work sometimes, it would be a violation of the license terms.

Windows 10 Usage According to GDPR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If Windows 10 is used in the EU to process personal data, according to GDPR no automatic data transfer to countries outside the EU is allowed without explicit consent of the person(s) concerned, or other legal consent, as applicable. Since no reliable way is found to completely control the sending of telemetry from Windows 10, the system containing personal data must be completely shielded from the internet.

This can be achieved by installing Windows 10 on a TemplateVM with the user data directory moved to a separate drive (usually ``D:``). Personal data must not be stored within the TemplateVM, but only in AppVMs depending on this TemplateVM. Network access by these AppVMs must be restricted to the local network and perhaps additional selected servers within the EU. Any data exchange of the AppVMs must be restricted to file and clipboard operations to and from other VMs in the same Qubes system.

Windows update
--------------


Depending on how old your installation media is, fully updating your Windows VM may take *hours* (this isn’t specific to Xen/Qubes) so make sure you clone your VM between the mandatory reboots in case something goes wrong. This `comment <https://github.com/QubesOS/qubes-issues/issues/3585#issuecomment-366471111>`__ provides useful links on updating a Windows 7 SP1 VM.

**Note:** if you already have Qubes Windows Tools installed the video adapter in Windows will be “Qubes video driver” and you won’t be able to see the Windows Update process when the VM is being powered off because Qubes services would have been stopped by then. Depending on the size of the Windows update packs it may take a bit of time until the VM shutdowns by itself, leaving one wondering if the VM has crashed or still finalizing the updates (in dom0 a changing CPU usage - eg. shown with ``xentop`` - usually indicates that the VM hasn’t crashed). To avoid guessing the VM’s state enable debugging (``qvm-prefs -s win7new debug true``) and in Windows’ device manager (My computer -> Manage / Device manager / Display adapters) temporarily re-enable the standard VGA adapter and disable “Qubes video driver”. You can disable debugging and revert to Qubes’ display once the VM is updated.

Further customization
---------------------


Please see the `Customizing Windows 7 templates <https://forum.qubes-os.org/t/19005>`__ page (despite the focus on preparing the VM for use as a template, most of the instructions are independent from how the VM will be used - ie. TemplateVM or StandaloneVM).
