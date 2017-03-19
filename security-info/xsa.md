---
layout: security
title: Xen Security Advisory (XSA) Tracker
permalink: /security/xsa/
---

Xen Security Advisory (XSA) Tracker
===================================

**Notice:** This page is still under construction.
Until this notice is removed, the information below may not be accurate.
We appreciate your patience.

This tracker shows whether Qubes OS is affected by any given [Xen Security Advisory (XSA)][XSA].
Shortly after a new XSA is published, we will add a new row to this tracker.
Whenever Qubes is significantly affected by an XSA, a [Qubes Security Bulletin (QSB)][QSB] is published, and a link to that QSB is added to the row for the associated XSA.

Under the "Is Qubes Affected?" column, there are two possible values: **Yes** or **No**.

 * **Yes** means that the *security* of Qubes OS *is* affected.
 * **No** means that the *security* of Qubes OS is *not* affected.

Important Notes
---------------

* For the purpose of this tracker, we do *not* classify mere [denial-of-service (DoS) attacks][DoS] as affecting the *security* of Qubes OS.
  Therefore, if an XSA pertains *only* to DoS attacks against Qubes, the value in this column will be **No**.

* For simplicitly, we use the present tense ("is affected") throughout this page, but this does **not** necessarily mean that up-to-date Qubes installations are *currently* affected by any particular XSA.
  Please read the QSB (if any) for each XSA for patching details.

<table>
  <tr>
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    <th title="Xen Security Advisory">XSA</th>
    <th>Is Qubes Affected?</th>
  </tr>
{% for xsa in site.data.xsa %}
  <tr id="{{ xsa.xsa }}">
    <td><a href="#{{ xsa.xsa }}" class="fa fa-link black-icon" title="Anchor link to tracker row: XSA-{{ xsa.xsa}}"></a></td>
    <td>
      <a title="Xen Security Advisory {{ xsa.xsa }}"
      {% if xsa.xsa <= 25 %}
        href="https://wiki.xenproject.org/wiki/Security_Announcements_(Historical)"
      {% else %}
        href="https://xenbits.xen.org/xsa/advisory-{{ xsa.xsa }}.html"
      {% endif %}>
      XSA-{{ xsa.xsa }}&nbsp;<span class="fa fa-external-link"></span></a>
    </td>
    <td>
    {% if xsa.affected == false %}
      {% if xsa.mitigation %}
        No (<a href="#{{ xsa.mitigation }}" title="No, the security of Qubes OS is not affected by XSA-{{ xsa.xsa }}. Click to read the explanation.">{{ xsa.mitigation }}</a>)
      {% else %}
        <span title="No, the security of Qubes OS is not affected by XSA-{{ xsa.xsa }}.">No</span>
      {% endif %}
    {% elsif xsa.affected == true %}
      <span title="Yes, the security of Qubes OS is affected by XSA-{{ xsa.xsa }}.">Yes</span>
      {% if xsa.qsb %}
        | <a href="https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-{{ xsa.qsb }}.txt" title="Qubes Security Bulletin {{ xsa.qsb }}">QSB-{{ xsa.qsb }}&nbsp;<span class="fa fa-external-link"></span></a>
      {% endif %}
    {% else %}
    {% endif %}
    </td>
  </tr>
{% endfor %}
</table>


[XSA]: https://xenbits.xen.org/xsa/
[QSB]: /security/bulletins/
[DoS]: https://en.wikipedia.org/wiki/Denial-of-service_attack

