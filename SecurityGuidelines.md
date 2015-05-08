---
layout: doc
title: SecurityGuidelines
permalink: /doc/SecurityGuidelines/
redirect_from: /wiki/SecurityGuidelines/
---

Security Guidelines
===================

1.  [Security Guidelines](#SecurityGuidelines)
    1.  [Download Verification](#DownloadVerification)
    2.  [Observing Security Contexts](#ObservingSecurityContexts)
    3.  [Installing Versus Running Programs](#InstallingVersusRunningPrograms)
    4.  [Enabling and Verifying VT-d/IOMMU](#EnablingandVerifyingVT-dIOMMU)
    5.  [Updating Software](#UpdatingSoftware)
    6.  [Handling Untrusted Files](#HandlingUntrustedFiles)
    7.  [Anti Evil Maid](#AntiEvilMaid)
    8.  [Reassigning USB Controllers](#ReassigningUSBControllers)
    9.  [Creating and Using a USBVM](#CreatingandUsingaUSBVM)
    10. [Dom0 Precautions](#Dom0Precautions)

The [Qubes introduction](http://theinvisiblethings.blogspot.com/2012/09/introducing-qubes-10.html) makes clear that without some active and responsible participation of the user, no real security is possible. So, for example, Qubes does not automagically make your Firefox (or any other app) running in one of the AppVMs suddenly more secure. It is just as [secure (or insecure)](https://en.wikipedia.org/wiki/Computer_insecurity) as on a normal Linux or Windows OS. But what drastically changes is the context in which your applications are used. [This context](/wiki/QubesArchitecture) is a [responsibility of the user](/wiki/SecurityGoals). But participation requires knowledge. So it is worth stressing some basic items:

Download Verification
---------------------

**Verify the authenticity and integrity of your downloads, [particularly Qubes iso](/wiki/VerifyingSignatures).**

Standard program installation

{% highlight trac-wiki %}
sudo yum install <program>
{% endhighlight %}

on template terminal already accomplishes verification, for fedora and qubes repositories.

If you install new repositories, they might have gpgcheck disabled. [Check the config files](http://docs.fedoraproject.org/en-US/Fedora/12/html/Deployment_Guide/sec-Configuring_Yum_and_Yum_Repositories.html) and be sure to check that

{% highlight trac-wiki %}
gpgcheck=1
{% endhighlight %}

Plus, also make sure you **safely import their signing keys**. This may require you check from multiple sources that the signing key is always the same.

Even then, you might want to consider new repository to be **less** secure and do not use it **in the template** that feeds your more trusted VMs.

But if you need to download programs that cannot be verified, then it is certainly better to install them in a **cloned template or a standalone VM**.

Observing Security Contexts
---------------------------

To each VM is associated a specific colour of window borders in Qubes. They are how Qubes communicates the **security context** of applications and data so that users can be easily aware of this at all times. So be sure to check the colour of window borders before taking any action, particularly if related to security, [see blog](http://theinvisiblethings.blogspot.com/2011/05/app-oriented-ui-model-and-its-security.html).

Also, be sure to use **Expose-like effect** when dealing with a smaller window displayed on top of a larger window. Remember that a "red" Firefox, can always draw a "green" password prompt box, and you don't want to enter your password there!

Check **Expose-like effect** is activated (e.g. System Tools -\> System Settings -\> Desktop Effects -\> All Effects -\> Desktop Grid Present Windows effects in KDE, or, if you're a hard-core Xfce4 user or something, then manually move the more trusted window so that it is not displayed on top of a less trusted one, but rather over the trusted Dom0 wallpaper.

Installing Versus Running Programs
----------------------------------

With the exception of the editor required for configuration, one should not run applications in either template VMs or in Dom0. From a security standpoint there is a great difference between installing a program and running it.

Enabling and Verifying VT-d/IOMMU
---------------------------------

In **Dom0** terminal, run:

{% highlight trac-wiki %}
qubes-hcl-report <userVM>
{% endhighlight %}

where \<userVM\> is the name of the VM within which the report will be written (but the report will also be displayed in the Dom0 terminal). If it displays that VT-d is active, you should be able to assign **PCIe devices to a HVM** and **enjoy DMA protection** for your driver domains, so you successfully passed this step.

If VT-d is not active, attempt to activate it by selecting the **VT-d flag** within the BIOS settings. If your processor/BIOS does not allow VT-d activation you still enjoy much better security than alternative systems, but you may be vulnerable to **DMA attacks**. Next time you buy a computer consult our **HCL (Hardware Compatibility List)** and possibly contribute to it.

Updating Software
-----------------

To keep your system regularly updated against security related bugs and get new features, run in Dom0:

{% highlight trac-wiki %}
sudo qubes-dom0-update
{% endhighlight %}

and run in templates and standalone VM

{% highlight trac-wiki %}
sudo yum update
{% endhighlight %}

or use the equivalent items in Qubes Manager, which displays an icon when an update is available.

Handling Untrusted Files
------------------------

When you receive or download any file from an **untrusted source**, do not browse to it with a file manager which has preview enabled. **To disable preview in Nautilus**: Gear (up-right-icon) -\> Preferences -\> Preview (tab) -\> Show thumbnails: Never. Note that this change can be made in a TemplateVM (including the [DispVM template](/wiki/UserDoc/DispVMCustomization)) so that future AppVMs created from this TemplateVM will inherit this feature.

Also, **do not open it in trusted VMs**. Rather open it in a **disposable VM** right-clicking on it. You may even modify it within the disposable VM and then [copy it to other VM](/wiki/CopyingFiles).

Alternatively PDFs may be converted to **trusted PDF** right clicking on them. This converts text to graphic form, so size will increase.

Anti Evil Maid
--------------

If there is a risk that somebody may **physically attack** your computer when you leave it powered down, or if you use Qubes in **dual boot mode**, then you may want to [install AEM](/wiki/AntiEvilMaid) (Anti Evil Maid). AEM will inform you of any unauthorized modifications to your BIOS or boot partition. If AEM alerts you of an attack it is really bad news because **there is no true fix**. If you are really serious about security you have to buy a new laptop and install Qubes from a trusted ISO. So buying a used laptop is not an option for a security focused one.

Reassigning USB Controllers
---------------------------

Before you [assign a USB controller to a VM](/wiki/AssigningDevices) check if any **input devices** are included in that controller.

Assigning USB keyboard will **deprive Dom0 VM of a keyboard**. Since a USB controller assignment survives reboot, you may find yourself **unable to access your system**. Most non-Apple laptops have a PS/2 input for keyboard and mouse, so this problem does not exist.

But **if you need to use a USB keyboard or mouse**, identify the USB controller in which you have your keyboard/mouse plugged in and do NOT assign it to a VM. Also makes sure you know all the other USB ports for that controller, and use them carefully, with the knowledge **you are exposing Dom0** (ie NO bluetooth device on it).

All USB devices should be assumed as **side channel attack vectors** (mic via sound), others via power usage so user may prefer to remove them. [See this about rootkits](https://www.networkworld.com/news/2007/080207-black-hat-virtual-machine-rootkit-detection.html)

The **web-cam** also may involve a risk, so better to physically cover it with a adhesive tape if you do not use it. If you need it, you have **to assign it to a VM** and cover it with a cap or an elastic band when not in use. Attaching a **microphone** using Qubes VM Manager also may be risky, so attach it only when required.

It is preferably to avoid using **Bluetooth** if you travel and if you do not trust your neighbours. Also there are zones roamed by kids with high-gain directional antennas. In this case, better buy a computer that does not have a Bluetooth hardware module, or, if you have it, assign it to an untrusted VM. This last solution will work also if you want to use Bluetooth without trusting it.

Many laptops will also allow one to disable various hardware (Camera, BT, Mic, etc) **in BIOS**. This might or might not be safe, depending on how much you trust your BIOS vendor.

Creating and Using a USBVM
--------------------------

The connection of an **untrusted USB external drive to Dom0** may involve some risk because Dom0 reads **partition tables** automatically, and also because the whole USB stack is put to work **to parse** all the USB device info first, to determine if it is a USB Mass Storage, and to read its config, etc. This happens even if the drive is then assigned and mounted in another VM.

To avoid this risk it is possible to prepare and utilize a **USBVM**. However this is not presently recommended for beginners, as Xen does not yet provide a working PVUSB, and so only USB Mass Storage devices could be passed to individual VMs later (via qvm-block). This involves that a USBVM cannot be preinstalled and the whole thing cannot be automatized. So avoid it if you have doubts.

Also avoid it if you do not have a **USB controller free of input devices** or programmable devices. However, as already noted most laptops use PS-2 for keyboards and touchpad devices which do not cause problems.

An **USBVM** operates like a dedicated temporary parking area, used just to prevent any contact between dom0 and the USB drive. Then, every time you connect an **untrusted USB external drive** to a USB port managed by that USB controller, you need to attach it to the VM that needs it, using qubes manager or [terminal](/wiki/StickMounting). Again, this **works only for disk-like USB devices**. Other devices cannot be currently virtualized. So once you assign their controller to your **USBVM** they'll be no more available.

**The process for creating a USBVM** is:

1.  In Dom0 terminal type `lsusb` to check if you have a USB controller free of input devices or programmable devices. If you find such free controller, then
2.  Create a new AppVM. Call it "usbvm" (or whatever you want).
3.  Give it "red" or "orange" or "yellow" label.
4.  In the AppVM's settings, go to the "devices" tab. Find your USB controller in the "Available" list. Move it to the "Selected" list.
5.  Click OK. Restart the AppVM. (Restarting may not even be required.)
6.  **In dom0 terminal**, run

    {% highlight trac-wiki %}
    qvm-prefs -s usbvm autostart true
    {% endhighlight %}

This will cause your new **USBVM** to automatically start when the system starts up. So that in case you forgot to start it and then accidentally plugged a USB stick (or your colleague at work did it while you were at lunch), **it won't compromise the Dom0**.

Dom0 Precautions
----------------

As explained [here](/wiki/GettingStarted#AppVMsDomainsandTemplateVMs), dom0 should not be used for any user operations. There are several reasons for this:

1.  Secure isolation among domUs (i.e., AppVMs, StandaloneVMs, HVMs, etc.) is the *raison d'être* of Qubes. This is the primary reason that we recommend the delegation of all user activities to some number of AppVMs. In the event that any given VM is compromised, only that particular VM is compromised. (TemplateVMs are the exception to this. If a TemplateVM were compromised, then every AppVM based on it might also be compromised. Even in this case, however, the entire system would not necessarily have been compromised, since StandaloneVM(s), HVM(s), and/or multiple TemplateVMs might be in use.) By contrast, if dom0 were ever compromised, the entire system would thereby be compromised.
2.  Due to the absence of convenience mechanisms in dom0 such as the inter-VM clipboard and inter-VM file copying, it is significantly less convenient to attempt to use dom0 for user operations (e.g., password management) in conjunction with AppVMs than it is to use another dedicated AppVM (e.g., a "vault" VM).
3.  Dom0 has access to every VM's data in the form of its private image file, including untrusted (e.g., red-bordered) VMs. If the user were to make a mistake (or be tricked into making one) and thereby inadvertently access untrusted files from dom0, those files could exploit the application which accessed them (e.g., a file manager) and gain control over dom0 and, therefore, the entire system. Even simply displaying the data in a [terminal emulator](http://securityvulns.com/docs4128.html) can be dangerous. For example, some file managers (such as the Thunar File Manager, which is pre-installed by default in the Xfce4 version of dom0) list loop devices used by running VMs. When one of these devices is selected in the file manager, the loop device is mounted to dom0, effectively [transferring the contents](https://groups.google.com/d/msg/qubes-users/_tkjmBa9m9w/9BbKh94PVtcJ) of the home directory of a (by definition less trusted) AppVM to dom0.
4.  There is a (hopefully small but non-zero) chance that any given program which runs in dom0 (or anywhere, for that matter) is malicious. (For example, an attacker may have stolen a third-party developer's keys and used them to sign a malicious package, which has then been downloaded as part of a standard yum update.) For this reason, it is very important that as few programs as possible be run in dom0 in as restricted a manner as possible. For example, although GnuPG is used in dom0 for verifying updates received from the firewallvm, it does not follow that GnuPG should be used for regular user operations (e.g., key management) in dom0. This is because only a single GnuPG operation, the "verify signature" operation" (which is believed to be the most bulletproof operation in GnuPG), is used by default in dom0. No other key management operations (e.g., importing unverified keys) or any other data parsing takes place in dom0 by default.
5.  Any VM can be shut down in order to make it even more difficult for an adversary to access, and shutting down one VM does not restrict the user of other VMs. By contrast, one cannot shut down dom0 and use other VMs at the same time.
6.  As far as we are aware, there are no special mechanisms in Xen which make dom0 more protected than any other VM, so there is no inherent security advantage to performing any user operations in dom0.

