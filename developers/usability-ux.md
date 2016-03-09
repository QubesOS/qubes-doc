---
layout: doc
title: Usability & UX
permalink: /doc/usability-ux/
---

Usability & UX
==============

If software is too complicated to use, it often goes unused. Thus, usability and user experience of Qubes OS is an utmost priority for us, as we want as many people as possible to benefit from the unique security properties of Qubes OS!

We ask anyone developing for Qubes OS to please read through this guide to better understand the user experience we strive to achieve. Also, please review [our style guide](/doc/style-guide/) for other design related information.

---

## Easy To Use

An ideal user experience is friendly and welcomes a new user to explore the interface and in this process easily discover *how* to use the software. Additionally, security focused software has the responsibility of providing safety to a user and their data.

<div class="focus">
  <i class="fa fa-times"></i> <strong>Interfaces Should Not</strong>
</div>

- Require numerous settings to be entered before a user can *begin* doing things
- Allow breaking provided features or actions in unrecoverable ways
- Perform actions which compromise security and data
- Overwhelm with too much information and cognitive load

Perhaps the most common cause of mistakes is complexity. Thus, if there is a configuration setting that will significantly affect the user experience, choose a safe and smart default then tuck this setting in an `Advanced Settings` panel.

<div class="focus">
  <i class="fa fa-check"></i> <strong>Interfaces Should</strong>
</div>

- Make it easy to discover features and available actions
- Provide some understanding of what discovered features do
- Offer the ability to easily undo mistakes
- Choose intelligent defaults for settings

A crucial thing in making software easy to use, is being mindful of [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) which dictates that *"humans are generally able to hold only seven +/-  two units of information in short-term memory."* This short-term memory limit is perhaps the most important factor in helping a user feel comfortable instead of overwhelmed.


---

## Easy to Understand

There will always be the need to communicate things to users. In these cases, an interface should aim to make this information easy to understand. The following are simple guides to help achieve this- none these are absolute maxims!

<div class="focus">
  <i class="fa fa-times"></i> <strong>Avoid Acronyms</strong>
</div>

Acronyms are short and make good names for command line tools. Acronyms do not make graphical user interfaces more intuitive for non-technical users. Until one learns an acronyms meaning, it is otherwise meaningless. Avoid acronyms whenever possible!

- `DVM` - Disposable Virtual Machine
- `GUID` - Graphic User Interface Domain
- `PID` - Process Identification
- `NetVM` - Networking Virtual Machine

<div class="focus">
  <i class="fa fa-check"></i> <strong> Use Simple Words</strong>
</div>

Use the minimum amount of words needed to be descriptive, but also informative. Go with common words that are as widely understood as possible. Sometimes, inventing a word such as `Qube` to describe a `virutal machine` in the context of Qubes OS, is a good idea.

- Use `Disposable Qube` instead of `DVM`
- Use `interface` instead of `GUI`
- Use `application` instead of `PID`
- Use `Networking` or `Networking Qube` instead of `NetVM` given context

However, acronyms like `USB` are widely used and understood due to being in common use for over a decade. It is good to use these acronyms, as the full words `Universal Serial Bus` is more likely to confuse users.

---

<div class="focus">
  <i class="fa fa-times"></i> <strong> Avoid Technical Words</strong>
</div>

Technical words are usually more accurate, but they often *only* make sense to technical users and are confusing and unhelpful to non-technical users. Examples of technical words that might show up in Qubes OS are:

- `root.img`
- `savefile`
- `qrexec-daemon`

These are all terms that have at some point showed up in notification messages presented users. Each term is very accurate, but requires understanding virtualization

<div class="focus">
  <i class="fa fa-check"></i> <strong> Use Common Concepts</strong>
</div>

Large amounts of the global population have been using computers for one or two decades and have formed some mental models of how things work. Leveraging these mental models are a huge gain.

- Use `disk space` instead of `root.img` while not quite accurate, it makes contextual sense
- Use`saving` instead of `savefile` as the former is the action trying to be completed
- Use `Qubes` instead of `qrexec-daemon` as it is the larger context what is happening

While these words are less accurate or precise, they help a user understand what is happening based on already known concepts (disk space) or start to form a mental model of something new (Qubes).

---

<div class="focus">
  <i class="fa fa-times"></i> <strong>Avoid Inconsistencies</strong>
</div>

It is easy to start abbreviating (or making acronyms) of long terms like `Disposable Virtual Machine` depending on where the term shows up in an interface.

- `DVM`
- `DispVM`
- `DisposableVM`

This variation in terms can cause new users to question or second guess what the three different variations mean, which can lead to inaction or mistakes.

<div class="focus">
  <i class="fa fa-check"></i> <strong> Make Things Consistent</strong>
</div>

Always strive to keep things consistent in the interfaces as well as documentation and other materials.

- Use `Disposable Qube` at all times as it meets other criteria as well.

By using the same term throughout an interface, a user can create a mental model and relationship with that term allowing them to feel empowered.

---

<div class="focus">
  <i class="fa fa-times"></i> <strong>Avoid Unneeded Redundancies</strong>
</div>

It is easy when trying to be descriptive and accurate to add words like `Domain` before items in a list or menu such as:

~~~
Menu
- Domain: work
- Domain: banking
- Domain: personal
~~~

The redundant use of `Domain` requires a users to read it for each item in the list- this takes extra time for the eye to parse to exact the word they are looking for, such as `work, banking, or personal`. This also affects horizontal space on fixed width lines.

<div class="focus">
  <i class="fa fa-check"></i> <strong> Create Groups & Categories</strong>
</div>

It is better to group things under headings like `Domains` as this allows the eye to easily scan the uniqueness of the items

~~~
Domains
- Work
- Banking
- Personal
~~~

---

## Easy To Resolve

Lastly, expected (and unexpected) situations will happen which require user actions or input. Make resolving of these actions as easy as possible.

<div class="focus">
  <i class="fa fa-times"></i> <strong>Do Not Strand Users</strong>
</div>

Consider the following notifications which are shown to a user

- `The disk space of your Qube "Work" is full`
- `There was an error saving that Qube`

<div class="focus">
  <i class="fa fa-check"></i> <strong> Offer Solutions</strong>
</div>

Add buttons or links to helpful information that a user can engage with to overcome the issue they experienced

- Add a button `Increase Disk Space`
- Add a link to documentation `Troubleshoot saving data`

Adhering to these principles, make undesirable situations more manageable for users.

---

## GNOME, KDE, and Xfce

The the desktop GUIs which QubesOS versions 1 - 3.1 offer are [KDE](https://www.kde.org), as well as [Xfce](https://xfce.org). We are currently migrating towards using [GNOME](https://www.gnome.org). We know some people prefer KDE, however, we believe the overalluser  experience of GNOME is more focused on simplicity and ease of use for average non-technical users. Xfce will always be supported, and technical users will always be able to still use KDE or other desktop environments.

All three desktop environments have their own [human interface guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines) and we suggest you familiarize yourself with the platform you developing for.

- [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/3.18/)
- [KDE HIG](https://techbase.kde.org/Projects/Usability/HIG)
- [Xfce UI Guidlines](https://wiki.xfce.org/dev/hig/general)

---

## Further Learning & Inspiration

Learning to make well designing intuitive interfaces and software is specialized skillset that can take years to cultivate, but if you are interested in furthering your understanding of usability and experience, we suggest the following resources.

- [Learn Design Principles](http://learndesignprinciples.com) by Melissa Mandelbaum
- [Usability in Free Software](http://jancborchardt.net/usability-in-free-software) by Jan C. Borchardt
- [Superheroes & Villains in Design](https://vimeo.com/70030549) by Aral Balkan
- [First Rule of Usability? Don’t Listen to Users](http://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/) by  by Jakob Nielsen
- [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) by Jakob Nielsen
- [Hack Design](https://hackdesign.org/) - online learning program
