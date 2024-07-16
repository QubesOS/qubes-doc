---
lang: it
layout: doc
permalink: /doc/installation-guide/
redirect_from:
- /it/doc/installation-guide/
- /doc/InstallationGuide/
- /wiki/InstallationGuide/
- /doc/InstallationGuideR1/
- /doc/InstallationGuideR2B1/
- /doc/InstallationGuideR2B2/
- /doc/InstallationGuideR2B3/
- /doc/InstallationGuideR2rc1/
- /doc/InstallationGuideR2rc2/
- /doc/InstallationGuideR3.0rc1/
- /doc/InstallationGuideR3.0rc2/
- /doc/live-usb/
- /doc/custom-install/
- /doc/encryption-config/
ref: 153
title: Guida d'installazione
---

Benvenuti alla guida d'installazione di Qubes OS! Questa guida ti guiderà attraverso il processo di installazione di Qubes OS. Ti preghiamo di leggerla attentamente e per intero in quanto contiene informazioni importanti per garantire che l'installazione di Qubes OS sia funzionale e sicura.

## Pre-installazione

### Requisiti Hardware

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Attenzione:</b> Qubes non può sapere cosa è successo sul tuo computer prima della sua installazione. Nessun software può garantire sicurezza se installato su hardware compromesso. Non installare Qubes su computer non affidabili. Vedi <a href="/doc/install-security/">installazione sicura</a> per maggiori informazioni.
</div>

Qubes OS ha [requisiti hardware](/doc/system-requirements/) molto specifici. Per garantire la completa compatibilità, raccomandiamo di utilizzare [hardware Qubes-certified](/doc/certified-hardware/). Hardware diverso potrebbe richiedere particolari configurazioni e attività di troubleshooting. Potrebbe essere utile consultare la [Lista Hardware Compatibile List](/hcl/).

Even on supported hardware, you must ensure that [IOMMU-based virtualization](https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit#Virtualization) is activated in the BIOS or UEFI. Without it, Qubes OS won't be able to enforce isolation. For Intel-based boards, this setting is called Intel Virtualization for Directed I/O (**Intel VT-d**) and for AMD-based boards, it is called  AMD I/O Virtualization Technology (or simply **AMD-Vi**). This parameter should be activated in your computer's BIOS or UEFI, alongside the standard Virtualization (**Intel VT-x**) and AMD Virtualization (**AMD-V**) extensions. This [external guide](https://web.archive.org/web/20200112220913/https://www.intel.in/content/www/in/en/support/articles/000007139/server-products.html) made for Intel-based boards can help you figure out how to enter your BIOS or UEFI to locate and activate those settings. If those settings are not nested under the Advanced tab, you might find them under the Security tab.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> Qubes OS non è pensato per essere installato all'interno di una macchina virtuale quale guest hypervisor. In altre parole, non è supportata la <b>virtualizzazione nidificata</b>. Al fine di garantire l'isolamento Qubes OS deve infatti poter gestire l'hardware in modo diretto.
</div>

### Copiare la ISO sul supporto di installazione

Scegli il computer e il sistema operativo più sicuri a tua disposizione per scaricare e copiare l'ISO di Qubes sul supporto di installazione. [Scarica](/downloads/) la ISO di Qubes.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Attenzione:</b> Qualsiasi file scaricato da Internet potrebbe essere malevole, anche se sembra provenire da una fonte affidabile. La nostra filosofia è <a href="/faq/#what-does-it-mean-to-distrust-the-infrastructure">diffidare dall'infrastruttura</a>. Indipendentemente da come otterrai la ISO di Qubes OS, <a href="/security/verifying-signatures/">verificane la sua autenticità</a> prima di proseguire.
</div>

Una volta verificata l'autenticità della ISO, potrai copiarla su un supporto di installazione a tua scelta tra unità USB, DVD dual-layer o un disco Blu-ray. La dimensione di ogni ISO di Qubes OS è visualizzabile sulla pagina di [download](/downloads/) passando con il mouse sopra al pulsante download. Le istruzioni seguenti si riferiscono alla scelta si un supporto USB quale media di installazione. Se hai scelto un supporto differenze andranno adattate alle tue esigenze.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Nota:</b> There are important <a href="/doc/install-security/">security considerations</a> to keep in mind when choosing an installation medium. Advanced users may wish to <a href="/security/verifying-signatures/#how-to-re-verify-installation-media-after-writing">re-verify their installation media after writing</a>.
</div>

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Attenzione:</b> Porre attenzione alla scelta del dispositivo corretto quando copi l'ISO, altrimenti potresti perdere i dati contenuti nel supporto. Si consiglia di effettuare un backup completo prima di modificare qualsiasi dispositivo.
</div>

#### Linux ISO to USB

On Linux, if you choose to use a USB drive, copy the ISO onto the USB device, e.g. using `dd`:

```
$ sudo dd if=Qubes-RX-x86_64.iso of=/dev/sdY status=progress bs=1048576 conv=fsync
```

Change `Qubes-RX-x86_64.iso` to the filename of the version you're installing, and change `/dev/sdY` to the correct target device e.g., `/dev/sdc`). Make sure to write to the entire device (e.g., `/dev/sdc`) rather than just a single partition (e.g., `/dev/sdc1`).

#### Windows ISO to USB

On Windows, you can use the [Rufus](https://rufus.akeo.ie/) tool to write the ISO to a USB key. Be sure to select "Write in DD Image mode" *after* selecting the Qubes ISO and pressing "START" on the Rufus main window.

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>Note:</b> Using Rufus to create the installation medium means that you <a href="https://github.com/QubesOS/qubes-issues/issues/2051">won't be able</a> to choose the "Test this media and install Qubes OS" option mentioned in the example below. Instead, choose the "Install Qubes OS" option.
</div>

[![Rufus menu](/attachment/doc/rufus-menu.png)](/attachment/doc/rufus-menu.png)

[![Rufus DD image mode](/attachment/doc/rufus-dd-image-mode.png)](/attachment/doc/rufus-dd-image-mode.png)

## Installation

This section will demonstrate a simple installation using mostly default settings.

### Getting to the boot screen

"Booting" is the process of starting your computer. When a computer boots up, it first runs low-level software before the main operating system. Depending on the computer, this low-level software is may be called the ["BIOS"](https://en.wikipedia.org/wiki/BIOS) or ["UEFI"](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface).

Since you're installing Qubes OS, you'll need to access your computer's BIOS or UEFI menu so that you can tell it to boot from the USB drive to which you just copied the Qubes installer ISO.

To begin, power off your computer and plug the USB drive into a USB port, but don't press the power button yet. Right after you press the power button, you'll have to immediately press a specific key to enter the BIOS or UEFI menu. The key to press varies from brand to brand. `Esc`, `Del`, and `F10` are common ones. If you're not sure, you can search the web for `<COMPUTER_MODEL> BIOS key` or `<COMPUTER_MODEL> UEFI key` (replacing `<COMPUTER_MODEL>` with your specific computer model) or look it up in your computer's manual.

Once you know the key to press, press your computer's power button, then repeatedly press that key until you've entered your computer's BIOS or UEFI menu. To give you and idea of what you should be looking for, we've provided a couple of example photos below.

Here's an example of what the BIOS menu looks like on a ThinkPad T430:

[![ThinkPad T430 BIOS menu](/attachment/doc/Thinkpad-t430-bios-main.jpg)](/attachment/doc/Thinkpad-t430-bios-main.jpg)

And here's an example of what a UEFI menu looks like:

[![UEFI menu](/attachment/doc/uefi.jpeg)](/attachment/doc/uefi.jpeg)

Once you access your computer's BIOS or UEFI menu, you'll want to go to the "boot menu," which is where you tell your computer which devices to boot from. The goal is to tell the computer to boot from your USB drive so that you can run the Qubes installer. If your boot menu lets you select which device to boot from first, simply select your USB drive. (If you have multiple entries that all look similar to your USB drive, and you're not sure which one is correct, one option is just to try each one until it works.) If, on the other hand, your boot menu presents you with a list of boot devices in order, then you'll want to move your USB drive to the top so that the Qubes installer runs before anything else.

Once you're done on the boot menu, save your changes. How you do this depends on your BIOS or UEFI, but the instructions should be displayed right there on the screen or in a nearby tab. (If you're not sure whether you've saved your changes correctly, you can always reboot your computer and go back into the boot menu to check whether it still reflects your changes.) Once your BIOS or UEFI is configured the way you want it, reboot your computer. This time, don't press any special keys. Instead, let the BIOS or UEFI load and let your computer boot from your USB drive. If you're successful in this step, after a few seconds you'll be presented with the Qubes installer screen:

[![Boot screen](/attachment/doc/boot-screen-4.2.png)](/attachment/doc/boot-screen-4.2.png)

From here, you can navigate the boot screen using the arrow keys on your keyboard. Pressing the "Tab" key will reveal options. You can choose one of five options:

* Install Qubes OS
* Test this media and install Qubes OS
* Troubleshooting - verbose boot
* Rescue a Qubes OS system
* Install Qubes OS 4.2.1 using kernel-latest
 
Select the option to test this media and install Qubes OS. 

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>Note:</b> If the latest stable release is not compatible with your hardware, you may wish to consider installing using the latest kernel. Be aware that this has not been as well tested as the standard kernel.
</div>

If the boot screen does not appear, there are several options to troubleshoot. First, try rebooting your computer. If it still loads your currently installed operating system or does not detect your installation medium, make sure the boot order is set up appropriately. The process to change the boot order varies depending on the currently installed system and the motherboard manufacturer. If **Windows 10** is installed on your machine, you may need to follow specific instructions to change the boot order. This may require an [advanced reboot](https://support.microsoft.com/en-us/help/4026206/windows-10-find-safe-mode-and-other-startup-settings).

### The installer home screen

On the first screen, you are asked to select the language that will be used during the installation process. When you are done, select **Continue**.

[![Language selection window](/attachment/doc/welcome-to-qubes-os-installation-screen-4.2.png)](/attachment/doc/welcome-to-qubes-os-installation-screen-4.2.png)

Prior to the next screen, a compatibility test runs to check whether IOMMU-virtualization is active or not. If the test fails, a window will pop up. 

[![Unsupported hardware detected](/attachment/doc/unsupported-hardware-detected.png)](/attachment/doc/unsupported-hardware-detected.png)

Do not panic. It may simply indicate that IOMMU-virtualization hasn't been activated in the BIOS or UEFI. Return to the [hardware requirements](#hardware-requirements) section to learn how to activate it. If the setting is not configured correctly, it means that your hardware won't be able to leverage some Qubes security features, such as a strict isolation of the networking and USB hardware. 

If the test passes, you will reach the installation summary screen. The installer loads Xen right at the beginning. If you can see the installer's graphical screen, and you pass the compatibility check that runs immediately afterward, Qubes OS is likely to work on your system!

Like Fedora, Qubes OS uses the Anaconda installer. Those that are familiar with RPM-based distributions should feel at home. 

### Installation summary

<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>Did you know?</b> The Qubes OS installer is completely offline. It doesn't even load any networking drivers, so there is no possibility of internet-based data leaks or attacks during the installation process.
</div>

The Installation summary screen allows you to change how the system will be installed and configured, including localization settings. At minimum, you are required to select the storage device on which Qubes OS will be installed. 

[![Installation summary screen awaiting input ](/attachment/doc/installation-summary-not-ready-4.2.png)](/attachment/doc/installation-summary-not-ready-4.2.png)

### Localization

Let's assume you wish to add a German keyboard layout. Go to Keyboard Layout, press the "Plus" symbol, search for "German" as indicated in the screenshot and press "Add". If you want it be your default language, select the "German" entry in the list and press the arrow button. Click on "Done" in the upper left corner, and you're ready to go!

[![Keyboard layout selection](/attachment/doc/keyboard-layout-selection.png)](/attachment/doc/keyboard-layout-selection.png)

The process to select a new language is similar to the process to select a new keyboard layout. Follow the same process in the "Language Support" entry.

[![Language support selection](/attachment/doc/language-support-selection.png)](/attachment/doc/language-support-selection.png)

You can have as many keyboard layout and languages as you want. Post-install, you will be able to switch between them and install others. 

Don't forget to select your time and date by clicking on the Time & Date entry.

[![Time and date](/attachment/doc/time-and-date.png)](/attachment/doc/time-and-date.png)
### Installation destination

Under the System section, you must choose the installation destination. Select the storage device on which you would like to install Qubes OS.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Be careful to choose the correct installation target, or you may lose data. We strongly recommended making a full backup before proceeding.
</div>

Your installation destination can be an internal or external storage drive, such as an SSD, HDD, or USB drive. The installation destination must have a least 32 GiB of free space available.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> The installation destination cannot be the same as the installation medium. For example, if you're installing Qubes OS <em>from</em> a USB drive <em>onto</em> a USB drive, they must be two distinct USB drives, and they must both be plugged into your computer at the same time. (Note: This may not apply to advanced users who partition their devices appropriately.)
</div>

Installing an operating system onto a USB drive can be a convenient way to try Qubes. However, USB drives are typically much slower than internal SSDs. We recommend a very fast USB 3.0 drive for decent performance. Please note that a minimum storage of 32 GiB is required. If you want to install Qubes OS onto a USB drive, just select the USB device as the target installation device. Bear in mind that the installation process is likely to take longer than it would on an internal storage device.

[![Select storage device screen](/attachment/doc/select-storage-device-4.2.png)](/attachment/doc/select-storage-device-4.2.png)

<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>Did you know?</b> By default, Qubes OS uses <a href="https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup">LUKS</a>/<a href="https://en.wikipedia.org/wiki/Dm-crypt">dm-crypt</a> to encrypt everything except the <code>/boot</code> partition.
</div>

As soon as you press **Done**, the installer will ask you to enter a passphrase for disk encryption. The passphrase should be complex. Make sure that your keyboard layout reflects what keyboard you are actually using. When you're finished, press **Done**.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> If you forget your encryption passphrase, there is no way to recover it.
</div>

[![Select storage passphrase](/attachment/doc/select-storage-passphrase.png)](/attachment/doc/select-storage-passphrase.png)

### Create your user account

Select "User Creation" to create your user account. This is what you'll use to log in after disk decryption and when unlocking the screen locker. This is a purely local, offline account in dom0. By design, Qubes OS is a single-user operating system, so this is just for you.

The new user you create has full administrator privileges and is protected by a password. Just as for the disk encryption, this password should be complex. The root account is deactivated and should remain as such.

[![Account name and password creation window. ](/attachment/doc/account-name-and-password-4.2.png)](/attachment/doc/account-name-and-password-4.2.png)

### Installation
When you have completed all the items marked with the warning icon, press **Begin Installation**.

Installation can take some time. 
[![Windows showing installation complete and Reboot button. ](/attachment/doc/installation-complete-4.2.png)](/attachment/doc/installation-complete-4.2.png)
When the installation is complete, press **Reboot System**. Don't forget to remove the installation medium, or else you may end up seeing the installer boot screen again.

## Post-installation

### First boot

If the installation was successful, you should now see the GRUB menu during the boot process.

[![Grub boot menu](/attachment/doc/grub-boot-menu.png)](/attachment/doc/grub-boot-menu.png)

Just after this screen, you will be asked to enter your encryption passphrase.

[![Screen to enter device decryption password](/attachment/doc/unlock-storage-device-screen-4.2.png)](/attachment/doc/unlock-storage-device-screen-4.2.png)

### Initial Setup

You're almost done. Before you can start using Qubes OS, some configuration is needed. 

[![Window with link for final configuration ](/attachment/doc/initial-setup-menu-4.2.png)](/attachment/doc/initial-setup-menu-4.2.png)
Click on the item marked with the warning triangle to enter the configuration screen.
[![Initial configuration menu](/attachment/doc/initial-setup-menu-configuration-4.2.png)](/attachment/doc/initial-setup-menu-configuration-4.2.png)

By default, the installer will create a number of qubes (depending on the options you selected during the installation process). These are designed to give you a more ready-to-use environment from the get-go.

Let's briefly go over the options:

* **Templates Configuration:** Here you can decide which [templates](../templates/) you want to have installed, and which will be the default template.
* **Create default system qubes:** These are the core components of the system, required for things like internet access. You can opt to have some created as [disposables](../glossary#disposable)
* **Create default application qubes:** These are how you compartmentalize your digital life. There's nothing special about the ones the installer creates. They're just suggestions that apply to most people. If you decide you don't want them, you can always delete them later, and you can always create your own.
* **Use a qube to hold all USB controllers:** Just like the network qube for the network stack, the USB qube isolates the USB controllers.
  * **Use sys-net qube for both networking and USB devices:** You should select this option if you rely on a USB device for network access, such as a USB modem or a USB Wi-Fi adapter.
* **Create Whonix Gateway and Workstation qubes:** If you want to use [Whonix](https://www.whonix.org/wiki/Qubes), you should select this option.
  * **Enabling system and template updates over the Tor anonymity network using Whonix:** If you select this option, then whenever you install or update software in dom0 or a template, the internet traffic will go through Tor.
* **Do not configure anything:** This is for very advanced users only. If you select this option, you will have to manually set up everything.

When you're satisfied with your choices, press **Done**. This configuration process may take a while, depending on the speed and compatibility of your system.

After configuration is done, you will be greeted by the login screen. Enter your password and log in.

[![Login screen](/attachment/doc/login-screen.png)](/attachment/doc/login-screen.png)

Congratulations, you are now ready to use Qubes OS!

[![Desktop menu](/attachment/doc/desktop-menu.png)](/attachment/doc/desktop-menu.png)

## Next steps

### Updating

Next, [update](/doc/how-to-update/) your installation to ensure you have the latest security updates. Frequently updating is one of the best ways to remain secure against new threats.

### Security

The Qubes OS Project occasionally issues [Qubes Security Bulletins (QSBs)](/security/qsb/) as part of the [Qubes Security Pack (qubes-secpack)](/security/pack/). It is important to make sure that you receive all QSBs in a timely manner so that you can take action to keep your system secure. (While [updating](#updating) will handle most security needs, there may be cases in which additional action from you is required.) For this reason, we strongly recommend that every Qubes user subscribe to the [qubes-announce](/support/#qubes-announce) mailing list.

In addition to QSBs, the Qubes OS Project also publishes [Canaries](/security/canary/), XSA summaries, template releases and end-of-life notices, and other items of interest to Qubes users. Since these are not essential for all Qubes users to read, they are not sent to [qubes-announce](/support/#qubes-announce) in order to keep the volume on that list low. However, we expect that most users, especially novice users, will find them helpful. If you are interested in these additional items, we encourage you to subscribe to the [Qubes News RSS feed](/feed.xml) or join one of our other [venues](/support/), where these news items are also announced.

For more information about Qubes OS Project security, please see the [security center](/security/).

### Backup
E' estremamente importante eseguire backup regolari al fine di non perdere dati inaspettatamente. Il [Qubes backup system](/doc/how-to-back-up-restore-and-migrate/) ti consente di fare in modo semplice e sicuro.

### Submit your HCL report

Consider giving back to the Qubes community and helping other users by [generating and submitting a Hardware Compatibility List (HCL) report](/doc/how-to-use-the-hcl/#generating-and-submitting-new-reports).

### Per iniziare

Find out [Getting Started](/doc/getting-started/) with Qubes, check out the other [How-To Guides](/doc/#how-to-guides), and learn about [Templates](/doc/#templates).

## Getting help

* We work very hard to make the [documentation](/doc/) accurate, comprehensive useful and user friendly. We urge you to read it! It may very well contain the answers to your questions. (Since the documentation is a community effort, we'd also greatly appreciate your help in [improving](/doc/how-to-edit-the-documentation/) it!)

* If issues arise during installation, see the [Installation Troubleshooting](/doc/installation-troubleshooting) guide. 

* If you don't find your answer in the documentation, please see [Help, Support, Mailing Lists, and Forum](/support/) for places to ask.

* Si prega di **non** inviare email individuali ai membri del team di Qube con domande sull'installazione o altri problemi. Consultate, invece [Aiuto, Supporto, Mailing Lists e Forum](/support/) for appropriate places to ask questions.

