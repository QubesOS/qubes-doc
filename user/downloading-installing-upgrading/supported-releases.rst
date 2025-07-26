==================
Supported releases
==================


This page details the level and period of support for releases of operating systems in the Qubes ecosystem.

Qubes OS
--------


Qubes OS releases are supported for **six months** after each subsequent major or minor release (see :doc:`Version Scheme </developer/releases/version-scheme>`). The current release and past major releases are always available on the `Downloads <https://www.qubes-os.org/downloads/>`__ page, while all ISOs, including past minor releases, are available from our `download mirrors <https://www.qubes-os.org/downloads/#mirrors>`__.

.. list-table:: 
   :widths: 11 11 11 11 
   :align: center
   :header-rows: 1

   * - Qubes OS
     - Start Date
     - End Date
     - Status
   * - Release 1
     - 2012-09-03
     - 2015-03-26
     - Unsupported
   * - Release 2
     - 2014-09-26
     - 2016-04-01
     - Unsupported
   * - Release 3.0
     - 2015-10-01
     - 2016-09-09
     - Unsupported
   * - Release 3.1
     - 2016-03-09
     - 2017-03-29
     - Unsupported
   * - Release 3.2
     - 2016-09-29
     - 2019-03-28
     - Unsupported
   * - Release 4.0
     - 2018-03-28
     - 2022-08-04
     - Unsupported
   * - Release 4.1
     - 2022-02-04
     - 2024-06-18
     - Unsupported
   * - Release 4.2
     - 2023-12-18
     - TBD
     - Supported
   * - Release 4.3
     - TBD
     - TBD
     - In development
   


Note on patch releases
^^^^^^^^^^^^^^^^^^^^^^


Please note that patch releases, such as 3.2.1 and 4.0.1, do not designate separate, new major or minor releases of Qubes OS. Rather, they designate their respective major or minor releases, such as 3.2 and 4.0, inclusive of all package updates up to a certain point. For example, installing Release 4.0 and fully updating it results in the same system as installing Release 4.0.1. Therefore, patch releases are not displayed as separate rows on any of the tables on this page.

Dom0
----


The table below shows the OS used for dom0 in each Qubes OS release.

.. list-table:: 
   :widths: 11 11 
   :align: center
   :header-rows: 1

   * - Qubes OS
     - Dom0 OS
   * - Release 1
     - Fedora 13
   * - Release 2
     - Fedora 18
   * - Release 3.0
     - Fedora 20
   * - Release 3.1
     - Fedora 20
   * - Release 3.2
     - Fedora 23
   * - Release 4.0
     - Fedora 25
   * - Release 4.1
     - Fedora 32
   * - Release 4.2
     - Fedora 37
   


Note on dom0 and EOL
^^^^^^^^^^^^^^^^^^^^


Dom0 is isolated from domUs. DomUs can access only a few interfaces, such as Xen, device backends (in the dom0 kernel and in other VMs, such as the NetVM), and Qubes tools (gui-daemon, qrexec-daemon, etc.). These components are :doc:`security-critical </developer/system/security-critical-code>`, and we provide updates for all of them (when necessary), regardless of the support status of the base distribution. For this reason, we consider it safe to continue using a given base distribution in dom0 even after it has reached end-of-life (EOL).

Templates
---------


The following table shows select :doc:`template </user/templates/templates>` (and :doc:`standalone </user/advanced-topics/standalones-and-hvms>`) releases that are currently supported. Currently, only :doc:`Fedora </user/templates/fedora/fedora>` and :doc:`Debian </user/templates/debian/debian>` templates are officially supported by the Qubes OS Project. `Whonix <https://www.whonix.org/wiki/Qubes>`__ templates are supported by our partner, the `Whonix Project <https://www.whonix.org/>`__. Qubes support for each template ends when that upstream release reaches end-of-life (EOL), even if that release is included in the table below. Please see below for distribution-specific notes.

It is the responsibility of each distribution to clearly notify its users in advance of its own EOL dates, and it is users’ responsibility to heed these notices by upgrading to supported releases. As a courtesy to Qubes users, we attempt to pass along upstream EOL notices we receive for select distributions, but our ability to do this reliably is dependent on the upstream distribution’s practices. For example, if a distribution provides a mailing list similar to :ref:`qubes-announce <introduction/support:qubes-announce>`, which allows us to receive only very important, infrequent messages, including EOL announcements, we are much more likely to be able to pass along EOL notices to Qubes users reliably. Qubes users can always check the EOL status of an upstream release on the upstream distribution’s website (see `Fedora EOL <https://fedoraproject.org/wiki/End_of_life>`__ and `Debian Releases <https://wiki.debian.org/DebianReleases>`__).

.. list-table:: 
   :widths: 11 11 11 
   :align: center
   :header-rows: 1

   * - Qubes OS
     - Fedora
     - Debian
   * - Release 4.2
     - 41, 42
     - 12
   


Note on Debian support
^^^^^^^^^^^^^^^^^^^^^^


Debian releases have two EOL dates: regular and `long-term support (LTS) <https://wiki.debian.org/LTS>`__. See `Debian Production Releases <https://wiki.debian.org/DebianReleases#Production_Releases>`__ for a chart that illustrates this. Qubes support ends at the *regular* EOL date, *not* the LTS EOL date, unless a specific exception has been made.

Note on Whonix support
^^^^^^^^^^^^^^^^^^^^^^


`Whonix <https://www.whonix.org/wiki/Qubes>`__ templates are supported by our partner, the `Whonix Project <https://www.whonix.org/>`__. The Whonix Project has set its own support policy for Whonix templates in Qubes. Please see the `Qubes-Whonix version support policy <https://www.whonix.org/wiki/About#Qubes_Hosts>`__ for details.
