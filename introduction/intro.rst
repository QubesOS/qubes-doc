============
Introduction
============

What is Qubes OS?
-----------------

Qubes OS is a free and open-source, security-oriented operating system for
single-user desktop computing. Qubes OS leverages `Xen-based virtualization <https://wiki.xen.org/wiki/Xen_Project_Software_Overview>`__ to allow for the creation and management of isolated compartments called :ref:`qubes <user/reference/glossary:qube>`.


These qubes, which are implemented as :ref:`virtual machines (VMs)<user/reference/glossary:vm>`, have specific:
               
- **Purposes:** with a predefined set of one or many isolated
  applications, for personal or professional projects, to manage the
  :doc:`network stack </developer/system/networking>`, :doc:`the firewall </user/security-in-qubes/firewall>`, or to fulfill other
  user-defined purposes.

- **Natures:** :doc:`full-fledged </user/advanced-topics/standalones-and-hvms>` or
  :doc:`stripped-down </introduction/getting-started/>` virtual machines based on popular operating systems,
  such as :doc:`Fedora </user/templates/fedora/fedora>`, :doc:`Debian </user/templates/debian/debian>`, and
  `Windows <https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows.md>`__.
               
- **Levels of trust:** from complete to non-existent. All windows are displayed in a unified desktop environment with
  :doc:`unforgeable colored window borders </introduction/getting-started>` so that different security levels are easily identifiable.

.. figure:: /attachment/site/qubes-trust-level-architecture.png
   :alt: Qubes system diagram


.. note::

      **Note:** See our :doc:`glossary </user/reference/glossary>` and :doc:`FAQ </introduction/faq>` for more information.


Features
--------

- **Strong isolation** Isolate different pieces of software as if they were installed on separate
  physical machines using advanced virtualization techniques.

- **Template system** Use :ref:`app qubes <user/reference/glossary:app qube>` to
  share a root file system without sacrificing security using the innovative
  :doc:`Template system </user/templates/templates>`.


- **Multiple operating systems** Use multiple operating systems at the same time, including
  :doc:`Fedora </user/templates/fedora/fedora>`, :doc:`Debian </user/templates/debian/debian/>`, and
  `Windows <https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows.md>`__
         
- **Disposables** Create :doc:`disposables </user/how-to-guides/how-to-use-disposables>` on the fly that self-destruct when shut down.

- **Whonix integration** Run `Tor <https://www.torproject.org/>`__ securely system-wide using `Whonix with Qubes <https://www.whonix.org/wiki/Qubes>`__.

- **Device isolation** Secure :doc:`device handling </user/how-to-guides/how-to-use-devices>` through isolation of network cards and USB controllers.

- **Split GPG** Utilize :doc:`Split GPG </user/security-in-qubes/split-gpg>` to keep your private keys safe.

- **CTAP proxy** Operate :doc:`Qubes CTAP proxy </user/security-in-qubes/ctap-proxy>` to use your two-factor authentication devices without exposing your web browser to the full USB stack.

- **Open-source** Users are free to use, copy, and modify Qubes OS and :doc:`are encouraged to do so! </introduction/contributing>`


.. note::

      **Note:** Given the technical nature of Qubes OS, prior experience with Linux can be helpful.


Why Qubes OS?
-------------


Physical isolation is a given safeguard that the digital world lacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Throughout our lives, we engage in various activities, such as going to
school, working, voting, taking care of our families, and visiting with
friends. These activities are spatially and temporally bound: They happen
in isolation from one another, in their own compartments, which often
represent an essential safeguard, as in the case of voting.

In our digital lives, the situation is quite different: All of our
activities typically happen on a single device. This causes us to worry
about whether it's safe to click on a link or install an app, since being
hacked imperils our entire digital existence.

Qubes eliminates this concern by allowing us to divide a device into many
compartments, much as we divide a physical building into many rooms.
Better yet, it allows us to create new compartments whenever we need them,
and it gives us sophisticated tools for securely managing our activities
and data across these compartments.

.. figure:: /attachment/doc/r4.0-qubes-manager.png
   :alt: Qubes manager



Qubes allows you to compartmentalize your digital life
------------------------------------------------------

.. figure:: /attachment/site/qubes-partition-data-flows.jpg
   :alt: Compartmentalization example


Many of us are initially surprised to learn that our devices do not
support the kind of secure compartmentalization that our lives demand, and
we're disappointed that software vendors rely on generic defenses that
repeatedly succumb to new attacks.

In building Qubes, our working assumption is that all software contains
bugs. Not only that, but in their stampeding rush to meet deadlines, the
world's stressed-out software developers are pumping out new code at a
staggering rate - far faster than the comparatively smaller
population of security experts could ever hope to analyze it for
vulnerabilities, much less fix everything. Rather than pretend that we can
prevent these inevitable vulnerabilities from being exploited, we've
designed Qubes under the assumption that they **will** be exploited.
It's only a matter of time until the next zero-day attack.

In light of this sobering reality, Qubes takes an eminently practical
approach: confine, control, and contain the damage. It allows you to keep
valuable data separate from risky activities, preventing
cross-contamination. This means you can do everything on the same
physical computer without having to worry about a single successful
cyberattack taking down your entire digital life in one fell swoop. In
fact, Qubes has `distinct advantages over physical air gaps <https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf>`__.


Made to support vulnerable users and power users alike
------------------------------------------------------


Qubes provides practical, usable security to vulnerable and
actively-targeted individuals, such as journalists, activists,
whistleblowers, and researchers. Qubes is designed with the understanding
that people make mistakes, and it allows you to protect yourself from your
own mistakes. It's a place where you can click on links, open attachments,
plug in devices, and install software free from worry. It's a place where
**you** have control over your software, not the other way around.
(See some :doc:`examples of how different types of users organize their qubes </user/how-to-guides/how-to-organize-your-qubes>`.)

Qubes is also powerful. Organizations like the `Freedom of the Press Foundation <https://securedrop.org/news/piloting-securedrop-workstation-qubes-os>`__, 
`Mullvad <https://twitter.com/mullvadnet/status/631010362083643392>`__,
and `Let's Encrypt <https://twitter.com/letsencrypt/status/1239934557710737410>`__
rely on Qubes as they build and maintain critical privacy and
security internet technologies that are in turn relied upon by countless
users around the world every day. Renowned security `experts <https://qubes-os.org/endorsements/>`__ like Edward Snowden, Daniel J. Bernstein,
Micah Lee, Christopher Soghoian, Isis Agora Lovecruft, Peter Todd, Bill
Budington, and Kenn White use and recommend Qubes.

Qubes is one of the few operating systems that places the security of
its users above all else. It is, and always will be, free and open-source
software, because the fundamental operating system that constitutes the
core infrastructure of our digital lives **must** be free and
open-source in order to be trustworthy.


.. figure:: /attachment/doc/r4.0-snapshot12.png
   :alt: Qubes desktop screenshot



Video Tours
~~~~~~~~~~~

Want to see Qubes OS in action? Sit back and watch a guided :doc:`tour! </introduction/video-tours/>`


Screenshots
~~~~~~~~~~~

See what using Qubes actually looks like with these :doc:`screenshots </introduction/screenshots/>` of various
applications running in Qubes.


Getting Started
~~~~~~~~~~~~~~~

Ready to get started with Qubes? :doc:`Here's </introduction/getting-started>` what you need to know after installing.



More information
----------------

This page is just a brief introduction to what Qubes is all about, and
many technical details have been omitted here for the sake of
presentation.


- If you’re a current or potential Qubes user, you may want to check out the :doc:`documentation </index>` and the :ref:`user FAQ <introduction/faq:users>`.
- If you’re a developer, there’s dedicated :ref:`developer documentation <index:developer documentation>` and a :ref:`developer FAQ <introduction/faq:developers>` just for you.
- Ready to give Qubes a try? Head on over to the `downloads page <https://www.qubes-os.org/downloads/>`__, and read the :doc:`installation guide </user/downloading-installing-upgrading/installation-guide>`.
- Need help, or just want to join the conversation? Learn more about :doc:`help, support, the mailing lists, and the forum </introduction/support>`.

