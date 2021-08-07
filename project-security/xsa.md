---
lang: en
layout: doc
permalink: /security/xsa/
ref: 214
title: Xen security advisory (XSA) tracker
---

This tracker shows whether Qubes OS is affected by any given [Xen security
advisory (XSA)](https://xenbits.xen.org/xsa/). Shortly after a new XSA is
published, we will add a new row to this tracker. Whenever Qubes is
significantly affected by an XSA, a [Qubes security bulletin
(QSB)](/security/qsb/) is published, and a link to that QSB is added to
the row for the associated XSA.

Under the "Is Qubes Affected?" column, there are two possible values: **Yes**
or **No**.

* **Yes** means that the *security* of Qubes OS *is* affected.
* **No** means that the *security* of Qubes OS is *not* affected.

## Important notes

* For the purpose of this tracker, we do *not* classify mere [denial-of-service
  (DoS) attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack) as
  affecting the *security* of Qubes OS. Therefore, if an XSA pertains *only* to
  DoS attacks against Qubes, the value in the "Is Qubes Affected?" column will
  be **No**.
* For simplicity, we use the present tense ("is affected") throughout this
  page, but this does **not** necessarily mean that up-to-date Qubes
  installations are *currently* affected by any particular XSA. In fact, it is
  extremely unlikely that any up-to-date Qubes installations are vulnerable to
  any XSAs on this page, since patches are almost always published concurrently
  with QSBs. Please read the QSB (if any) for each XSA for patching details.
* Embargoed XSAs are excluded from this tracker until they are publicly
  released, since the [Xen security
  policy](https://www.xenproject.org/security-policy.html) does not permit us
  to state whether Qubes is affected prior to the embargo date.
* Unused and withdrawn XSA numbers are included in the tracker for the sake of
  completeness, but they are excluded from the [statistics](#statistics)
  section for the sake of accuracy.
* All dates are in UTC.
