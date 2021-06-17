---
lang: en
layout: doc
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
ref: 217
title: Security Center
---

# Qubes OS Project Security Center

This page provides a central hub for topics pertaining to the security of the Qubes OS Project.
For topics pertaining to software security *within* Qubes OS, see [Security in Qubes](/doc/#security-in-qubes).
The following is a list of important project security pages:

- [Qubes Security Pack (`qubes-secpack`)](/security/pack/)
- [Qubes Security Bulletins (QSBs)](/security/bulletins/)
- [Qubes Canaries](/security/canaries/)
- [Xen Security Advisory (XSA) Tracker](/security/xsa/)
- [Verifying signatures](/security/verifying-signatures/)
- [PGP keys](https://keys.qubes-os.org/keys/)
- [Security FAQ](/faq/#general--security)

## Reporting Security Issues in Qubes OS

If you believe you have found a security issue affecting Qubes OS, either directly or indirectly (e.g. the issue affects Xen in a configuration that is used in Qubes OS), then we would be more than happy to hear from you!
We promise to treat any reported issue seriously and, if the investigation confirms that it affects Qubes, to patch it within a reasonable time and release a public [Qubes Security Bulletin](/security/bulletins/) that describes the issue, discusses the potential impact of the vulnerability, references applicable patches or workarounds, and credits the discoverer.

## Security Updates

Qubes security updates are obtained by [Updating Qubes OS](/doc/updating-qubes-os/).

## The Qubes Security Team

The Qubes Security Team (QST) is the subset of the [Qubes Team](/team/) that is responsible for ensuring the security of Qubes OS and the Qubes OS Project.
In particular, the QST is responsible for:

- Responding to [reported security issues](#reporting-security-issues-in-qubes-os)
- Evaluating whether [XSAs](/security/xsa/) affect the security of Qubes OS
- Writing, applying, and/or distributing security patches to fix vulnerabilities in Qubes OS
- Writing, signing, and publishing [Security Bulletins](/security/bulletins/)
- Writing, signing, and publishing [Canaries](/security/canaries/)
- Generating, safeguarding, and using the project's [PGP Keys](https://keys.qubes-os.org/keys/)

As a security-oriented operating system, the QST is fundamentally important to Qubes, and every Qubes user implicitly trusts the members of the QST by virtue of the actions listed above.
The Qubes Security Team can be contacted via email at the following address:

```
security at qubes-os dot org
```

### Security Team PGP Key

Please use the [Security Team PGP Key](https://keys.qubes-os.org/keys/qubes-os-security-team-key.asc) to encrypt all emails sent to this address.
This key is signed by the [Qubes Master Signing Key](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc).
Please see [Why and How to Verify Signatures](/security/verifying-signatures/) for information about how to verify these keys.

### Members of the Security Team

- [Marek Marczykowski-Górecki](/team/#marek-marczykowski-górecki)
- [Simon Gaiser (aka HW42)](/team/#simon-gaiser-aka-hw42)
- [Joanna Rutkowska](/team/#joanna-rutkowska) ([emeritus, canaries only](/news/2018/11/05/qubes-security-team-update/))

