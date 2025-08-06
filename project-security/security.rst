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
title: Qubes OS project security center
---

This page provides a central hub for topics pertaining to the security of the
Qubes OS Project. For topics pertaining to software security *within* Qubes OS,
see [security in Qubes](/doc/#security-in-qubes). The following is a list of
important project security pages:

- [Qubes security pack (qubes-secpack)](/security/pack/)
- [Qubes security bulletins (QSBs)](/security/qsb/)
- [Qubes canaries](/security/canary/)
- [Xen security advisory (XSA) tracker](/security/xsa/)
- [Verifying signatures](/security/verifying-signatures/)
- [PGP keys](https://keys.qubes-os.org/keys/)
- [Security FAQ](/faq/#general--security)

## Reporting security issues in Qubes OS

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Please note:</b> The Qubes security team email address is intended for
  <b>responsible disclosure</b> by security researchers and others who discover
  legitimate security vulnerabilities. It is <b>not</b> intended for everyone
  who suspects they've been hacked. Please <b>do not</b> attempt to contact the
  Qubes security team unless you can <b>demonstrate</b> an actual security
  vulnerability or unless the team will be able to take reasonable steps to
  verify your claims.
</div>

If you've discovered a security issue affecting Qubes OS, either directly or
indirectly (e.g., the issue affects Xen in a configuration that is used in
Qubes OS), then we would be more than happy to hear from you! We promise to
take all reported issues seriously. If our investigation confirms that an issue
affects Qubes, we will patch it within a reasonable time and release a public
[Qubes security bulletin (QSB)](/security/qsb/) that describes the issue,
discusses the potential impact of the vulnerability, references applicable
patches or workarounds, and credits the discoverer. Please use the [Qubes
security team PGP
key](https://keys.qubes-os.org/keys/qubes-os-security-team-key.asc) to encrypt
your email to this address:

```
security at qubes-os dot org
```

This key is signed by the [Qubes Master Signing
Key](https://keys.qubes-os.org/keys/qubes-master-signing-key.asc). Please see
[verifying signatures](/security/verifying-signatures/) for information about
how to authenticate these keys.

## Security updates

Qubes security updates are obtained by [updating Qubes
OS](/doc/how-to-update/).

## Qubes security team

The **Qubes security team (QST)** is the subset of the [core
team](/team/#core-team) that is responsible for ensuring the security of Qubes
OS and the Qubes OS Project. In particular, the QST is responsible for:

- Responding to [reported security
  issues](#reporting-security-issues-in-qubes-os)
- Evaluating whether [XSAs](/security/xsa/) affect the security of Qubes OS
- Writing, applying, and/or distributing security patches to fix
  vulnerabilities in Qubes OS
- Writing, signing, and publishing [Qubes security bulletins
  (QSBs)](/security/qsb/)
- Writing, signing, and publishing [Qubes canaries](/security/canary/)
- Generating, safeguarding, and using the project's [PGP
  keys](https://keys.qubes-os.org/keys/)

As a security-oriented operating system, the QST is fundamentally important to
Qubes, and every Qubes user implicitly trusts the members of the QST by virtue
of the actions listed above.

### Members of the security team

- [Marek Marczykowski-Górecki](/team/#marek-marczykowski-górecki)
- [Simon Gaiser (aka HW42)](/team/#simon-gaiser-aka-hw42)
