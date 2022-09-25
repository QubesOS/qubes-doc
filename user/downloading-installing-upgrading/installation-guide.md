---
lang: en
layout: doc
permalink: /doc/installation-guide/
redirect_from:
- /en/doc/installation-guide/
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
ref: 153
title: Installation guide
---

Welcome to the Qubes OS installation guide! This guide will walk you through
the process of installing Qubes. Please read it carefully and thoroughly, as it
contains important information for ensuring that your Qubes OS installation is
functional and secure.

## Pre-installation

### Hardware requirements

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Qubes has no control over what happens on your computer
  before you install it. No software can provide security if it is installed on
  compromised hardware. Do not install Qubes on a computer you don't trust.
  See <a href="/doc/install-security/">installation security</a> for more
  information.
</div>

Qubes OS has very specific [system requirements](/doc/system-requirements/). To
ensure compatibility, we strongly recommend using [Qubes-certified hardware](/doc/certified-hardware/). Other hardware may require you to perform
significant troubleshooting. You may also find it helpful to consult the
[Hardware Compatibility List](/hcl/).

Even on supported hardware, you must ensure that [IOMMU-based virtualization](https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit#Virtualization)
is activated in the BIOS or UEFI. Without it, Qubes OS won't be able to enforce
isolation. For Intel-based boards, this setting is called Intel Virtualization
for Directed I/O (**Intel VT-d**) and for AMD-based boards, it is called  AMD
I/O Virtualization Technology (or simply **AMD-Vi**). This parameter should be
activated in your computer's BIOS or UEFI, alongside the standard
Virtualization (**Intel VT-x**) and AMD Virtualization (**AMD-V**) extensions.
This [external guide](https://web.archive.org/web/20200112220913/https://www.intel.in/content/www/in/en/support/articles/000007139/server-products.html)
made for Intel-based boards can help you figure out how to enter your BIOS or
UEFI to locate and activate those settings. If those settings are not nested
under the Advanced tab, you might find them under the Security tab.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> Qubes OS is not meant to be installed inside a virtual machine
  as a guest hypervisor. In other words, <b>nested virtualization</b> is not
  supported. In order for a strict compartmentalization to be enforced, Qubes
  OS needs to be able to manage the hardware directly.
</div>

### Copying the ISO onto the installation medium

Pick the most secure existing computer and OS you have available for
downloading and copying the Qubes ISO onto the installation medium.
[Download](/downloads/) a Qubes ISO.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Any file you download from the internet could be malicious,
  even if it appears to come from a trustworthy source. Our philosophy is to <a
  href="/faq/#what-does-it-mean-to-distrust-the-infrastructure">distrust the
  infrastructure</a>. Regardless of how you acquire your Qubes ISO, <a
  href="/security/verifying-signatures/">verify its authenticity</a> before
  continuing.
</div>

Once the ISO has been verified as authentic, you should copy it onto the
installation medium of your choice, such as a USB drive, dual-layer DVD,
or Blu-ray disc. The size of each Qubes ISO is available on the
[downloads](/downloads/) page by hovering over the download button. The
instructions below assume you've chosen a USB drive as your medium. If you've
chosen a different medium, please adapt the instructions accordingly.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> There are important <a href="/doc/install-security/">security
  considerations</a> to keep in mind when choosing an installation medium.
  Advanced users may wish to <a
  href="/security/verifying-signatures/#how-to-re-verify-installation-media-after-writing">re-verify
  their installation media after writing</a>.
</div>

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Be careful to choose the correct device when copying the ISO,
  or you may lose data. We strongly recommended making a full backup before
  modifying any devices.
</div>

#### Linux ISO to USB

On Linux, if you choose to use a USB drive, copy the ISO onto the USB device,
e.g. using `dd`:

```
$ sudo dd if=Qubes-RX-x86_64.iso of=/dev/sdY status=progress bs=1048576 conv=fsync
```

Change `Qubes-RX-x86_64.iso` to the filename of the version you're installing,
and change `/dev/sdY` to the correct target device e.g., `/dev/sdc`). Make sure
to write to the entire device (e.g., `/dev/sdc`) rather than just a single
partition (e.g., `/dev/sdc1`).

#### Windows ISO to USB

On Windows, you can use the [Rufus](https://rufus.akeo.ie/) tool to write the
ISO to a USB key. Be sure to select "Write in DD Image mode" *after* selecting
the Qubes ISO and pressing "START" on the Rufus main window.

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>Note:</b> Using Rufus to create the installation medium means that you
  <a href="https://github.com/QubesOS/qubes-issues/issues/2051">won't be able</a>
  to choose the "Test this media and install Qubes OS" option mentioned in the
  example below. Instead, choose the "Install Qubes OS" option.
</div>

[![Rufus menu](/attachment/doc/rufus-menu.png)](/attachment/doc/rufus-menu.png)

[![Rufus DD image mode](/attachment/doc/rufus-dd-image-mode.png)](/attachment/doc/rufus-dd-image-mode.png)

## Installation

This section will demonstrate a simple installation using mostly default
settings.

If you are an advanced user, and you would like to customize your installation,
please see [custom installation](/doc/custom-install/). Otherwise, follow the
instructions below.

### Getting to the boot screen

"Booting" is the process of starting your computer. When a computer boots up,
it first runs low-level software before the main operating system. Depending on
the computer, this low-level software is may be called the
["BIOS"](https://en.wikipedia.org/wiki/BIOS) or
["UEFI"](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface).

Since you're installing Qubes OS, you'll need to access your computer's BIOS or
UEFI menu so that you can tell it to boot from the USB drive to which you just
copied the Qubes installer ISO.

To begin, power off your computer and plug the USB drive into a USB port, but
don't press the power button yet. Right after you press the power button,
you'll have to immediately press a specific key to enter the BIOS or UEFI menu.
The key to press varies from brand to brand. `Esc`, `Del`, and `F10` are common
ones. If you're not sure, you can search the web for `<COMPUTER_MODEL> BIOS
key` or `<COMPUTER_MODEL> UEFI key` (replacing `<COMPUTER_MODEL>` with your
specific computer model) or look it up in your computer's manual.

Once you know the key to press, press your computer's power button, then
repeatedly press that key until you've entered your computer's BIOS or UEFI
menu. To give you and idea of what you should be looking for, we've provided a
couple of example photos below.

Here's an example of what the BIOS menu looks like on a ThinkPad T430:

[![ThinkPad T430 BIOS menu](/attachment/doc/Thinkpad-t430-bios-main.jpg)](/attachment/doc/Thinkpad-t430-bios-main.jpg)

And here's an example of what a UEFI menu looks like:

[![UEFI menu](/attachment/doc/uefi.jpeg)](/attachment/doc/uefi.jpeg)

Once you access your computer's BIOS or UEFI menu, you'll want to go to the
"boot menu," which is where you tell your computer which devices to boot from.
The goal is to tell the computer to boot from your USB drive so that you can
run the Qubes installer. If your boot menu lets you select which device to boot
from first, simply select your USB drive. (If you have multiple entries that
all look similar to your USB drive, and you're not sure which one is correct,
one option is just to try each one until it works.) If, on the other hand, your
boot menu presents you with a list of boot devices in order, then you'll want
to move your USB drive to the top so that the Qubes installer runs before
anything else.

Once you're done on the boot menu, save your changes. How you do this depends
on your BIOS or UEFI, but the instructions should be displayed right there on
the screen or in a nearby tab. (If you're not sure whether you've saved your
changes correctly, you can always reboot your computer and go back into the
boot menu to check whether it still reflects your changes.) Once your BIOS or
UEFI is configured the way you want it, reboot your computer. This time, don't
press any special keys. Instead, let the BIOS or UEFI load and let your
computer boot from your USB drive. If you're successful in this step, after a
few seconds you'll be presented with the Qubes installer screen:

[![Boot screen](/attachment/doc/boot-screen.png)](/attachment/doc/boot-screen.png)

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>Note:</b> When installing Qubes OS 4.0 on UEFI, there is intentionally no
  boot menu. It goes straight to the installer. The boot menu will be back in
  Qubes OS 4.1.
</div>

From here, you can navigate the boot screen using the arrow keys on your
keyboard. Pressing the "Tab" key will reveal options. You can choose one of
three options:

* Install Qubes OS
* Test this media and install Qubes OS
* Troubleshooting
 
Select the option to test this media and install Qubes OS. 

If the boot screen does not appear, there are several options to troubleshoot.
First, try rebooting your computer. If it still loads your currently installed
operating system or does not detect your installation medium, make sure the
boot order is set up appropriately. The process to change the boot order varies
depending on the currently installed system and the motherboard manufacturer.
If **Windows 10** is installed on your machine, you may need to follow specific
instructions to change the boot order. This may require an [advanced reboot](https://support.microsoft.com/en-us/help/4026206/windows-10-find-safe-mode-and-other-startup-settings).

### The installer home screen

On the first screen, you are asked to select the language that will be used
during the installation process. When you are done, select **Continue**.

[![welcome](/attachment/doc/welcome-to-qubes-os-installation-screen.png)](/attachment/doc/welcome-to-qubes-os-installation-screen.png)

Prior to the next screen, a compatibility test runs to check whether
IOMMU-virtualization is active or not. If the test fails, a window will pop up. 

[![Unsupported hardware detected](/attachment/doc/unsupported-hardware-detected.png)](/attachment/doc/unsupported-hardware-detected.png)

Do not panic. It may simply indicate that IOMMU-virtualization hasn't been
activated in the BIOS or UEFI. Return to the [hardware requirements](#hardware-requirements) section to learn how to activate it. If
the setting is not configured correctly, it means that your hardware won't be
able to leverage some Qubes security features, such as a strict isolation of
the networking and USB hardware. 

If the test passes, you will reach the installation summary screen. The
installer loads Xen right at the beginning. If you can see the installer's
graphical screen, and you pass the compatibility check that runs immediately
afterward, Qubes OS is likely to work on your system!

Like Fedora, Qubes OS uses the Anaconda installer. Those that are familiar with
RPM-based distributions should feel at home. 

### Installation summary

<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>Did you know?</b> The Qubes OS installer is completely offline. It doesn't
  even load any networking drivers, so there is no possibility of
  internet-based data leaks or attacks during the installation process.
</div>

The Installation summary screen allows you to change how the system will be
installed and configured, including localization settings. At minimum, you are
required to select the storage device on which Qubes OS will be installed. 

[![Installation summary not ready](/attachment/doc/installation-summary-not-ready.png)](/attachment/doc/installation-summary-not-ready.png)

### Localization

Let's assume you wish to add a German keyboard layout. Go to Keyboard Layout,
press the "Plus" symbol, search for "German" as indicated in the screenshot and
press "Add". If you want it be your default language, select the "German" entry
in the list and press the arrow button. Click on "Done" in the upper left
corner, and you're ready to go!

[![Keyboard layout selection](/attachment/doc/keyboard-layout-selection.png)](/attachment/doc/keyboard-layout-selection.png)

The process to select a new language is similar to the process to select a new
keyboard layout. Follow the same process in the "Language Support" entry.

[![Language support selection](/attachment/doc/language-support-selection.png)](/attachment/doc/language-support-selection.png)

You can have as many keyboard layout and languages as you want. Post-install,
you will be able to switch between them and install others. 

Don't forget to select your time and date by clicking on the Time & Date entry.

[![Time and date](/attachment/doc/time-and-date.png)](/attachment/doc/time-and-date.png)

### Software

[![Add-ons](/attachment/doc/add-ons.png)](/attachment/doc/add-ons.png)

On the software selection tab, you can choose which software to install in
Qubes OS. Two options are available:

* **Debian:** Select this option if you would like to use
  [Debian](/doc/templates/debian/) qubes in addition to the default Fedora
  qubes.
* **Whonix:** Select this option if you would like to use
  [Whonix](https://www.whonix.org/wiki/Qubes) qubes. Whonix allows you to use
  [Tor](https://www.torproject.org/) securely within Qubes.

Whonix lets you route some or all of your network traffic through Tor for
greater privacy. Depending on your threat model, you may need to install Whonix
templates right away.

Regardless of your choices on this screen, you will always be able to install
these and other [templates](/doc/templates/) later. If you're short on disk
space, you may wish to deselect these options.

By default, Qubes OS comes preinstalled with the lightweight Xfce4 desktop
environment. Other desktop environments will be available to you after the
installation is completed, though they may not be officially supported (see
[Advanced Topics](/doc/#advanced-topics)).

Press **Done** to go back to the installation summary screen.

### Installation destination

Under the System section, you must choose the installation destination. Select
the storage device on which you would like to install Qubes OS.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Be careful to choose the correct installation target, or you
  may lose data. We strongly recommended making a full backup before
  proceeding.
</div>

Your installation destination can be an internal or external storage drive,
such as an SSD, HDD, or USB drive. The installation destination must have a
least 32 GiB of free space available.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> The installation destination cannot be the same as the
  installation medium. For example, if you're installing Qubes OS <em>from</em>
  a USB drive <em>onto</em> a USB drive, they must be two distinct USB drives,
  and they must both be plugged into your computer at the same time. (Note:
  This may not apply to advanced users who partition their devices
  appropriately.)
</div>

Installing an operating system onto a USB drive can be a convenient way to try
Qubes. However, USB drives are typically much slower than internal SSDs. We
recommend a very fast USB 3.0 drive for decent performance. Please note that a
minimum storage of 32 GiB is required. If you want to install Qubes OS onto a
USB drive, just select the USB device as the target installation device. Bear
in mind that the installation process is likely to take longer than it would on
an internal storage device.

[![Select storage device](/attachment/doc/select-storage-device.png)](/attachment/doc/select-storage-device.png)

<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>Did you know?</b> Qubes OS uses full-disk AES encryption (FDE) via LUKS by
  default.
</div>

As soon as you press **Done**, the installer will ask you to enter a passphrase
for disk encryption. The passphrase should be complex. Make sure that your
keyboard layout reflects what keyboard you are actually using. When you're
finished, press **Done**.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> If you forget your encryption passphrase, there is no way to
  recover it.
</div>

[![Select storage passhprase](/attachment/doc/select-storage-passphrase.png)](/attachment/doc/select-storage-passphrase.png)

When you're ready, press **Begin Installation**.

[![Installation summary ready](/attachment/doc/installation-summary-ready.png)](/attachment/doc/installation-summary-ready.png)

### Create your user account

While the installation process is running, you can create your user account.
This is what you'll use to log in after disk decryption and when unlocking the
screen locker. This is a purely local, offline account in dom0. By design,
Qubes OS is a single-user operating system, so this is just for you.

Select **User Creation** to define a new user with administrator privileges and
a password. Just as for the disk encryption, this password should be complex.
The root account is deactivated and should remain as such.

[![Account name and password](/attachment/doc/account-name-and-password.png)](/attachment/doc/account-name-and-password.png)

When the installation is complete, press **Reboot**. Don't forget to remove the
installation medium, or else you may end up seeing the installer boot screen
again.

## Post-installation

### First boot

If the installation was successful, you should now see the GRUB menu during the
boot process.

[![Grub boot menu](/attachment/doc/grub-boot-menu.png)](/attachment/doc/grub-boot-menu.png)

Just after this screen, you will be asked to enter your encryption passphrase.

[![Unlock storage device screen](/attachment/doc/unlock-storage-device-screen.png)](/attachment/doc/unlock-storage-device-screen.png)

### Initial Setup

You're almost done. Before you can start using Qubes OS, some configuration is
needed. 

[![Initial setup menu](/attachment/doc/initial-setup-menu.png)](/attachment/doc/initial-setup-menu.png)

By default, the installer will create a number of qubes (depending on the
options you selected during the installation process). These are designed to
give you a more ready-to-use environment from the get-go.

[![Initial setup menu configuration](/attachment/doc/initial-setup-menu-configuration.png)](/attachment/doc/initial-setup-menu-configuration.png)

Let's briefly go over the options:

* **Create default system qubes:**
  These are the core components of the system, required for things like
  internet access.
* **Create default application qubes:**
  These are how you compartmentalize your digital life. There's nothing special
  about the ones the installer creates. They're just suggestions that apply to
  most people. If you decide you don't want them, you can always delete them
  later, and you can always create your own.
* **Create Whonix Gateway and Workstation qubes:**
  If you want to use Whonix, you should select this option.
  * **Enabling system and template updates over the Tor anonymity network using
  Whonix:**
  If you select this option, then whenever you install or update software in
  dom0 or a template, the internet traffic will go through Tor.
* **Create USB qube holding all USB controllers:**
  Just like the network qube for the network stack, the USB qube isolates the
  USB controllers.
  * **Use sys-net qube for both networking and USB devices:**
  You should select this option if you rely on a USB device for network access,
  such as a USB modem or a USB Wi-Fi adapter.
* **Do not configure anything:**
  This is for very advanced users only. If you select this option, you'll have
  to set everything up manually afterward.

When you're satisfied with you choices, press **Done**. This configuration
process may take a while, depending on the speed and compatibility of your
system.

After the configuration is done, you will be greeted by the login screen. Enter
your password and log in.

[![Login screen](/attachment/doc/login-screen.png)](/attachment/doc/login-screen.png)

Congratulations, you are now ready to use Qubes OS!

[![Desktop menu](/attachment/doc/desktop-menu.png)](/attachment/doc/desktop-menu.png)

## Next steps

### Updating

Next, [update](/doc/how-to-update/) your installation to ensure you have
the latest security updates. Frequently updating is one of the best ways to
remain secure against new threats.

### Security

The Qubes OS Project occasionally issues [Qubes Security Bulletins (QSBs)](/security/qsb/) as part of the [Qubes Security Pack (qubes-secpack)](/security/pack/). It is important to make sure that you
receive all QSBs in a timely manner so that you can take action to keep your
system secure. (While [updating](#updating) will handle most security needs,
there may be cases in which additional action from you is required.) For this
reason, we strongly recommend that every Qubes user subscribe to the
[qubes-announce](/support/#qubes-announce) mailing list.

In addition to QSBs, the Qubes OS Project also publishes
[Canaries](/security/canary/), XSA summaries, template releases and
end-of-life notices, and other items of interest to Qubes users. Since these
are not essential for all Qubes users to read, they are not sent to
[qubes-announce](/support/#qubes-announce) in order to keep the volume on that
list low. However, we expect that most users, especially novice users, will
find them helpful. If you are interested in these additional items, we
encourage you to subscribe to the [Qubes News RSS feed](/feed.xml) or join one
of our other [venues](/support/), where these news items are also announced.

For more information about Qubes OS Project security, please see the [security center](/security/).

### Backups

It is extremely important to make regular backups so that you don't lose your
data unexpectedly. The [Qubes backup system](/doc/how-to-back-up-restore-and-migrate/) allows you to do this
securely and easily.

### Submit your HCL report

Consider giving back to the Qubes community and helping other users by
[generating and submitting a Hardware Compatibility List (HCL) report](/doc/how-to-use-the-hcl/#generating-and-submitting-new-reports).

### Get Started

Find out [Getting Started](/doc/getting-started/) with Qubes, check out
the other [How-To Guides](/doc/#how-to-guides), and learn about
[Templates](/doc/#templates).

## Getting help

* We work very hard to make the [documentation](/doc/) accurate, comprehensive
  useful and user friendly. We urge you to read it! It may very well contain
  the answers to your questions. (Since the documentation is a community
  effort, we'd also greatly appreciate your help in
  [improving](/doc/how-to-edit-the-documentation/) it!)

* If issues arise during installation, see the [Installation Troubleshooting](/doc/installation-troubleshooting) guide. 

* If you don't find your answer in the documentation, please see [Help, Support, Mailing Lists, and Forum](/support/) for places to ask.

* Please do **not** email individual members of the Qubes team with questions
  about installation or other problems. Instead, please see [Help, Support, Mailing Lists, and Forum](/support/) for appropriate places to ask questions.
