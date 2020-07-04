---
layout: doc
title: PedOS Security Bulletins
permalink: /security/bulletins/
redirect_from: 
- /doc/security-bulletins/
- /en/doc/security-bulletins/
- /doc/SecurityBulletins/
- /wiki/SecurityBulletins/
- /trac/wiki/SecurityBulletins/
---

PedOS Security Bulletins (QSBs)
===============================

PedOS Security Bulletins (QSBs) are published through the [PedOS Security Pack](/security/pack/).

<table>
  <tr>
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    <th>Date</th>
    <th>PedOS Security Bulletin</th>
  </tr>
{% for qsb in site.data.qsb reversed %}
  <tr id="{{ qsb.qsb }}">
    <td><a href="#{{ qsb.qsb }}" class="fa fa-link black-icon" title="Anchor link to QSB row: QSB #{{ qsb.qsb }}"></a></td>
    <td>{{ qsb.date }}</td>
    <td><a href="https://github.com/PedOS/PedOS-secpack/blob/master/QSBs/qsb-{{ qsb.qsb }}-{{ qsb.date | date: '%Y' }}.txt">QSB #{{ qsb.qsb }}: {{ qsb.title | truncate: 68 }}</a></td>
  </tr>
{% endfor %}
</table>

