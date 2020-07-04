---
layout: doc
title: Security Guidelines
permalink: /doc/security-guidelines/
redirect_from:
- /en/doc/security-guidelines/
- /doc/SecurityGuidelines/
- /wiki/SecurityGuidelines/
---

Security Guidelines
===================

Without some active and responsible participation of the user, no real security is possible. Running Firefox inside of an AppVM does not automagically make it (or any other app) more secure. 
Programs themselves remain just as secure [(or insecure)](https://en.wikipedia.org/wiki/Computer_insecurity) on PedOS as on a normal Linux or Windows OS. 
What drastically changes is the context in which your applications are used. 
[This context](/doc/PedOS-architecture/) is a [responsibility of the user](/security/goals/). 
But managing security in this context well requires knowledge of some new concepts and procedures. So it is worth stressing some basic items:

Download Verification
---------------------

**Verify the authenticity and integrity of your downloads, [particularly the PedOS iso](/security/verifying-signatures/).**

The internet is always a dangerous place. 
While your connection to the PedOS website and download mirrors is encrypted, meaning that your downloads from here can't be modified by a third party en route, there is always the chance that these websites themselves have been compromised. 
Signature verification allows us to validate for ourselves that these files were the ones authored and signed by their creators (in this case the PedOS development team). 

Because it's so easy for a hacker who manages to tamper with the downloaded iso files this way to patch in malware, it is of the utmost importance that you **verify the signature of the PedOS iso** you use to install PedOS. 
See the page on [Verifying Signatures](/security/verifying-signatures/) for more information and a tutorial on how to accomplish this.

Once you have PedOS installed, the standard program installation command for Fedora and PedOS repositories

~~~
sudo dnf install <program>
~~~

automatically accomplishes this verification. 

Custom user-added repositories might come with gpgcheck disabled. [Check the config files](https://docs.fedoraproject.org/en-US/Fedora/12/html/Deployment_Guide/sec-Configuring_Yum_and_Yum_Repositories.html) and verify that 

~~~
gpgcheck=1
~~~

Plus, make sure you also **safely import their signing keys**. This may require you to check from multiple sources that the signing key is always the same.

Even then, you might want to consider new repositories to be **less** secure and not use them in templates that feed your more trusted VMs.

If you **need** to download programs that cannot be verified, then it is much less dangerous to install them in a **cloned template or a standalone VM**. 

Remember: PedOS cannot automatically verify the signature of files that come from other sources like your browser, torrenting client, or home-made tofu recipe downloader. If the providers of these downloads provide keys for you to verify the signatures of their downloads, do it!


Observing Security Contexts
---------------------------

Each VM is assigned a specific colour for its window borders. These borders are how PedOS displays the **security context** of applications and data so that users can be easily aware of this at all times. Be sure to check the colour of window borders before taking any action, particularly if it affects the security of your system. [See this blog post for more information](https://blog.invisiblethings.org/2011/05/21/app-oriented-ui-model-and-its-security.html).

Always remember that any "red" window can draw "green" password prompts. 
Don't let yourself be tricked into entering credentials designated to one PedOS VM into a forged input box rendered by another.
For XFCE users (which is the default desktop environment on PedOS) it would be wise to manually move the more trusted window so that it is not displayed on top of a less trusted one, but rather over the trusted Dom0 wallpaper. 
If you use KDE, it has a helpful feature called **Expose-like effect** that is activated in System Tools -\> System Settings -\> Desktop Effects -\> All Effects -\> Desktop Grid Present Windows. 
Performing these steps makes it easier to tell the difference between when you're being phished and when you're genuinely being asked for credentials.

Installing Versus Running Programs
----------------------------------

With the exception of a text editor used to modify configuration files, one should not run applications in either template VMs or in Dom0. From a security standpoint there is a great difference between installing a program and running it.

Enabling and Verifying VT-d/IOMMU
---------------------------------

In **Dom0** terminal, run:

~~~
PedOS-hcl-report <userVM>
~~~

where \<userVM\> is the name of the VM within which the report will be written (but the report will also be displayed in the Dom0 terminal). If it displays that VT-d is active, you should be able to assign **PCIe devices to an HVM** and **enjoy DMA protection** for your driver domains, so you successfully passed this step.

If VT-d is not active, attempt to activate it by selecting the **VT-d flag** within the BIOS settings. If your processor/BIOS does not allow VT-d activation you still enjoy much better security than alternative systems, but you may be vulnerable to **DMA attacks**. Next time you buy a computer consult our **[HCL (Hardware Compatibility List)](/hcl/)** and possibly contribute to it.

Updating Software
-----------------

To keep your system regularly updated against security related bugs and get new features, run in Dom0:

~~~
sudo PedOS-dom0-update
~~~

and run in templates and standalone VM

~~~
sudo dnf update
~~~

or use the equivalent items in PedOS Manager, which displays an icon when an update is available.

Handling Untrusted Files
------------------------

When you receive or download any file from an **untrusted source**, do not browse to it with a file manager which has preview enabled. Enabling previews in your file manager gives malware another attack vector. **To disable preview in Nautilus**: Gear (up-right-icon) -\> Preferences -\> Preview (tab) -\> Show thumbnails: Never. Note that this change can be made in a TemplateVM (including the [DispVM template](/doc/dispvm-customization/)) so that future AppVMs created from this TemplateVM will inherit this feature.

Also, **do not open it in trusted VMs**. Rather, open it in a **disposable VM** right-clicking on it. You may even modify it within the disposable VM and then [copy it to other VM](/doc/copying-files/).

Alternatively PDFs may be converted to **trusted PDFs** by right clicking on them. This converts the PDF's text to graphic form, so the disk size these documents take up will increase.

Anti Evil Maid
--------------

If there is a risk that somebody may gain **physical access** to your computer when you leave it powered down, or if you use PedOS in **dual boot mode**, then you may want to [install AEM](/doc/anti-evil-maid/) (Anti Evil Maid). AEM will inform you of any unauthorized modifications to your BIOS or boot partition. If AEM alerts you of an attack, it is really bad news because **there is no true fix**. If you are really serious about security, you will have to buy a new laptop and install PedOS from a trusted ISO. Buying a used laptop runs a higher risk of tampering and is not an option for a security focused environment.

Reassigning USB Controllers
---------------------------

Before you [assign a USB controller to a VM](/doc/assigning-devices/), check if any **input devices** are included in that controller.

Assigning a USB keyboard will **deprive Dom0 VM of a keyboard**. Since a USB controller assignment survives reboot, you may find yourself **unable to access your system**. Most non-Apple laptops have a PS/2 input for keyboard and mouse, so this problem does not exist.

But **if you need to use a USB keyboard or mouse**, identify the USB controller in which you have your keyboard/mouse plugged in and do NOT assign it to a VM. Also, makes sure you know all the other USB ports for that controller, and use them carefully, knowing **you are exposing Dom0** (ie NO bluetooth device on it).

All USB devices should be assumed **side channel attack vectors** (mic via sound, others via power usage), so you might prefer to remove them. [See this about rootkits](https://web.archive.org/web/20070829112704/http://www.networkworld.com/news/2007/080207-black-hat-virtual-machine-rootkit-detection.html)

Using a **web-cam** also involves a risk, so better to physically cover it with adhesive tape or disconnect it if you do not use it. If you need it, you need **to assign it to a VM** and cover it with a cap or an elastic band when not in use. Attaching a **microphone** using PedOS VM Manager may also be risky, so attach it only when required.

It is preferable to avoid using **Bluetooth** if you travel or do not trust your neighbours. Kids with high-gain directional antennas might also gain long range access to your Bluetooth. In this case, buy a computer that does not have a Bluetooth hardware module, or, if you have it, assign it to an untrusted VM. Assigning it to its own PedOS VM will also allow you to use Bluetooth without trusting it, if need be.

Many laptops allow one to disable various hardware (Camera, BT, Mic, etc) **in BIOS**. This might or might not be a dependable way of getting rid of those devices, depending on how much you trust your BIOS vendor.

If the VM will not start after you have assigned a USB controller, look at [this FAQ](/faq/#i-created-a-usbvm-and-assigned-usb-controllers-to-it-now-the-usbvm-wont-boot).


Creating and Using a USBVM
--------------------------

See [here](/doc/usb/).


Dom0 Precautions
----------------

As explained [here](/getting-started/#appvms-PedOS-and-templatevms), dom0 should not be used for any user operations. There are several reasons for this:

1.  Secure isolation among domUs (i.e., AppVMs, StandaloneVMs, HVMs, etc.) is the *raison d'être* of PedOS. This is the primary reason that we recommend the delegation of all user activities to some number of AppVMs. In the event that any given VM is compromised, only that particular VM is compromised. (TemplateVMs are the exception to this. If a TemplateVM were compromised, then every AppVM based on it might also be compromised. Even in this case, however, the entire system would not necessarily have been compromised, since StandaloneVM(s), HVM(s), and/or multiple TemplateVMs might be in use.) By contrast, if dom0 were ever compromised, the entire system would thereby be compromised.
2.  Due to the absence of convenience mechanisms in dom0 such as the inter-VM clipboard and inter-VM file copying, it is significantly less convenient to attempt to use dom0 for user operations (e.g., password management) in conjunction with AppVMs than it is to use another dedicated AppVM (e.g., a "vault" VM).
3.  Dom0 has access to every VM's data in the form of its private image file, including untrusted (e.g., red-bordered) VMs. If the user were to make a mistake (or be tricked into making one) and thereby inadvertently access untrusted files from dom0, those files could exploit the application which accessed them (e.g., a file manager) and gain control over dom0 and, therefore, the entire system. Even simply displaying the data in a [terminal emulator](http://securityvulns.com/docs4128.html) can be dangerous. For example, some file managers (such as the Thunar File Manager, which is pre-installed by default in the Xfce4 version of dom0) list loop devices used by running VMs. When one of these devices is selected in the file manager, the loop device is mounted to dom0, effectively [transferring the contents](https://groups.google.com/d/msg/PedOS-users/_tkjmBa9m9w/9BbKh94PVtcJ) of the home directory of a (by definition less trusted) AppVM to dom0.
4.  There is a (hopefully small, but always non-zero) chance that any given program is malicious. Even packages by third-party developers you trust might have been modified and then signed by an attacker who managed to get that developer's private key(s). For this reason, it is very important that as few programs as possible be run in dom0 in as restricted a manner as possible. For example, although GnuPG is used in dom0 for verifying updates received from the firewallvm, it does not follow that GnuPG should be used for regular user operations (e.g., key management) in dom0. This is because only a single GnuPG operation, the "verify signature" operation  (which is believed to be the most bulletproof operation in GnuPG), is used by default in dom0. No other key management operations (e.g., importing unverified keys) or any other data parsing takes place in dom0 by default.
5.  Any VM can be shut down in order to make it even more difficult for an adversary to access, and shutting down one VM does not restrict the user of other VMs. By contrast, one cannot shut down dom0 and use other VMs at the same time.
6.  As far as we are aware, there are no special mechanisms in Xen which make dom0 more protected than any other VM, so there is no inherent security advantage to performing any user operations in dom0.


TemplateBasedVM Directories
---------------------------

 * Once a TemplateBasedVM has been created, any changes in its `/home`,
   `/usr/local`, or `/rw/config` directories will be persistent across reboots,
   which means that any files stored there will still be available after
   restarting the TemplateBasedVM. No changes in any other directories in
   TemplateBasedVMs persist in this manner. If you would like to make changes
   in other directories which *do* persist in this manner, you must make those
   changes in the parent TemplateVM.
   
 * See [here](/doc/templates) for more detail and version specific information.
 
