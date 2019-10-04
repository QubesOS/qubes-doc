---
layout: intro
title: An Introduction to Qubes OS
permalink: /intro/
redirect_from:
- /tour/
- /en/tour/
- /tour/#what-is-qubes-os
- /about/
- /en/about/
---

What is Qubes OS?
-----------------

Qubes OS is a free and open-source security-oriented operating system meant for single-user desktop computing. 

Qubes OS allows you to compartmentalize various parts of your digital life into isolated domains. If one of those compartments get compromised by a malicious email attachment carrying a ransomware, other parts of your system will remain unaffected : this is one of the key benefits of the [*security by compartmentalization*](https://www.qubes-os.org/faq/) approach taken by Qubes OS.

How does Qubes OS provide security?
------------------------------------

Behind the scenes, Qubes OS leverages virtualization and more specifically the [open-source Xen hypervisor](https://wiki.xen.org/wiki/Xen_Project_Software_Overview) to allow the creation and management of well-isolated virtual machines called *qubes*. Those qubes, which are also referred simply to as *domains* or *compartments*, have specific :

* **Purposes** : for personal or professional projects, to manage the USB or network stack.
* **Natures** : full-fledged or stripped-down virtual machines which can be based on Fedora, Debian or even Windows.
* **Levels of trust** : from complete to non-existent. 

All of these isolated qubes are integrated into a single, usable system. Programs are isolated in their own separate qubes, but all windows are displayed in a single, unified desktop environment with [unforgeable colored
window borders][getting started] so that you can easily identify windows from different security levels. Common attack vectors like network cards and USB controllers are isolated in their own hardware qubes while their functionality
is preserved through secure [networking], [firewalls], and [USB device management][USB]. Integrated [file] and [clipboard] copy and paste operations make it easy to work across various qubes without compromising security. The
innovative [Template] system separates software installation from software use, allowing qubes to share a root filesystem without sacrificing security (and saving disk space, to boot). Qubes even allows you to sanitize PDFs and images in a few clicks. Users concerned about privacy will appreciate the [integration][Qubes-Whonix] of [Whonix] with Qubes, which makes it easy to use [Tor] securely, while those concerned about physical hardware attacks will
benefit from [Anti Evil Maid].

Qubes OS is open
----------------

Another distinct features of Qubes OS is that as a user, you are free to use, copy and modify it. In other words, Qubes OS is a free and open-source software. The source code, including the documentation, is openly available so that others can contribute to and audit it, which we strongly encourage you to do ! 


<hr class="add-top more-bottom">
  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Video Tours</h3>
      <p>Want to see Qubes OS in action? Sit back and watch a guided tour!</p>
      <a href="/video-tours/" class="btn btn-primary">
        <i class="fa fa-play-circle"></i> Video Tours
      </a>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Screenshots</h3>
      <p>See what using Qubes actually looks like with these screenshots of various applications running in Qubes.</p>
      <a href="/screenshots/" class="btn btn-primary">
        <i class="fa fa-picture-o"></i> Screenshots
      </a>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Getting Started</h3>
      <p>Ready to get started with Qubes? Here's what you need to know after installing.</p>
      <a href="/getting-started/" class="btn btn-primary">
        <i class="fa fa-cubes"></i> Getting Started
      </a>
    </div>
  </div>

More information
----------------

This page is just a brief sketch of what Qubes is all about, and many
technical details have been omitted here for the sake of presentation.

 * If you're a current or potential Qubes user, you may want to check out the
   [documentation][doc] and the [FAQ][user-faq].
 * If you're a developer, there's dedicated [documentation][system-doc]
   and an [FAQ][devel-faq] just for you.
 * Ready to give Qubes a try? Head on over to the [downloads] page.


[disposable qube]: /doc/disposablevm/
[networking]: /doc/networking/
[firewalls]: /doc/firewall/
[USB]: /doc/usb/
[file]: /doc/copying-files/
[clipboard]: /doc/copy-paste/
[Template]: /doc/templates/
[Qubes-Whonix]: /doc/whonix/
[Whonix]: https://www.whonix.org/
[Tor]: https://www.torproject.org/
[Anti Evil Maid]: /doc/anti-evil-maid/
[Tails]: https://tails.boum.org/
[Xen]: https://www.xenproject.org
[paper-compart]: https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf
[doc]: /doc/
[user-faq]: /faq/#users
[system-doc]: /doc/system-doc/
[devel-faq]: /faq/#developers
[downloads]: /downloads/
[getting started]: /getting-started/

