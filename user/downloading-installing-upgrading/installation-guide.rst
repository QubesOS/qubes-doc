==================
Installation guide
==================


Welcome to the Qubes OS installation guide! This guide will walk you through the process of installing Qubes. Please read it carefully and thoroughly, as it contains important information for ensuring that your Qubes OS installation is functional and secure.

Pre-installation
----------------


Hardware requirements
^^^^^^^^^^^^^^^^^^^^^


.. DANGER::
      
      **Warning:** Qubes has no control over what happens on your computer before you install it. No software can provide security if it is installed on compromised hardware. Do not install Qubes on a computer you don’t trust. See :doc:`installation security </user/downloading-installing-upgrading/install-security>`       for more information.

Qubes OS has very specific :doc:`system requirements </user/hardware/system-requirements>`. To ensure compatibility, we strongly recommend using :doc:`Qubes-certified hardware </user/hardware/certified-hardware/certified-hardware>`. Other hardware may require you to perform significant troubleshooting. You may also find it helpful to consult the :website:`Hardware Compatibility List <hcl/>`.

Even on supported hardware, you must ensure that :wikipedia:`IOMMU-based virtualization <Input%E2%80%93output_memory_management_unit#Virtualization>` is activated in the BIOS or UEFI. Without it, Qubes OS won’t be able to enforce isolation. For Intel-based boards, this setting is called Intel Virtualization for Directed I/O (**Intel VT-d**) and for AMD-based boards, it is called AMD I/O Virtualization Technology (or simply **AMD-Vi**). This parameter should be activated in your computer’s BIOS or UEFI, alongside the standard Virtualization (**Intel VT-x**) and AMD Virtualization (**AMD-V**) extensions. This `external guide <https://web.archive.org/web/20200112220913/https://www.intel.in/content/www/in/en/support/articles/000007139/server-products.html>`__ made for Intel-based boards can help you figure out how to enter your BIOS or UEFI to locate and activate those settings. If those settings are not nested under the Advanced tab, you might find them under the Security tab.

.. warning::
      
      **Note:** Qubes OS is not meant to be installed inside a virtual machine as a guest hypervisor. In other words, *nested virtualization* is not supported. In order for a strict compartmentalization to be enforced, Qubes OS needs to be able to manage the hardware directly.

Copying the ISO onto the installation medium
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Pick the most secure existing computer and OS you have available for downloading and copying the Qubes ISO onto the installation medium. :website:`Download <downloads/>` a Qubes ISO. If your Internet connection is unstable and the download is interrupted, you could resume the partial download with ``wget --continue`` in case you are currently using wget for downloading or use a download-manager with resume capability. Alternatively you can download installation ISO via BitTorrent that sometimes enables higher download speeds and more reliable downloads of large files.

.. DANGER::
      
      **Warning:** Any file you download from the internet could be malicious, even if it appears to come from a trustworthy source. Our philosophy is to :ref:`distrust the infrastructure <introduction/faq:what does it mean to "distrust the infrastructure"?>`      . Regardless of how you acquire your Qubes ISO, :doc:`verify its authenticity </project-security/verifying-signatures>`       before continuing.

Once the ISO has been verified as authentic, you should copy it onto the installation medium of your choice, such as a USB drive, dual-layer DVD, or Blu-ray disc. The size of each Qubes ISO is available on the :website:`downloads <downloads/>` page by hovering over the download button. The instructions below assume you’ve chosen a USB drive as your medium. If you’ve chosen a different medium, please adapt the instructions accordingly.

.. warning::
      
      **Note:** There are important :doc:`security considerations </user/downloading-installing-upgrading/install-security>`       to keep in mind when choosing an installation medium. Advanced users may wish to :ref:`re-verify their installation media after writing <project-security/verifying-signatures:how to re-verify installation media after writing>`      .

.. DANGER::
      
      **Warning:** Be careful to choose the correct device when copying the ISO, or you may lose data. We strongly recommended making a full backup before modifying any devices.

Linux ISO to USB
^^^^^^^^^^^^^^^^


On Linux, if you choose to use a USB drive, copy the ISO onto the USB device, e.g. using ``dd``:

.. code:: bash

      $ sudo dd if=Qubes-RX-x86_64.iso of=/dev/sdY status=progress bs=1048576 conv=fsync



Change ``Qubes-RX-x86_64.iso`` to the filename of the version you’re installing, and change ``/dev/sdY`` to the correct target device e.g., ``/dev/sdc``). Make sure to write to the entire device (e.g., ``/dev/sdc``) rather than just a single partition (e.g., ``/dev/sdc1``).

Windows ISO to USB
^^^^^^^^^^^^^^^^^^


On Windows, you can use the `Rufus <https://rufus.ie/>`__ tool to write the ISO to a USB key. Be sure to select “Write in DD Image mode” *after* selecting the Qubes ISO and pressing “START” on the Rufus main window.

.. note::
      
      **Note:** Using Rufus to create the installation medium means that you :issue:`won’t be able <2051>`       to choose the “Test this media and install Qubes OS” option mentioned in the example below. Instead, choose the “Install Qubes OS” option.

|Rufus menu|

|Rufus DD image mode|

Installation
------------


This section will demonstrate a simple installation using mostly default settings.

Getting to the boot screen
^^^^^^^^^^^^^^^^^^^^^^^^^^


“Booting” is the process of starting your computer. When a computer boots up, it first runs low-level software before the main operating system. Depending on the computer, this low-level software may be called the :wikipedia:`“BIOS” <BIOS>` or :wikipedia:`“UEFI” <Unified_Extensible_Firmware_Interface>`.

Since you’re installing Qubes OS, you’ll need to access your computer’s BIOS or UEFI menu so that you can tell it to boot from the USB drive to which you just copied the Qubes installer ISO.

To begin, power off your computer and plug the USB drive into a USB port, but don’t press the power button yet. Right after you press the power button, you’ll have to immediately press a specific key to enter the BIOS or UEFI menu. The key to press varies from brand to brand. ``Esc``, ``Del``, and ``F10`` are common ones. If you’re not sure, you can search the web for ``<COMPUTER_MODEL> BIOS key`` or ``<COMPUTER_MODEL> UEFI key`` (replacing ``<COMPUTER_MODEL>`` with your specific computer model) or look it up in your computer’s manual.

Once you know the key to press, press your computer’s power button, then repeatedly press that key until you’ve entered your computer’s BIOS or UEFI menu. To give you an idea of what you should be looking for, we’ve provided a couple of example photos below.

Here’s an example of what the BIOS menu looks like on a ThinkPad T430:

|ThinkPad T430 BIOS menu|

And here’s an example of what a modern UEFI menu looks like:

|UEFI menu|

Once you access your computer’s BIOS or UEFI menu, you’ll want to go to the “boot menu”, which is where you tell your computer which devices to boot from. The goal is to tell the computer to boot from your USB drive so that you can run the Qubes installer. If your boot menu lets you select which device to boot from first, simply select your USB drive. (If you have multiple entries that all look similar to your USB drive, and you’re not sure which one is correct, one option is just to try each one until it works.) If, on the other hand, your boot menu presents you with a list of boot devices in order, then you’ll want to move your USB drive to the top so that the Qubes installer runs before anything else.

Then, if you are on a computer using UEFI, you’ll have to disable `Secure Boot <https://en.m.wikipedia.org/wiki/UEFI#SECURE-BOOT>`__ to allow Qubes OS to boot.

Once you’re done with the settings, save your changes. How you do this depends on your BIOS or UEFI, but the instructions should be displayed right there on the screen or in a nearby tab. (If you’re not sure whether you’ve saved your changes correctly, you can always reboot your computer and go back into the boot menu to check whether it still reflects your changes.) Once your BIOS or UEFI is configured the way you want it, reboot your computer. This time, don’t press any special keys. Instead, let the BIOS or UEFI load and let your computer boot from your USB drive. If you’re successful in this step, after a few seconds you’ll be presented with the Qubes installer screen:

|Boot screen|

From here, you can navigate the boot screen using the arrow keys on your keyboard. Pressing the “Tab” key will reveal options. You can choose one of five options:

- Install Qubes OS

- Test this media and install Qubes OS

- Troubleshooting - verbose boot

- Rescue a Qubes OS system

- Install Qubes OS 4.2.1 using kernel-latest



Select the option to test this media and install Qubes OS.

.. note::
      
      **Note:** If the latest stable release is not compatible with your hardware, you may wish to consider installing using the latest kernel. Be aware that this has not been as well tested as the standard kernel.

If the boot screen does not appear, there are several options to troubleshoot. First, try rebooting your computer. If it still loads your currently installed operating system or does not detect your installation medium, make sure the boot order is set up appropriately. The process to change the boot order varies depending on the currently installed system and the motherboard manufacturer. If **Windows 10** is installed on your machine, you may need to follow specific instructions to change the boot order. This may require an `advanced reboot <https://support.microsoft.com/en-us/help/4026206/windows-10-find-safe-mode-and-other-startup-settings>`__.

The installer home screen
^^^^^^^^^^^^^^^^^^^^^^^^^


On the first screen, you are asked to select the language that will be used during the installation process. When you are done, select **Continue**.

|Language selection window|

Prior to the next screen, a compatibility test runs to check whether IOMMU-virtualization is active or not. If the test fails, a window will pop up.

|Unsupported hardware detected|

Do not panic. It may simply indicate that IOMMU-virtualization hasn’t been activated in the BIOS or UEFI. Return to the `hardware requirements <#hardware-requirements>`__ section to learn how to activate it. If the setting is not configured correctly, it means that your hardware won’t be able to leverage some Qubes security features, such as a strict isolation of the networking and USB hardware.

If the test passes, you will reach the installation summary screen. The installer loads Xen right at the beginning. If you can see the installer’s graphical screen, and you pass the compatibility check that runs immediately afterward, Qubes OS is likely to work on your system!

Like Fedora, Qubes OS uses the Anaconda installer. Those that are familiar with RPM-based distributions should feel at home.

Installation summary
^^^^^^^^^^^^^^^^^^^^


.. note::
      
      **Did you know?** The Qubes OS installer is completely offline. It doesn’t even load any networking drivers, so there is no possibility of internet-based data leaks or attacks during the installation process.

The Installation summary screen allows you to change how the system will be installed and configured, including localization settings. At minimum, you are required to select the storage device on which Qubes OS will be installed.

|Installation summary screen awaiting input|

Localization
^^^^^^^^^^^^


Let’s assume you wish to add a German keyboard layout. Go to Keyboard Layout, press the “Plus” symbol, search for “German” as indicated in the screenshot and press “Add”. If you want it be your default language, select the “German” entry in the list and press the arrow button. Click on “Done” in the upper left corner, and you’re ready to go!

|Keyboard layout selection|

The process to select a new language is similar to the process to select a new keyboard layout. Follow the same process in the “Language Support” entry.

|Language support selection|

You can have as many keyboard layout and languages as you want. Post-install, you will be able to switch between them and install others.

Don’t forget to select your time and date by clicking on the Time & Date entry.

|Time and date|

Installation destination
^^^^^^^^^^^^^^^^^^^^^^^^


Under the System section, you must choose the installation destination. Select the storage device on which you would like to install Qubes OS.

.. DANGER::
      
      **Warning:** Be careful to choose the correct installation target, or you may lose data. We strongly recommended making a full backup before proceeding.

Your installation destination can be an internal or external storage drive, such as an SSD, HDD, or USB drive. The installation destination must have a least 32 GiB of free space available.

.. warning::
      
      **Note:** The installation destination cannot be the same as the installation medium. For example, if you’re installing Qubes OS *from* a USB drive *onto* a USB drive, they must be two distinct USB drives, and they must both be plugged into your computer at the same time. (**Note:** This may not apply to advanced users who partition their devices appropriately.)

Installing an operating system onto a USB drive can be a convenient way to try Qubes. However, USB drives are typically much slower than internal SSDs. We recommend a very fast USB 3.0 drive for decent performance. Please note that a minimum storage of 32 GiB is required. If you want to install Qubes OS onto a USB drive, just select the USB device as the target installation device. Bear in mind that the installation process is likely to take longer than it would on an internal storage device.

|Select storage device screen|

.. note::
      
      **Did you know?** By default, Qubes OS uses :wikipedia:`LUKS <Linux_Unified_Key_Setup>`      /:wikipedia:`dm-crypt <Dm-crypt>`       to encrypt everything except the ``/boot`` partition.

As soon as you press **Done**, the installer will ask you to enter a passphrase for disk encryption. The passphrase should be complex. Make sure that your keyboard layout reflects what keyboard you are actually using. When you’re finished, press **Done**.

.. DANGER::
      
      **Warning:** If you forget your encryption passphrase, there is no way to recover it.

|Select storage passphrase|

Create your user account
^^^^^^^^^^^^^^^^^^^^^^^^


Select “User Creation” to create your user account. This is what you’ll use to log in after disk decryption and when unlocking the screen locker. This is a purely local, offline account in dom0. By design, Qubes OS is a single-user operating system, so this is just for you.

The new user you create has full administrator privileges and is protected by a password. Just as for the disk encryption, this password should be complex. The root account is deactivated and should remain as such.

|Account name and password creation window.|

.. _installation-1:


Installation
^^^^^^^^^^^^




When you have completed all the items marked with the warning icon, press **Begin Installation**.

Installation can take some time. |Windows showing installation complete and Reboot button.| When the installation is complete, press **Reboot System**. Don’t forget to remove the installation medium, or else you may end up seeing the installer boot screen again.

Post-installation
-----------------


First boot
^^^^^^^^^^


If the installation was successful, you should now see the GRUB menu during the boot process.

|Grub boot menu|

Just after this screen, you will be asked to enter your encryption passphrase.

|Screen to enter device decryption password|

Initial Setup
^^^^^^^^^^^^^


You’re almost done. Before you can start using Qubes OS, some configuration is needed.

|Window with link for final configuration| Click on the item marked with the warning triangle to enter the configuration screen. |Initial configuration menu|

By default, the installer will create a number of qubes (depending on the options you selected during the installation process). These are designed to give you a more ready-to-use environment from the get-go.

Let’s briefly go over the options:

- **Templates Configuration:** Here you can decide which :doc:`templates </user/templates/templates>` you want to have installed, and which will be the default template.

- **Create default system qubes:** These are the core components of the system, required for things like internet access. You can opt to have some created as :ref:`disposables <user/reference/glossary:disposable>`.

- **Create default application qubes:** These are how you compartmentalize your digital life. There’s nothing special about the ones the installer creates. They’re just suggestions that apply to most people. If you decide you don’t want them, you can always delete them later, and you can always create your own.

- **Use a qube to hold all USB controllers:** Just like the network qube for the network stack, the USB qube isolates the USB controllers.

  - **Use sys-net qube for both networking and USB devices:** You should select this option if you rely on a USB device for network access, such as a USB modem or a USB Wi-Fi adapter.



- **Create Whonix Gateway and Workstation qubes:** If you want to use `Whonix <https://www.whonix.org/wiki/Qubes>`__, you should select this option.

  - **Enabling system and template updates over the Tor anonymity network using Whonix:** If you select this option, then whenever you install or update software in dom0 or a template, the internet traffic will go through Tor.



- **Do not configure anything:** This is for very advanced users only. If you select this option, you will have to manually set up everything.



When you’re satisfied with your choices, press **Done**. This configuration process may take a while, depending on the speed and compatibility of your system.

After configuration is done, you will be greeted by the login screen. Enter your password and log in.

|Login screen|

Congratulations, you are now ready to use Qubes OS!

|Desktop menu|

Next steps
----------


Updating
^^^^^^^^


Next, :doc:`update </user/how-to-guides/how-to-update>` your installation to ensure you have the latest security updates. Frequently updating is one of the best ways to remain secure against new threats.

Security
^^^^^^^^


The Qubes OS Project occasionally issues :website:`Qubes Security Bulletins (QSBs) <security/qsb/>` as part of the :doc:`Qubes Security Pack (qubes-secpack) </project-security/security-pack>`. It is important to make sure that you receive all QSBs in a timely manner so that you can take action to keep your system secure. (While `updating <#updating>`__ will handle most security needs, there may be cases in which additional action from you is required.) For this reason, we strongly recommend that every Qubes user subscribe to the :ref:`qubes-announce <introduction/support:qubes-announce>` mailing list.

In addition to QSBs, the Qubes OS Project also publishes :website:`Canaries <security/canary/>`, XSA summaries, template releases and end-of-life notices, and other items of interest to Qubes users. Since these are not essential for all Qubes users to read, they are not sent to :ref:`qubes-announce <introduction/support:qubes-announce>` in order to keep the volume on that list low. However, we expect that most users, especially novice users, will find them helpful. If you are interested in these additional items, we encourage you to subscribe to the :website:`Qubes News RSS feed <feed.xml>` or join one of our other :doc:`venues </introduction/support>`, where these news items are also announced.

For more information about Qubes OS Project security, please see the :doc:`security center </project-security/security>`.

Backups
^^^^^^^


It is extremely important to make regular backups so that you don’t lose your data unexpectedly. The :doc:`Qubes backup system </user/how-to-guides/how-to-back-up-restore-and-migrate>` allows you to do this securely and easily.

Submit your HCL report
^^^^^^^^^^^^^^^^^^^^^^


Consider giving back to the Qubes community and helping other users by :ref:`generating and submitting a Hardware Compatibility List (HCL) report <user/hardware/how-to-use-the-hcl:generating and submitting new reports>`.

Get Started
^^^^^^^^^^^


Find out :doc:`Getting Started </introduction/getting-started>` with Qubes, check out the other :ref:`How-To Guides <how-to-guides>`, and learn about :ref:`Templates <templates>`.

Getting help
------------


- We work very hard to make the :doc:`documentation </index>` accurate, comprehensive useful and user friendly. We urge you to read it! It may very well contain the answers to your questions. (Since the documentation is a community effort, we’d also greatly appreciate your help in :website:`improving <doc/how-to-edit-the-documentation/>` it!)

- If issues arise during installation, see the :doc:`Installation Troubleshooting </user/troubleshooting/installation-troubleshooting>` guide.

- If you don’t find your answer in the documentation, please see :doc:`Help, Support, Mailing Lists, and Forum </introduction/support>` for places to ask.

- Please do **not** email individual members of the Qubes team with questions about installation or other problems. Instead, please see :doc:`Help, Support, Mailing Lists, and Forum </introduction/support>` for appropriate places to ask questions.



.. |Rufus menu| image:: /attachment/doc/rufus-menu.png
   

.. |Rufus DD image mode| image:: /attachment/doc/rufus-dd-image-mode.png
   

.. |ThinkPad T430 BIOS menu| image:: /attachment/doc/Thinkpad-t430-bios-main.jpg
   

.. |UEFI menu| image:: /attachment/doc/uefi.jpeg
   

.. |Boot screen| image:: /attachment/doc/boot-screen-4.2.png
   

.. |Language selection window| image:: /attachment/doc/welcome-to-qubes-os-installation-screen-4.2.png
   

.. |Unsupported hardware detected| image:: /attachment/doc/unsupported-hardware-detected.png
   

.. |Installation summary screen awaiting input| image:: /attachment/doc/installation-summary-not-ready-4.2.png
   

.. |Keyboard layout selection| image:: /attachment/doc/keyboard-layout-selection.png
   

.. |Language support selection| image:: /attachment/doc/language-support-selection.png
   

.. |Time and date| image:: /attachment/doc/time-and-date.png
   

.. |Select storage device screen| image:: /attachment/doc/select-storage-device-4.2.png
   

.. |Select storage passphrase| image:: /attachment/doc/select-storage-passphrase.png
   

.. |Account name and password creation window.| image:: /attachment/doc/account-name-and-password-4.2.png
   

.. |Windows showing installation complete and Reboot button.| image:: /attachment/doc/installation-complete-4.2.png
   

.. |Grub boot menu| image:: /attachment/doc/grub-boot-menu.png
   

.. |Screen to enter device decryption password| image:: /attachment/doc/unlock-storage-device-screen-4.2.png
   

.. |Window with link for final configuration| image:: /attachment/doc/initial-setup-menu-4.2.png
   

.. |Initial configuration menu| image:: /attachment/doc/initial-setup-menu-configuration-4.2.png
   

.. |Login screen| image:: /attachment/doc/login-screen.png
   

.. |Desktop menu| image:: /attachment/doc/desktop-menu.png
   
