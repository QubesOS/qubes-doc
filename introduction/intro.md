---
layout: intro
title: Introduction
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

  <div class="row">
      <div class="col-lg-12 col-md-12">
          <p>Qubes OS is a free and open-source, security-oriented operating system for single-user desktop computing. Qubes OS leverages <a href="https://wiki.xen.org/wiki/Xen_Project_Software_Overview">Xen-based virtualization</a> to allow for the creation and management of isolated compartments called <a href="/doc/glossary#qube">qubes</a>.</p>
      </div>
  </div>
  <div class="row">
      <div class="col-lg-3 col-md-3 text-left">
          <p>These qubes, which are implemented as <a href="/doc/glossary#vm">virtual machines (VMs)</a>, have specific:</p>
          <ul>
            <li class="more-bottom"><b>Purposes:</b> with a predefined set of one or many isolated applications, for personal or professional projects, to manage the <a href="/doc/networking/">network stack</a>, <a href="/doc/firewall/">the firewall</a>, or to fulfill other user-defined purposes.</li>
            <li class="more-bottom"><b>Natures:</b> <a href="/doc/standalone-and-hvm/">full-fledged</a> or <a href="/getting-started/#appvms-qubes-and-templatevms">stripped-down</a> virtual machines based on popular operating systems, such as <a href="/doc/templates/fedora">Fedora</a>, <a href="/doc/templates/debian">Debian</a>, and <a href="/doc/windows/">Windows</a>.</li>
            <li class="more-bottom"><b>Levels of trust:</b> from complete to non-existent. All windows are displayed in a unified desktop environment with <a href="https://www.qubes-os.org/getting-started/">unforgeable colored window borders</a> so that different security levels are easily identifiable.</li>
          </ul>
      </div>
      <div class="col-lg-9 col-md-9">
        <a href="/attachment/site/qubesosdiagram.png"><img src="/attachment/site/qubesosdiagram.png" class="center-block more-bottom"></a>
      </div>
  </div>

<div class="alert alert-info more-bottom" role="alert">
    <i class="fa fa-question-circle"></i>
    <b>Note:</b> See our <a href="/doc/glossary/">glossary</a> and <a href="/faq">FAQ</a> for more information.
</div>

<h2 class="more-bottom">Features</h2>

  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Strong isolation</h3>
      <p>Isolate different pieces of software as if they were installed on separate physical machines using <a href="/doc/glossary/#pv">PV</a> or <a href="/doc/glossary/#hvm">HVM</a> virtualization techniques.</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Template system</h3>
      <p>Use <a href="/getting-started/#appvms-qubes-and-templatevms">AppVMs</a> to share a root file system without sacrificing security using the innovative <a href="/doc/templates/">Template system</a>.</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Multiple operating systems</h3>
      <p>Use multiple operating systems at the same time, including <a href="/doc/templates/fedora">Fedora</a>, <a href="/doc/templates/debian">Debian</a>, and <a href="/doc/windows/">Windows.</a></p>
    </div>
  </div>

  <hr class="add-top more-bottom">
  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>DisposableVMs</h3>
      <p>Create <a href="/doc/disposablevm/">DisposableVMs</a> on the fly that self-destruct when shut down.</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Whonix integration</h3>
      <p>Run <a href="https://www.torproject.org/">Tor</a> securely system-wide using <a href="/doc/whonix/">Whonix with Qubes</a>.</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Device isolation</h3>
      <p>Secure <a href="/doc/device-handling/">device handling</a> through isolation of network cards and USB controllers.</p>
    </div>
  </div>

  <hr class="add-top more-bottom">
  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Split GPG</h3>
      <p>Utilize <a href="/doc/split-gpg/">Split GPG</a> to keep your private keys safe.</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>U2F proxy</h3>
      <p>Operate <a href="/doc/u2f-proxy/">Qubes U2F proxy</a> to use your two-factor authentication devices without exposing your web browser to the full USB stack.</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Open-source</h3>
      <p>Users are free to use, copy, and modify Qubes OS and <a href="/doc/contributing/">are encouraged to do so!</a></p>
    </div>
  </div>

<div class="alert alert-info more-bottom" role="alert">
    <i class="fa fa-question-circle"></i>
    <b>Note:</b> Given the technical nature of Qubes OS, prior experience with Linux can be helpful.
</div>


<h2 class="more-bottom">Why Qubes OS?</h2>

<h3>Physical isolation is a given safeguard that the digital world lacks</h3>

  <div class="row">
      <div class="col-lg-6 col-md-6 text-left">
        <p>Throughout our lives, we engage in various activities, such as going to school, working, voting, taking care of our families, and visiting with friends. These activities are spatially and temporally bound: They happen in isolation from one another, in their own compartments, which often represent an essential safeguard, as in the case of voting.</p>
        <p>In our digital lives, the situation is quite different: All of our activities typically happen on a single device. This causes us to worry about whether it's safe to click on a link or install an app, since being hacked imperils our entire digital existence.</p>
        <p>Qubes eliminates this concern by allowing us to divide a device into many compartments, much as we divide a physical building into many rooms. Better yet, it allows us to create new compartments whenever we need them, and it gives us sophisticated tools for securely managing our activities and data across these compartments.</p>
      </div>
      <div class="col-lg-6 col-md-6">
        <a href="/attachment/wiki/GettingStarted/r2b1-qubes-manager-2.png"><img src="/attachment/wiki/GettingStarted/r2b1-qubes-manager-2.png" height="330" class="center-block more-bottom"></a>
      </div>
  </div>

<h3>Qubes allows you to compartmentalize your digital life</h3>

 <div class="row">
      <div class="col-lg-6 col-md-6">
        <a href="/attachment/site/qubes-partition-data-flows.jpg"><img src="/attachment/site/qubes-partition-data-flows.jpg" height="450" class="center-block more-bottom"></a>
      </div>
      <div class="col-lg-6 col-md-6 text-left center-block">
        <p>Many of us are initially surprised to learn that our devices do not support the kind of secure compartmentalization that our lives demand, and we're disappointed that software vendors rely on generic defenses that repeatedly succumb to new attacks.</p>
        <p>In building Qubes, our working assumption is that all software contains bugs. Not only that, but in their stampeding rush to meet deadlines, the world's stressed-out software developers are pumping out new code at a staggering rate &mdash; far faster than the comparatively smaller population of security experts could ever hope to analyze it for vulnerabilities, much less fix everything. Rather than pretend that we can prevent these inevitable vulnerabilities from being exploited, we've designed Qubes under the assumption that they <em>will</em> be exploited. It's only a matter of time until the next zero-day attack.</p>
        <p>In light of this sobering reality, Qubes takes an eminently practical approach: confine, control, and contain the damage. It allows you to keep valuable data separate from risky activities, preventing cross-contamination. This means you you can do everything on the same physical computer without having to worry about a single successful cyberattack taking down your entire digital life in one fell swoop. In fact, Qubes has <a href="https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf">distinct advantages over physical air gaps</a>.</p>
      </div>
  </div>

<h3>Made to support vulnerable users</h3>

 <div class="row">
    <div class="col-lg-12 col-md-12 text-left">
        <p>Qubes provides practical, usable security to vulnerable and actively-targeted individuals, such as journalists, activists, whistleblowers, and researchers. Qubes is designed with the understanding that people make mistakes, and it allows you to protect yourself from your own mistakes. It's a place where you can click on links, open attachments, plug in devices, and install software free from worry. It's a place where <em>you</em> have control over your software, not the other way around.</p>
    </div>
 </div>

 <p><a href="/attachment/wiki/GettingStarted/snapshot12.png"><img src="/attachment/wiki/GettingStarted/snapshot12.png" alt="snapshot12.png"/></a></p>

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

This page is just a brief introduction to what Qubes is all about, and many technical details have been omitted here for the sake of presentation.

 * If you're a current or potential Qubes user, you may want to check out the [documentation][doc] and the [user FAQ][user-faq].
 * If you're a developer, there's dedicated [developer documentation] and an [developer FAQ][devel-faq] just for you.
 * Ready to give Qubes a try? Head on over to the [downloads] page, and read the [installation guide].
 * Need help, or just want to join the conversation? Learn more about [help, support, the mailing lists, and the forum][support].


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
[doc]: /doc/
[user-faq]: /faq/#users
[developer documentation]: /doc/#developer-documentation
[devel-faq]: /faq/#developers
[downloads]: /downloads/
[getting started]: /getting-started/
[installation guide]: /doc/installation-guide/
[support]: /support/

