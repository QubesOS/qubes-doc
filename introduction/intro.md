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

  <div class="row">
      <div class="col-lg-3 col-md-3 text-left">
          <p>Qubes OS is a free and open-source security-oriented operating system meant for single-user desktop computing.</p> 
          <p>Qubes OS leverages <a href="https://wiki.xen.org/wiki/Xen_Project_Software_Overview">xen-based virtualization</a> to allow for the creation and management of isolated virtual machines called <a href="/doc/glossary#qube">qubes</a>. 
          Qubes, which are implemented as <a href="/doc/glossary#vm">virtual machines (VMs)</a>, have specific :</p>
          <ul>
            <li><b>Purposes</b> : with a predefined set of one or many isolated applications, for personal or professional projects, to manage the <a href="/doc/networking/">network stack</a>, <a href="/doc/firewall/">the firewall</a>, or to fulfill other user-defined purposes.</li>
            <li><b>Natures</b> : <a href="/doc/standalone-and-hvm/">full-fledged</a> or <a href="/getting-started/#appvms-qubes-and-templatevms">stripped-down</a> virtual machines which are based on popular operating systems such as <a href="/doc/templates/fedora">Fedora</a>, <a href="/doc/templates/debian">Debian</a> or <a href="/doc/windows/">Windows</a>.</li>
            <li><b>Levels of trust</b> : from complete to non-existent. All windows are displayed in a unified desktop environment with <a href="https://www.qubes-os.org/getting-started/">unforgeable colored window borders</a> so different security levels are easily identifiable.</li>
          </ul>
      </div>
      <div class="col-lg-9 col-md-9">
        <h3 class="text-center add-bottom">Qubes OS Overview Example</h3>
        <img src="/attachment/site/qubesosdiagram.png" class="center-block">
      </div>
  </div>

<div class="alert alert-info" role="alert">
    <i class="fa fa-question-circle"></i>
    <b>Note : </b> Head over to the <a href="/doc/glossary/">glossary</a> or the <a href="/faq">FAQ</a> for more information.  
</div>

<h2>Features</h2>

  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Strong isolation</h3>
      <p>Isolate software as if they were installed on separate physical machines using <a href="/doc/glossary/#pv">PV</a> or <a href="/doc/glossary/#hvm">HVM</a> virtualization techniques</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Template system</h3>
      <p> Allow qubes called <a href="/getting-started/#appvms-qubes-and-templatevms">AppVMs</a> to share a root file system without sacrificing security using the innovative <a href="/doc/templates/">Template system</a></p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Multiple operating systems</h3>
      <p> Use multiple operating systems at the same time, including <a href="/doc/templates/fedora">Fedora</a>, <a href="/doc/templates/debian">Debian</a>, or <a href="/doc/windows/">Windows</a></p>
    </div>
  </div>

  <hr class="add-top more-bottom">
  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Disposable VMs</h3>
      <p>Create <a href="/doc/disposablevm/">disposable VMs</a> which are spawned quickly and destroyed when closed</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Whonix integration</h3>
      <p> Run <a href="https://www.torproject.org/">Tor</a> securely system-wide using <a href="/doc/whonix/">Whonix with Qubes</a></p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Controller isolation</h3>
      <p>Secure <a href="/doc/device-handling/">device handling</a> through isolation of network cards and USB controllers</p>
    </div>
  </div>

  <hr class="add-top more-bottom">
  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Split GPG</h3>
      <p>Utilize <a href="/doc/split-gpg/">Split GPG</a> to store private GPG keys in an AppVM</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>U2F proxy</h3>
      <p>Operate <a href="/doc/u2f-proxy/">Qubes U2F proxy</a> to use two-factor authentication</p>
    </div>
    <div class="col-lg-4 col-md-4 col-xs-12">
      <h3>Open-source</h3>
      <p>Users are free to use, copy and modify Qubes OS and <a href="/doc/contributing/">are encouraged to do so!</a></p>
    </div>
  </div>

<div class="alert alert-info" role="alert">
    <i class="fa fa-question-circle"></i>
    <b>Note : </b> Given the technical nature of Qubes OS, prior experience with a Linux distribution such as Ubuntu, Debian or Fedora is advisable.
</div>


Why Qubes OS ?
--------------

<h3>Physical isolation is a given safeguard that the digital world lacks</h3>

  <div class="row">
      <div class="col-lg-6 col-md-6 text-left">
        <p>Throughout their lives, individuals engage in various activities such as going to school, working, voting, taking care of their families or visiting with friends. </p> 
        <p>These activities are spatially and temporally bound : they happen in isolation of one another, in their own compartments, which often represent an essential safeguard, such as in the case of voting.</p> 
        <p>In one's digital life, the situation is quite different : each activity, often intertwined with its real-life counterpart, tends to happen on a single computing device.</p>
      </div>
      <div class="col-lg-6 col-md-6">
        <img src="/attachment/wiki/GettingStarted/r2b1-qubes-manager-2.png" height="300" class="center-block">
      </div>
  </div>

<h3>Qubes OS compartmentalizes one's digital life</h3>

 <div class="row">
      <div class="col-lg-3 col-md-3">
        <img src="/attachment/icons/128x128/apps/qubes-logo-icon.png" height="128" class="center-block">
      </div>
      <div class="col-lg-9 col-md-9 text-left">
        <p> Surprisingly, personal computing devices are not designed to offer means to enforce the same kind of isolation that people enjoy in the physical world.</p>
        <p>What if there were an operating system that provided a kind of digital compartmentalization almost as strong as physical isolation?</p> 
        <p>Qubes OS allows users to compartmentalize various parts of their digital lives into well-isolated compartments.</p> 
      </div>
  </div>

<h3>Made to support vulnerable users</h3>

 <div class="row">
    <div class="col-lg-12 col-md-12 text-left">
        <p>Thanks to Qubes OS, vulnerable or actively targeted individuals such as journalists, political activists, whistleblowers or researchers can enjoy the same benefits of using multiple computing devices at a fraction of the cost and without the associated loss of usability.</p>
        <p> It allows users to do everything on the same physical computer without having to worry about a single successful cyberattack taking down their entire digital life in one fell swoop.</p>
        <p>Computing should remain an activity where mistakes can be made and where users can explore the web freely, downloading attachments and clicking on links without having to constantly evaluate a myriad of risk factors.</p> 
        <p>Qubes OS strives to bring back this experience. It creates a place where users can feel safe.</p>
    </div>
 </div>

 <p><img src="/attachment/wiki/GettingStarted/snapshot12.png" alt="snapshot12.png"/></p>

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

This page is just a brief introduction to what Qubes is all about, and many
technical details have been omitted here for the sake of presentation.

 * If you're a current or potential Qubes user, you may want to check out the
   [documentation][doc] and the [FAQ][user-faq].
 * If you're a developer, there's dedicated [documentation][system-doc]
   and an [FAQ][devel-faq] just for you.
 * Ready to give Qubes a try? Head on over to the [downloads] page or the [installation guide].


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
[installation guide]: /doc/installation-guide/
