---
layout: team
title: Team
permalink: /team/
redirect_from:
- /people/
- /doc/QubesDevelopers/
- /wiki/QubesDevelopers/
---

<div id="team-core" class="white-box page-content more-bottom">
  <div class="col-lg-12 col-md-12 col-sm-12">
    <h2 class="text-center more-bottom">Core Team</h2>
  </div>
  {% for team in site.data.team %}
    {% if team.type == "core" %}
      <div class="row team team-core">
        <div class="col-lg-2 col-md-2 col-sm-5 col-xs-12 text-center">
        <div class="picture more-bottom">
          {% if team.picture %}
          <a href="/team/#{{team.name | slugify}}"><img src="/attachment/site/{{team.picture}}" title="Picture of {{team.name}}"></a>
          {% else %}
          <i class="fa fa-user"></i>
          {% endif %}
        </div>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-7 col-xs-12" id="{{team.name | slugify}}">
          {% assign name_array = team.name | split:" " %}
          <a href="/team/#{{team.name | slugify}}"><h4 class="half-bottom">{{team.name}}</h4></a>
          <em class="role half-bottom">{{team.role}}</em>
          {% if team.email %}
          <a href="mailto:{{team.email}}" class="add-right"><i class="fa fa-envelope fa-fw"></i> Email</a>
          {% endif %}
          {% if team.website %}
          <a href="{{team.website}}" class="add-right" target="blank"><i class="fa fa-globe fa-fw"></i> Website</a>
          {% endif %}
          {% if team.twitter %}
          <a href="https://twitter.com/{{team.twitter}}" target="blank"><i class="fa fa-twitter fa-fw"></i> Twitter</a>
          {% endif %}
        </div>
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 text-center">
          {% if team.fingerprint %}
          <span class="fingerprint" title="{{team.name}}'s PGP Key Fingerprint">{{team.fingerprint}}</span>
          {% endif %}
          {% if team.pgp_key %}
          <a href="{{team.pgp_key}}"><i class="fa fa-lock fa-fw"></i> {{name_array[0]}}'s PGP Key</a>
          {% endif %}
        </div>
      </div>
    {% endif %}
  {% endfor %}
  <div class="text-center more-bottom">
    <a href="/join/" class="btn btn-primary"><i class="fa fa-user-plus fa-fw white-icon"></i> Join the team!</a>
  </div>
</div>
<div class="white-box page-content more-bottom">
  <div class="col-lg-12 col-md-12 col-sm-12">
    <h2 class="text-center more-bottom">Emeritus</h2>
    <p>Emeriti are honorary members of the Qubes team who previously
    contributed to the project in a central way but who are no longer
    currently active.</p>
  </div>
  {% assign emeritus_total = 0 %}
  {% for team in site.data.team %}
    {% if team.type == "emeritus" %}
      {% assign emeritus_total = emeritus_total | plus:1 %}
    {% endif %}
  {% endfor %}
  {% assign emeritus_half = emeritus_total | divided_by:2 %}
  {% assign emeritus_shown = 0 %}
  <div class="row team">
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
    {% for team in site.data.team %}
      {% if team.type == "emeritus" %}
        {% if emeritus_shown < emeritus_half %}
          {% include team-simple.html %}
        {% elsif emeritus_shown == emeritus_half %}
    </div>
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
          {% include team-simple.html %}
        {% else %}
          {% include team-simple.html %}
        {% endif %}
      {% assign emeritus_shown = emeritus_shown | plus:1 %}
      {% endif %}
    {% endfor %}
    </div>
  </div>
</div>
<div class="white-box page-content more-bottom">
  <div class="col-lg-12 col-md-12 col-sm-12">
    <h2 class="text-center more-bottom">Community Contributors</h2>
    <p>Qubes would not be where it is today without the input of the many users,
    testers, and developers of all skill levels who have come together to form
    this thriving community. The community's discussions take place primarily on
    the <a href="/doc/mailing-lists/">Qubes mailing lists</a>.</p>
  </div>
  {% assign community_total = 0 %}
  {% for team in site.data.team %}
    {% if team.type == "community" %}
      {% assign community_total = community_total | plus:1 %}
    {% endif %}
  {% endfor %}
  {% assign community_half = community_total | divided_by:2 %}
  {% assign community_shown = 0 %}
  <div class="row team">
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
    {% for team in site.data.team %}
      {% if team.type == "community" %}
        {% if community_shown < community_half %}
          {% include team-simple.html %}
        {% elsif community_shown == community_half %}
    </div>
    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
          {% include team-simple.html %}
        {% else %}
          {% include team-simple.html %}
        {% endif %}
      {% assign community_shown = community_shown | plus:1 %}
      {% endif %}
    {% endfor %}
    </div>
  </div>
</div>

