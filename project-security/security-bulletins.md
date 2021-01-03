---
layout: doc
title: Qubes Security Bulletins (QSBs)
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

A Qubes Security Bulletin (QSB) is a security announcement issued by the Qubes OS Project, typically providing a summary and impact analysis of one or more recently discovered software vulnerabilities, including details about patching to address them.
QSBs are published through the [Qubes Security Pack (qubes-secpack)](/security/pack/).

<table>
  <tr>
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    <th>Date</th>
    <th>Qubes Security Bulletin</th>
  </tr>
{% for qsb in site.data.qsb reversed %}
  <tr id="{{ qsb.qsb }}">
    <td><a href="#{{ qsb.qsb }}" class="fa fa-link black-icon" title="Anchor link to QSB row: QSB #{{ qsb.qsb }}"></a></td>
    <td>{{ qsb.date }}</td>
    <td><a href="https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-{{ qsb.qsb }}-{{ qsb.date | date: '%Y' }}.txt">QSB #{{ qsb.qsb }}: {{ qsb.title | truncate: 68 }}</a></td>
  </tr>
{% endfor %}
</table>

