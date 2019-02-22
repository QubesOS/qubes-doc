---
layout: security
title: Qubes Security Bulletins
permalink: /security/bulletins/
redirect_from: 
- /doc/security-bulletins/
- /en/doc/security-bulletins/
- /doc/SecurityBulletins/
- /wiki/SecurityBulletins/
- /trac/wiki/SecurityBulletins/
---

Qubes Security Bulletins (QSBs)
===============================

Qubes Security Bulletins (QSBs) are published through the [Qubes Security Pack](/security/pack/).

<table>
  <tr>
    <th>QSB</th>
    <th>Date</th>
    <th>Title</th>
  </tr>
{% for qsb in site.data.qsb %}
  <tr id="{{ qsb.qsb }}">
    <td><a href="#{{ qsb.qsb }}">{{ qsb.qsb }}</a></td>
    <td>{{ qsb.date }}</td>
    <td><a href="https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-{{ qsb.qsb }}-{{ qsb.date | date: '%Y' }}.txt">{{ qsb.title | truncate: 76 }}</a></td>
  </tr>
{% endfor %}
</table>

