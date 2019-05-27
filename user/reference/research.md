---
layout: default
title: Research
permalink: /research/
redirect_from:
- /doc/qubes-research/
- /en/doc/qubes-research/
- /doc/QubesResearch/
- /wiki/QubesResearch/
---

Here are links to various research papers, projects, and blog posts that relate
to Qubes OS.

{% for category in site.data.research.categories %}
  <h3>{{category.name}}</h3>
  <ul class="add-top more-bottom">
  {% for paper in site.data.research.papers %}
    {% if paper.category == category.slug %}
    <li>
      <a href="{{paper.url}}">{{paper.title}}</a> by {{paper.author}}{% if paper.date %}, {{paper.date}}{% endif %}
    </li>
    {% endif %}
  {% endfor %}
  </ul>
{% endfor %}
