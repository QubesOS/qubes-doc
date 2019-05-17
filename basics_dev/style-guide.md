---
layout: doc
title: Style-guide
permalink: /doc/style-guide/
---

Style Guide
===========

## Fonts

Currently Qubes OS is using the following fonts for our website, branding, and other public facing (non-OS) materials. The OS itself uses what is normal for a user's desktop environment of choice.

<div class="styleguide">
{% for font in site.data.styleguide.fonts %}
  <div class="row">
  <div class="col-lg-6 col-md-6 focus">
    <div class="font {{font.class}}">Custom Qubes Font</div>
  </div>
  <div class="col-lg-6 col-md-6">
    <strong>Family:</strong> {{font.family}}<br>
  </div>
  </div>
{% endfor %}
</div>

---

## Colors

The following **grayscale** colors are currently used on the Qubes website and documentation, and they will eventually match colors within the OS itself.

<div class="styleguide">
{% for color in site.data.styleguide.colors %}
  {% if color.type == "grayscale" %}
  <div class="swatch more-bottom more-right">
    <div class="color add-bottom bg-{{color.class}}"></div>
    <strong class="add-bottom">{{color.name}}</strong>
    <code>#{{color.hex | downcase}}</code>
  </div>
  {% endif %}
{% endfor %}
</div>

The following **colors** are currently being used on the Qubes website and documentation, and they will eventually match the colors within the OS itself!

<div class="styleguide">
{% for color in site.data.styleguide.colors %}
  {% if color.type == "colors" %}
  <div class="swatch more-bottom more-right">
    <div class="color add-bottom bg-{{color.class}}"></div>
    <strong class="add-bottom">{{color.name}}</strong>
    <code>#{{color.hex | downcase}}</code>
  </div>
  {% endif %}
{% endfor %}
</div>

---

## Icons

Currently, all the icons on the Qubes-OS.org website are generated using [FontAwesome](http://fortawesome.github.io/Font-Awesome/).

*As more custom work is done to generate icons for the operating system itself, they will be added here!*

---

## Logos

The following is a collection of various sizes and versions of the Qubes logo used both in the OS itself and on our website.
The artwork is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).
The code is licensed under GNU GPLv2.
GPLv2 and the source code can be [downloaded here](https://github.com/QubesOS/qubes-artwork).

<div class="styleguide">
{% for logo in site.data.styleguide.logos %}
  {% for version in logo.versions %}
  <div class="row more-bottom">
    <div class="col-lg-4 col-md-4">
      <div class="focus">
        <img class="logo" src="{{version.path}}{{logo.image}}">
      </div>
    </div>
    <div class="col-lg-8 col-md-8">
      <p>
        <strong>Image:</strong> {{logo.image}}<br>
        <strong>Size:</strong> {{version.size}}<br>
        <strong>Format:</strong> {{version.format}}<br>
        <strong>Download:</strong> <a href="{{version.path}}{{logo.image}}" target="_blank">this image</a>
      </p>
    </div>
  </div>
  {% endfor %}
{% endfor %}
</div>
