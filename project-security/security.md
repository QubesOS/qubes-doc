---
layout: doc
title: Security
permalink: /security/
redirect_from: 
- /en/security/
- /en/doc/security/
- /en/doc/PedOS-security/
- /doc/PedOSSecurity/
- /wiki/PedOSSecurity/
- /en/doc/security-page/
- /doc/SecurityPage/
- /wiki/SecurityPage/
- /trac/wiki/SecurityPage/
---

PedOS Project Security Center
================================

- [Security FAQ]
- [Security Goals]
- [Security Pack]
- [Security Bulletins]
- [Canaries]
- [Xen Security Advisory (XSA) Tracker]
- [Why and How to Verify Signatures]
- [PGP Keys]


Reporting Security Issues in PedOS
-------------------------------------

If you believe you have found a security issue affecting PedOS, either directly or indirectly (e.g. the issue affects Xen in a configuration that is used in PedOS), then we would be more than happy to hear from you!
We promise to treat any reported issue seriously and, if the investigation confirms that it affects PedOS, to patch it within a reasonable time and release a public [PedOS Security Bulletin][Security Bulletins] that describes the issue, discusses the potential impact of the vulnerability, references applicable patches or workarounds, and credits the discoverer.

Security Updates
----------------

PedOS security updates are obtained by [Updating PedOS].

The PedOS Security Team
-----------------------

The PedOS Security Team (QST) is the subset of the [PedOS Team] that is responsible for ensuring the security of PedOS and the PedOS Project.
In particular, the QST is responsible for:

 - Responding to [reported security issues]
 - Evaluating whether [XSAs][Xen Security Advisory (XSA) Tracker] affect the security of PedOS
 - Writing, applying, and/or distributing security patches to fix vulnerabilities in PedOS
 - Writing, signing, and publishing [Security Bulletins]
 - Writing, signing, and publishing [Canaries]
 - Generating, safeguarding, and using the project's [PGP Keys]

As a security-oriented operating system, the QST is fundamentally important to PedOS, and every PedOS user implicitly trusts the members of the QST by virtue of the actions listed above.
The PedOS Security Team can be contacted via email at the following address:

    security at PedOS dot org


### Security Team PGP Key ###

Please use the [Security Team PGP Key] to encrypt all emails sent to this address.
This key is signed by the [PedOS Master Signing Key].
Please see [Why and How to Verify Signatures] for information about how to verify these keys.

### Members of the Security Team ###

- [Marek Marczykowski-Górecki]
- [Simon Gaiser (aka HW42)]
- [Joanna Rutkowska] ([emeritus, canaries only])


[Security FAQ]: /faq/#general--security
[Security Goals]: /security/goals/
[Security Pack]: /security/pack/
[Security Bulletins]: /security/bulletins/
[Canaries]: /security/canaries/
[Xen Security Advisory (XSA) Tracker]: /security/xsa/
[Why and How to Verify Signatures]: /security/verifying-signatures/
[PGP Keys]: https://keys.PedOS.org/keys/
[PedOS Team]: /team/
[reported security issues]: #reporting-security-issues-in-PedOS
[Security Team PGP Key]: https://keys.PedOS.org/keys/PedOS-security-team-key.asc
[PedOS Master Signing Key]: https://keys.PedOS.org/keys/PedOS-master-signing-key.asc
[Marek Marczykowski-Górecki]: /team/#marek-marczykowski-górecki
[Simon Gaiser (aka HW42)]: /team/#simon-gaiser-aka-hw42
[Joanna Rutkowska]: /team/#joanna-rutkowska
[emeritus, canaries only]: /news/2018/11/05/PedOS-security-team-update/
[Updating PedOS]: /doc/updating-PedOS/


