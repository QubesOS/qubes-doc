---
layout: doc
title: Security
permalink: /security/
redirect_from:
- /en/security/
- /en/doc/security/
- /en/doc/qubes-security/
- /doc/QubesSecurity/
- /wiki/QubesSecurity/
- /en/doc/security-page/
- /doc/SecurityPage/
- /wiki/SecurityPage/
- /trac/wiki/SecurityPage/
---

# Qubes OS Project Security Center

- [Security FAQ]
- [Security Goals]
- [Security Pack]
- [Security Bulletins]
- [Canaries]
- [Xen Security Advisory (XSA) Tracker]
- [Why and How to Verify Signatures]
- [PGP Keys]

## Reporting Security Issues in Qubes OS

If you believe you have found a security issue affecting Qubes OS, either directly or indirectly (e.g. the issue affects Xen in a configuration that is used in Qubes OS), then we would be more than happy to hear from you!
We promise to treat any reported issue seriously and, if the investigation confirms that it affects Qubes, to patch it within a reasonable time and release a public [Qubes Security Bulletin][Security Bulletins] that describes the issue, discusses the potential impact of the vulnerability, references applicable patches or workarounds, and credits the discoverer.

## Security Updates

Qubes security updates are obtained by [Updating Qubes OS].

## The Qubes Security Team

The Qubes Security Team (QST) is the subset of the [Qubes Team] that is responsible for ensuring the security of Qubes OS and the Qubes OS Project.
In particular, the QST is responsible for:

- Responding to [reported security issues]
- Evaluating whether [XSAs][Xen Security Advisory (XSA) Tracker] affect the security of Qubes OS
- Writing, applying, and/or distributing security patches to fix vulnerabilities in Qubes OS
- Writing, signing, and publishing [Security Bulletins]
- Writing, signing, and publishing [Canaries]
- Generating, safeguarding, and using the project's [PGP Keys]

As a security-oriented operating system, the QST is fundamentally important to Qubes, and every Qubes user implicitly trusts the members of the QST by virtue of the actions listed above.
The Qubes Security Team can be contacted via email at the following address:

```
security at qubes-os dot org
```

### Security Team PGP Key

Please use the [Security Team PGP Key] to encrypt all emails sent to this address.
This key is signed by the [Qubes Master Signing Key].
Please see [Why and How to Verify Signatures] for information about how to verify these keys.

### Members of the Security Team

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
[PGP Keys]: https://keys.qubes-os.org/keys/
[Qubes Team]: /team/
[reported security issues]: #reporting-security-issues-in-qubes-os
[Security Team PGP Key]: https://keys.qubes-os.org/keys/qubes-os-security-team-key.asc
[Qubes Master Signing Key]: https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
[Marek Marczykowski-Górecki]: /team/#marek-marczykowski-górecki
[Simon Gaiser (aka HW42)]: /team/#simon-gaiser-aka-hw42
[Joanna Rutkowska]: /team/#joanna-rutkowska
[emeritus, canaries only]: /news/2018/11/05/qubes-security-team-update/
[Updating Qubes OS]: /doc/updating-qubes-os/


