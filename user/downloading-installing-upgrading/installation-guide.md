---
lang: en
layout: doc
permalink: /doc/installation-guide/
redirect_from:
- /en/doc/installation-guide/
- /doc/installationguide/
- /wiki/installationguide/
- /doc/installationguider1/
- /doc/installationguider2b1/
- /doc/installationguider2b2/
- /doc/installationguider2b3/
- /doc/installationguider2rc1/
- /doc/installationguider2rc2/
- /doc/installationguider3.0rc1/
- /doc/installationguider3.0rc2/
- /doc/live-usb/
ref: 153
title: installation guide
---

welcome to the qubes os installation guide! this guide will walk you through
the process of installing qubes. please read it carefully and thoroughly, as it
contains important information for ensuring that your qubes os installation is
functional and secure.

## pre-installation

### hardware requirements

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>warning:</b> qubes has no control over what happens on your computer
  before you install it. no software can provide security if it is installed on
  compromised hardware. do not install qubes on a computer you don't trust. see
  <a href="/doc/install-security/">installation security</a> for more
  information.
</div>

qubes os has very specific [system requirements](/doc/system-requirements/). to
ensure compatibility, we strongly recommend using [qubes-certified
hardware](/doc/certified-hardware/). other hardware may require you to perform
significant troubleshooting. you may also find it helpful to consult the
[hardware compatibility list](/hcl/).

even on supported hardware, you must ensure that [iommu-based
virtualization](https://en.wikipedia.org/wiki/input%e2%80%93output_memory_management_unit#virtualization)
is activated in the bios. without it, qubes os won't be able to enforce
isolation. for intel-based boards, this setting is called intel virtualization
for directed i/o (**intel vt-d**) and for amd-based boards, it is called  amd
i/o virtualization technology (or simply **amd-vi**). this parameter should be
activated in your computer's bios, alongside the standard virtualization
(**intel vt-x**) and amd virtualization (**amd-v**) extensions. this [external
guide](https://web.archive.org/web/20200112220913/https://www.intel.in/content/www/in/en/support/articles/000007139/server-products.html)
made for intel-based boards can help you figure out how to enter your bios to
locate and activate those settings. if those settings are not nested under the
advanced tab, you might find them under the security tab.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>note:</b> qubes os is not meant to be installed inside a virtual machine
  as a guest hypervisor. in other words, <b>nested virtualization</b> is not
  supported. in order for a strict compartmentalization to be enforced, qubes
  os needs to be able to manage the hardware directly.
</div>

### copying the iso onto the installation medium

start by [downloading](/downloads/) a qubes iso.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>warning:</b> any file you download from the internet could be malicious,
  even if it appears to come from a trustworthy source. our philosophy is to <a
  href="/faq/#what-does-it-mean-to-distrust-the-infrastructure">distrust the
  infrastructure</a>. regardless of how you acquire your qubes iso, <a
  href="/security/verifying-signatures/">verify its authenticity</a> before
  continuing.
</div>

once the iso has been verified as authentic, you should copy it onto the
installation medium of your choice, such as a dual-layer dvd, a blu-ray disc,
or a usb drive. the size of each qubes iso is available on the
[downloads](/downloads/) page by hovering over the download button.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>note:</b> there are important <a href="/doc/install-security/">security
  considerations</a> to keep in mind when choosing an installation medium.
</div>

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>warning:</b> be careful to choose the correct device when copying the iso,
  or you may lose data. we strongly recommended making a full backup before
  modifying any devices.
</div>

if you choose to use a usb drive, copy the iso onto the usb device, e.g. using
`dd`:

```
$ sudo dd if=qubes-rx-x86_64.iso of=/dev/sdy status=progress bs=1048576 && sync
```

change `qubes-rx-x86_64.iso` to the filename of the version you're installing,
and change `/dev/sdy` to the correct target device e.g., `/dev/sdc`). make sure
to write to the entire device (e.g., `/dev/sdc`) rather than just a single
partition (e.g., `/dev/sdc1`).

on windows, you can use the [rufus](https://rufus.akeo.ie/) tool to write the
iso to a usb key. mediatest is not recommended. be sure to select "dd image"
mode (*after* selecting the qubes iso):

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>note:</b>  if you do this on windows 10, you can only install qubes
  without mediatest, which is not recommended.
</div>

![rufus menu](/attachment/doc/rufus-menu.png)

![rufus dd image mode](/attachment/doc/rufus-dd-image-mode.png)

if you are an advanced user, and you would like to customize your installation,
please see [custom installation](/doc/custom-install/). otherwise, follow the
instructions below.

## installation

this section will demonstrate a simple installation using mostly default
settings.

### getting to the boot screen

just after you power on your machine, make the qubes os medium available to the
computer by inserting your dvd or usb drive. shortly after the power-on
self-test (post) is completed, you should be greeted with the qubes os boot
screen. 

![boot screen](/attachment/doc/boot-screen.png)

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>note:</b> when installing qubes os 4.0 on uefi, there is intentionally no
  boot menu. it goes straight to the installer. the boot menu will be back in
  qubes os 4.1.
</div>

from here, you can navigate the boot screen using the arrow keys on your
keyboard. pressing the "tab" key will reveal options. you can choose one of
three options:

* install qubes os
* test this media and install qubes os
* troubleshooting
 
select the option to test this media and install qubes os. 

if the boot screen does not appear, there are several options to troubleshoot.
first, try rebooting your computer. if it still loads your currently installed
operating system or does not detect your installation medium, make sure the
boot order is set up appropriately. the process to change the boot order varies
depending on the currently installed system and the motherboard manufacturer.
if **windows 10** is installed on your machine, you may need to follow specific
instructions to change the boot order. this may require an [advanced
reboot](https://support.microsoft.com/en-us/help/4026206/windows-10-find-safe-mode-and-other-startup-settings).

after the post, you may have a chance to choose a boot device. you may wish to
select the usb drive or dvd drive as a temporary boot option so that the next
time you boot, your internal storage device will be selected first. 

![boot order](/attachment/doc/boot-order.png)

### the installer home screen

on the first screen, you are asked to select the language that will be used
during the installation process. when you are done, select **continue**.

![welcome](/attachment/doc/welcome-to-qubes-os-installation-screen.png)

prior to the next screen, a compatibility test runs to check whether
iommu-virtualization is active or not. if the test fails, a window will pop up. 

![unsupported hardware detected](/attachment/doc/unsupported-hardware-detected.png)

do not panic. it may simply indicate that iommu-virtualization hasn't been
activated in the bios. return to the [hardware
requirements](#hardware-requirements) section to learn how to activate it. if
the setting is not configured correctly, it means that your hardware won't be
able to leverage some qubes security features, such as a strict isolation of
the networking and usb hardware. 

if the test passes, you will reach the installation summary screen. the
installer loads xen right at the beginning. if you can see the installer's
graphical screen, and you pass the compatibility check that runs immediately
afterward, qubes os is likely to work on your system!

like fedora, qubes os uses the anaconda installer. those that are familiar with
rpm-based distributions should feel at home. 

### installation summary

<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>did you know?</b> the qubes os installer is completely offline. it doesn't
  even load any networking drivers, so there is no possibility of
  internet-based data leaks or attacks during the installation process.
</div>

the installation summary screen allows you to change how the system will be
installed and configured, including localization settings. at minimum, you are
required to select the storage device on which qubes os will be installed. 

![installation summary not ready](/attachment/doc/installation-summary-not-ready.png)

### localization

let's assume you wish to add a german keyboard layout. go to keyboard layout,
press the "plus" symbol, search for "german" as indicated in the screenshot and
press "add". if you want it be your default language, select the "german" entry
in the list and press the arrow button. click on "done" in the upper left
corner, and you're ready to go!

![keyboard layout selection](/attachment/doc/keyboard-layout-selection.png)

the process to select a new language is similar to the process to select a new
keyboard layout. follow the same process in the "language support" entry.

![language support selection](/attachment/doc/language-support-selection.png)

you can have as many keyboard layout and languages as you want. post-install,
you will be able to switch between them and install others. 

don't forget to select your time and date by clicking on the time & date entry.

![time and date](/attachment/doc/time-and-date.png)

### software

![add-ons](/attachment/doc/add-ons.png)

on the software selection tab, you can choose which software to install in
qubes os. two options are available:

* **debian:** select this option if you would like to use
  [debian](/doc/templates/debian/) qubes in addition to the default fedora
  qubes.
* **whonix:** select this option if you would like to use
  [whonix](/doc/whonix/) qubes. whonix allows you to use
  [tor](https://www.torproject.org/) securely within qubes.

whonix lets you route some or all of your network traffic through tor for
greater privacy. depending on your threat model, you may need to install whonix
templates right away.

regardless of your choices on this screen, you will always be able to install
these and other [templates](/doc/templates/) later. if you're short on disk
space, you may wish to deselect these options.

by default, qubes os comes preinstalled with the lightweight xfce4 desktop
environment. other desktop environments will be available to you after the
installation is completed, though they may not be officially supported (see
[advanced topics](/doc/#advanced-topics)).

press **done** to go back to the installation summary screen.

### installation destination

under the system section, you must choose the installation destination. select
the storage device on which you would like to install qubes os.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>warning:</b> be careful to choose the correct installation target, or you
  may lose data. we strongly recommended making a full backup before
  proceeding.
</div>

your installation destination can be an internal or external storage drive,
such as an ssd, hdd, or usb drive. the installation destination must have a
least 32 gib of free space available.

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>note:</b> the installation destination cannot be the same as the
  installation medium. for example, if you're installing qubes os <em>from</em>
  a usb drive <em>onto</em> a usb drive, they must be two distinct usb drives,
  and they must both be plugged into your computer at the same time. (note:
  this may not apply to advanced users who partition their devices
  appropriately.)
</div>

installing an operating system onto a usb drive can be a convenient way to try
qubes. however, usb drives are typically much slower than internal ssds. we
recommend a very fast usb 3.0 drive for decent performance. please note that a
minimum storage of 32 gib is required. if you want to install qubes os onto a
usb drive, just select the usb device as the target installation device. bear
in mind that the installation process is likely to take longer than it would on
an internal storage device.

![select storage device](/attachment/doc/select-storage-device.png)

<div class="alert alert-success" role="alert">
  <i class="fa fa-check-circle"></i>
  <b>did you know?</b> qubes os uses full-disk aes encryption (fde) via luks by
  default.
</div>

as soon as you press **done**, the installer will ask you to enter a passphrase
for disk encryption. the passphrase should be complex. make sure that your
keyboard layout reflects what keyboard you are actually using. when you're
finished, press **done**.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>warning:</b> if you forget your encryption passphrase, there is no way to
  recover it.
</div>

![select storage passhprase](/attachment/doc/select-storage-passphrase.png)

when you're ready, press **begin installation**.

![installation summary ready](/attachment/doc/installation-summary-ready.png)

### create your user account

while the installation process is running, you can create your user account.
this is what you'll use to log in after disk decryption and when unlocking the
screen locker. this is a purely local, offline account in dom0. by design,
qubes os is a single-user operating system, so this is just for you.

select **user creation** to define a new user with administrator privileges and
a password. just as for the disk encryption, this password should be complex.
the root account is deactivated and should remain as such.

![account name and password](/attachment/doc/account-name-and-password.png)

when the installation is complete, press **reboot**. don't forget to remove the
installation medium, or else you may end up seeing the installer boot screen
again.

## post-installation

### first boot

if the installation was successful, you should now see the grub menu during the
boot process.

![grub boot menu](/attachment/doc/grub-boot-menu.png)

just after this screen, you will be asked to enter your encryption passphrase.

![unlock storage device screen](/attachment/doc/unlock-storage-device-screen.png)

### initial setup

you're almost done. before you can start using qubes os, some configuration is
needed. 

![initial setup menu](/attachment/doc/initial-setup-menu.png)

by default, the installer will create a number of qubes (depending on the
options you selected during the installation process). these are designed to
give you a more ready-to-use environment from the get-go.

![initial setup menu configuration](/attachment/doc/initial-setup-menu-configuration.png)

let's briefly go over the options:

* **create default system qubes:**
  these are the core components of the system, required for things like
  internet access.
* **create default application qubes:**
  these are how you compartmentalize your digital life. there's nothing special
  about the ones the installer creates. they're just suggestions that apply to
  most people. if you decide you don't want them, you can always delete them
  later, and you can always create your own.
* **create whonix gateway and workstation qubes:**
  if you want to use whonix, you should select this option.
  * **enabling system and template updates over the tor anonymity network using whonix:**
  if you select this option, then whenever you install or update software in
  dom0 or a template, the internet traffic will go through tor.
* **create usb qube holding all usb controllers:**
  just like the network qube for the network stack, the usb qube isolates the
  usb controllers.
  * **use sys-net qube for both networking and usb devices:**
  you should select this option if you rely on a usb device for network access,
  such as a usb modem or a usb wi-fi adapter.
* **Do not configure anything:**
  This is for very advanced users only. If you select this option, you'll have
  to set everything up manually afterward.

When you're satisfied with you choices, press **Done**. This configuration
process may take a while, depending on the speed and compatibility of your
system.

After the configuration is done, you will be greeted by the login screen. Enter
your password and log in.

![Login screen](/attachment/doc/login-screen.png)

Congratulations, you are now ready to use Qubes OS!

![Desktop menu](/attachment/doc/desktop-menu.png)

## Next steps

### Updating

Next, [update](/doc/how-to-update/) your installation to ensure you have
the latest security updates. Frequently updating is one of the best ways to
remain secure against new threats.

### Security

The Qubes OS Project occasionally issues [Qubes Security Bulletins
(QSBs)](/security/bulletins/) as part of the [Qubes Security Pack
(qubes-secpack)](/security/pack/). It is important to make sure that you
receive all QSBs in a timely manner so that you can take action to keep your
system secure. (While [updating](#updating) will handle most security needs,
there may be cases in which additional action from you is required.) For this
reason, we strongly recommend that every Qubes user subscribe to the
[qubes-announce](/support/#qubes-announce) mailing list.

In addition to QSBs, the Qubes OS Project also publishes
[Canaries](/security/canaries/), XSA summaries, template releases and
end-of-life notices, and other items of interest to Qubes users. Since these
are not essential for all Qubes users to read, they are not sent to
[qubes-announce](/support/#qubes-announce) in order to keep the volume on that
list low. However, we expect that most users, especially novice users, will
find them helpful. If you are interested in these additional items, we
encourage you to subscribe to the [Qubes News RSS feed](/feed.xml) or join one
of our other [venues](/support/), where these news items are also announced.

For more information about Qubes OS Project security, please see the [security
center](/security/).

### Backups

It is extremely important to make regular backups so that you don't lose your
data unexpectedly. The [Qubes backup
system](/doc/how-to-back-up-restore-and-migrate/) allows you to do this
securely and easily.

### Submit your HCL report

Consider giving back to the Qubes community and helping other users by
[generating and submitting a Hardware Compatibility List (HCL)
report](/doc/hcl/#generating-and-submitting-new-reports).

### Get Started

See [How to Get Started](/doc/how-to-get-started/) with Qubes, check out the
[How-to Guides](/doc/#how-to-guides), and learn about
[Templates](/doc/#templates).

## Getting help

* We work very hard to make the [documentation](/doc/) accurate, comprehensive
  useful and user friendly. We urge you to read it! It may very well contain
  the answers to your questions. (Since the documentation is a community
  effort, we'd also greatly appreciate your help in
  [improving](/doc/doc-guidelines/) it!)

* If issues arise during installation, see the [Installation
  Troubleshooting](/doc/installation-troubleshooting) guide. 

* If you don't find your answer in the documentation, please see [Help,
  Support, Mailing Lists, and Forum](/support/) for places to ask.

* Please do **not** email individual members of the Qubes team with questions
  about installation or other problems. Instead, please see [Help, Support,
  Mailing Lists, and Forum](/support/) for appropriate places to ask questions.

