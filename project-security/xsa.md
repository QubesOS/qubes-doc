---
layout: security
title: Xen Security Advisory (XSA) Tracker
permalink: /security/xsa/
---

Xen Security Advisory (XSA) Tracker
===================================

This tracker shows whether Qubes OS is affected by any given [Xen Security Advisory (XSA)][XSA].
Shortly after a new XSA is published, we will add a new row to this tracker.
Whenever Qubes is significantly affected by an XSA, a [Qubes Security Bulletin (QSB)][QSB] is published, and a link to that QSB is added to the row for the associated XSA.

Under the "Is Qubes Affected?" column, there are two possible values: **Yes** or **No**.

* **Yes** means that the *security* of Qubes OS *is* affected.
* **No** means that the *security* of Qubes OS is *not* affected.


Important Notes
---------------
* For the purpose of this tracker, we do *not* classify mere [denial-of-service (DoS) attacks][DoS] as affecting the *security* of Qubes OS.
  Therefore, if an XSA pertains *only* to DoS attacks against Qubes, the value in the "Is Qubes Affected?" column will be **No**.
* For simplicity, we use the present tense ("is affected") throughout this page, but this does **not** necessarily mean that up-to-date Qubes installations are *currently* affected by any particular XSA.
  In fact, it is extremely unlikely that any up-to-date Qubes installations are vulnerable to any XSAs on this page, since patches are almost always published concurrently with QSBs.
  Please read the QSB (if any) for each XSA for patching details.
* Embargoed XSAs are excluded from this tracker until they are publicly released, since the [Xen Security Policy] does not permit us to state whether Qubes is affected prior to the embargo date.
* Unused and withdrawn XSA numbers are included in the tracker for the sake of completeness, but they are excluded from the [Statistics] section for the sake of accuracy.
* All dates are in UTC.


Statistics
----------
{% assign date_first = site.data.xsa.first.date %}
{% assign date_first_epoch = date_first | date: "%s" %}
{% assign date_last = site.data.xsa.last.date %}
{% assign date_last_epoch = date_last | date: "%s" %}
{% assign timespan_epoch = date_last_epoch | minus: date_first_epoch %}
{% assign timespan_human = timespan_epoch | divided_by: 31536000.0 | round: 1 %}
{% assign xsa_total = site.data.xsa | size | plus: 1.0 %}
{% assign xsa_unused = 0.0 %}
{% assign xsa_affected = 0.0 %}
{% for xsa in site.data.xsa %}
  {% if xsa.affected == true %}
    {% assign xsa_affected = xsa_affected | plus: 1.0 %}
  {% endif %}
  {% if xsa.unused == true %}
    {% assign xsa_unused = xsa_unused | plus: 1.0 %}
  {% endif %}
{% endfor %}
{% assign xsa_used = xsa_total | minus: xsa_unused %}
{% assign affected_percentage = xsa_affected | divided_by: xsa_used | times: 100.0 | round: 2 %}

* Total time span: **{{ timespan_human }} years** ({{ date_first }} to {{ date_last }})
* Total XSAs published: **{{ xsa_used | round }}**
* Total XSAs affecting Qubes OS: **{{ xsa_affected | round }}**
* Percentage of XSAs affecting Qubes OS: **{{ affected_percentage }}%**

Tracker
-------
<table>
  <tr class="center">
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    <th>Date</th>
    <th title="Xen Security Advisory">XSA</th>
    <th>Is Qubes Affected?</th>
  </tr>
{% for xsa in site.data.xsa reversed %}
  <tr id="{{ xsa.xsa }}">
    <td><a href="#{{ xsa.xsa }}" class="fa fa-link black-icon" title="Anchor link to tracker row: XSA-{{ xsa.xsa }}"></a></td>
    <td>{{ xsa.date }}</td>
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
      {% if xsa.unused %}
        No (unused or withdrawn XSA number)
      {% elsif xsa.mitigation %}
        No (<a href="#{{ xsa.mitigation }}" title="No, the security of Qubes OS is not affected by XSA-{{ xsa.xsa }}. Click to read the explanation.">{{ xsa.mitigation }}</a>)
      {% else %}
        <span title="No, the security of Qubes OS is not affected by XSA-{{ xsa.xsa }}.">No</span>
      {% endif %}
    {% elsif xsa.affected == true %}
      <span title="Yes, the security of Qubes OS is affected by XSA-{{ xsa.xsa }}.">Yes</span>
      {% if xsa.qsb %}
        | <a href="https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-{{ xsa.qsb }}.txt" title="Qubes Security Bulletin {{ xsa.qsb }}">QSB-{{ xsa.qsb }}&nbsp;<span class="fa fa-external-link"></span></a>
      {% endif %}
    {% elsif xsa.affected == "tba" %}
      {% if xsa.tba %}
        <a href="{{ xsa.tba }}" title="To be announced. Click for more information.">TBA&nbsp;<span class="fa fa-external-link"></span></a>
      {% else %}
        <span title="To be announced">TBA</span>
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
[Xen Security Policy]: https://www.xenproject.org/security-policy.html
[Statistics]: #statistics

