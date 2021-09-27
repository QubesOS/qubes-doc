---
lang: en
release: 4.0
reviewed: yes
layout: doc
permalink: /doc/website-style-guide/
title: Website style guide
---

This page explains the standards we follow for building and maintaining the
website. Please follow these guidelines and conventions when modifying the
website. For the standards governing the documentation in particular, please
see the [documentation style guide](/doc/documentation-style-guide/).

## Coding conventions

The following conventions apply to the website as a whole, including everything
written in HTML, CSS, YAML, and Liquid. These conventions are intended to keep
the codebase consistent when multiple collaborators are working on it. They
should be understood as a practical set of rules for maintaining order in this
specific codebase rather than as a statement of what is objectively right or
good.

### General practices

- Use comments to indicate the purposes of different blocks of code. This makes
  the file easier to understand and navigate.

- Use descriptive variable names. Never use one or two letter variable names.
  Avoid obscure abbreviations and made-up words.

- In general, make it easy for others to read your code. Your future self will
  thank you, and so will your collaborators!

- [Don't Repeat Yourself
  (DRY)!](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) Instead of
  repeating the same block of code multiple times, abstract it out into a
  separate file and `include` that file where you need it.

### Whitespace

- Always use spaces. Never use tabs.

- Each indentation step should be exactly two (2) spaces.

- Whenever you add an opening tag, indent the following line. (Exception: If
  you open and close the tag on the same line, do not indent the following
  line.)

- Indent Liquid the same way as HTML.

- In general, the starting columns of every adjacent pair of lines should be no
  more than two spaces apart (example below).

- No blank or empty lines. (Hint: When you feel you need one, add a comment on
  that line instead.)

#### Indentation example

Here's an example that follows the indentation rules:

{% raw %}
```html
<table>
  <tr>
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    {% for item in secs.htmlsections[0].columns %}
      <th>{{ item.title }}</th>
    {% endfor %}
  </tr>
  {% for canary in site.data.sec-canary reversed %}
    <tr id="{{ canary.canary }}">
      <td><a href="#{{ canary.canary }}" class="fa fa-link black-icon" title="Anchor link to Qubes Canary row: Qubes Canary #{{ canary.canary }}"></a></td>
      <td>{{ canary.date }}</td>
      <td><a href="https://github.com/QubesOS/qubes-secpack/blob/master/canaries/canary-{{ canary.canary }}-{{ canary.date | date: '%Y' }}.txt">Qubes Canary #{{ canary.canary }}</a></td>
    </tr>
  {% endfor %}
</table>
```
{% endraw %}
