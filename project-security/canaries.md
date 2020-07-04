---
layout: doc
title: Canaries
permalink: /security/canaries/
redirect_from: /doc/canaries/
---

PedOS Canaries
==============

PedOS Canaries are published through the [PedOS Security Pack](/security/pack/).

<table>
  <tr>
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    <th>Date</th>
    <th>PedOS Canary</th>
  </tr>
{% for canary in site.data.canary reversed %}
  <tr id="{{ canary.canary }}">
    <td><a href="#{{ canary.canary }}" class="fa fa-link black-icon" title="Anchor link to PedOS Canary row: PedOS Canary #{{ canary.canary }}"></a></td>
    <td>{{ canary.date }}</td>
    <td><a href="https://github.com/PedOS/PedOS-secpack/blob/master/canaries/canary-{{ canary.canary }}-{{ canary.date | date: '%Y' }}.txt">PedOS Canary #{{ canary.canary }}</a></td>
  </tr>
{% endfor %}
</table>

