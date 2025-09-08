================================
Qubes OS project security center
================================


This page provides a central hub for topics pertaining to the security of the Qubes OS Project. For topics pertaining to software security *within* Qubes OS, see :ref:`security in Qubes <security-in-qubes>`. The following is a list of important project security pages:

- :doc:`Qubes security pack (qubes-secpack) </project-security/security-pack>`

- `Qubes security bulletins (QSBs) <https://www.qubes-os.org/security/qsb/>`__

- `Qubes canaries <https://www.qubes-os.org/security/canary/>`__

- `Xen security advisory (XSA) tracker <https://www.qubes-os.org/security/xsa/>`__

- :doc:`Verifying signatures </project-security/verifying-signatures>`

- `PGP keys <https://keys.qubes-os.org/keys/>`__

- :ref:`Security FAQ <introduction/faq:general \& security>`



Reporting security issues in Qubes OS
-------------------------------------


.. warning::

      **Please note:** The Qubes security team email address is intended for **responsible disclosure** by security researchers and others who discover legitimate security vulnerabilities. It is **not** intended for everyone who suspects they’ve been hacked. Please do not attempt to contact the Qubes security team unless you can **demonstrate** an actual security vulnerability or unless the team will be able to take reasonable steps to verify your claims.

If you’ve discovered a security issue affecting Qubes OS, either directly or indirectly (e.g., the issue affects Xen in a configuration that is used in Qubes OS), then we would be more than happy to hear from you! We promise to take all reported issues seriously. If our investigation confirms that an issue affects Qubes, we will patch it within a reasonable time and release a public `Qubes security bulletin (QSB) <https://www.qubes-os.org/security/qsb/>`__ that describes the issue, discusses the potential impact of the vulnerability, references applicable patches or workarounds, and credits the discoverer. Please use the `Qubes security team PGP key <https://keys.qubes-os.org/keys/qubes-os-security-team-key.asc>`__ to encrypt your email to this address:

.. code:: text

      security at qubes-os dot org



This key is signed by the `Qubes Master Signing Key <https://keys.qubes-os.org/keys/qubes-master-signing-key.asc>`__. Please see :doc:`verifying signatures </project-security/verifying-signatures>` for information about how to authenticate these keys.

Security updates
----------------


Qubes security updates are obtained by :doc:`updating Qubes OS </user/how-to-guides/how-to-update>`.

Qubes security team
-------------------


The **Qubes security team (QST)** is the subset of the `core team <https://www.qubes-os.org/team/#core-team>`__ that is responsible for ensuring the security of Qubes OS and the Qubes OS Project. In particular, the QST is responsible for:

- Responding to `reported security issues <#reporting-security-issues-in-qubes-os>`__

- Evaluating whether `XSAs <https://www.qubes-os.org/security/xsa/>`__ affect the security of Qubes OS

- Writing, applying, and/or distributing security patches to fix vulnerabilities in Qubes OS

- Writing, signing, and publishing `Qubes security bulletins (QSBs) <https://www.qubes-os.org/security/qsb/>`__

- Writing, signing, and publishing `Qubes canaries <https://www.qubes-os.org/security/canary/>`__

- Generating, safeguarding, and using the project’s `PGP keys <https://keys.qubes-os.org/keys/>`__



As a security-oriented operating system, the QST is fundamentally important to Qubes, and every Qubes user implicitly trusts the members of the QST by virtue of the actions listed above.

Members of the security team
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


- `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/#marek-marczykowski-górecki>`__

- `Simon Gaiser (aka HW42) <https://www.qubes-os.org/team/#simon-gaiser-aka-hw42>`__


