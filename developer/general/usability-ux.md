---
lang: en
layout: doc
redirect_from:
- /doc/usability-ux/
ref: 31
title: Usability & UX
---


Software that is too complicated to use, is often unused. Because we want as many people as possible to benefit from its unique security properties, the usability and user experience of Qubes OS is an utmost priority!

We ask anyone developing for Qubes OS to please read through this guide to better understand the user experience we strive to achieve. We also ask them to review [our style guide](/doc/style-guide/) for other design related information.

---

## Easy To Use

An ideal user experience is friendly, and it beckons a new user to explore the interface. In this process, they can naturally discover how to use the software. Below are some guidelines that will help you design a user interface that accomplishes this goal.

<div class="focus">
  <i class="fa fa-times"></i> <strong>Interfaces Should Not</strong>
</div>

- Require extensive configuration before a user can *begin* doing things
- Make it possible to break provided features or actions in unrecoverable ways
- Perform actions which compromise security and data
- Overwhelm the user with too much information and cognitive load

Perhaps the most common cause of mistakes is complexity. If there is a configuration setting that will significantly affect the user's experience, choose a safe and smart default then tuck this setting in an `Advanced Settings` panel.

<div class="focus">
  <i class="fa fa-check"></i> <strong>Interfaces Should</strong>
</div>

- Make it easy to discover features and available actions
- Provide some understanding of what discovered features do
- Offer the ability to easily undo mistakes
- Choose intelligent defaults for settings

In making software easy to use, it is crucial to be mindful of [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) which dictates that *"humans are generally able to hold only seven +/-  two units of information in short-term memory."* Making sure your interfaces don't pass this short-term memory limit is perhaps the most important factor in helping a user feel comfortable instead of overwhelmed.

---

## Easy to Understand

There will always be the need to communicate things to users. In these cases, an interface should aim to make this information easy to understand. The following are simple guides to help achieve this - none of these are absolute maxims!

<div class="focus">
  <i class="fa fa-times"></i> <strong>Avoid Acronyms</strong>
</div>

Acronyms are compact and make good names for command line tools. They do not make graphical user interfaces more intuitive for non-technical users. Until one learns an acronym's meaning, it is gibberish. Avoid acronyms in your interfaces whenever possible!

- `DVM` - Disposable Virtual Machine
- `GUID` - Global Unique Identifier
- `PID` - Process Identification Number
- `NetVM` - Networking Virtual Machine

Despite this rule, some acronyms like `USB` are widely used and understood due to being in common use for over a decade. It is good to use these acronyms when the full words like `Universal Serial Bus` are more likely to confuse users.

<div class="focus">
  <i class="fa fa-check"></i> <strong> Use Simple Words</strong>
</div>

Use the minimum amount of words needed to be descriptive, but also informative. Go with common words that are as widely understood. Sometimes, inventing a word such as `Qube` to describe a `virtual machine` makes the life of the user much easier.

- Use `Disposable Qube` instead of `DVM` or `Disposable Virtual Machine`
- Use `interface` instead of `GUI` or `Graphical User Interface`
- Use `application number` instead of `PID` or `Process Identification Number`
- Use `Networking` or `Networking Qube` instead of `NetVM` given context

---

<div class="focus">
  <i class="fa fa-times"></i> <strong> Avoid Technical Words</strong>
</div>

Technical words are usually more accurate, but they often *only* make sense to technical users and are confusing and unhelpful to non-technical users. Examples of technical words that might show up in Qubes OS are:

- `root.img`
- `savefile`
- `qrexec-daemon`

These are all terms that have at some point showed up in users' notification messages. Each term is very specific, but requires the user to understand virtualization to interpret.

<div class="focus">
  <i class="fa fa-check"></i> <strong> Use Common Concepts</strong>
</div>

Large amounts of the global population have been using computers for one or two decades and have formed some mental models of how things work. Leveraging these mental models are a huge gain.

- Use `disk space` instead of `root.img`, since while not quite accurate, it makes contextual sense
- Use `saving` instead of `savefile` as the former is the action trying to be completed
- Use `Qubes` instead of `qrexec-daemon` as it gives better context on what is happening

These words are more abstract and user relevant- they help a user understand what is happening based on already known concepts (disk space) or start to form a mental model of something new (Qubes).

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
  <i class="fa fa-times"></i> <strong>Avoid Duplicate Words</strong>
</div>

It is easy to add words like `Domain` before items in a list or menu in an attempt to be descriptive, such as:

~~~
Menu
- Domain: work
- Domain: banking
- Domain: personal
~~~

The repeated use of the word `Domain` requires a user to read it for each item in the list, which makes extra work for the eye in parsing out the relevant word like `work, banking, or personal`.  This also affects horizontal space on fixed width lines.

<div class="focus">
  <i class="fa fa-check"></i> <strong> Create Groups & Categories</strong>
</div>

It is more efficient to group things under headings instead as this allows the eye to easily scan the uniqueness of the items. (As per our previous example:)

~~~
Domains
- Work
- Banking
- Personal
~~~

---

## Easy To Complete

Lastly, expected (and unexpected) situations often require user actions or input. Make resolving these occurences as easy as possible to complete the action.

<div class="focus">
  <i class="fa fa-times"></i><strong>Don't Leave Users Stranded</strong>
</div>

Consider the following notifications:

- `The disk space of your Qube "Work" is full`
- `There was an error saving Qube "Personal"`

Instead of displaying solvable errors like these and neglecting to provide a fix:

<div class="focus">
  <i class="fa fa-check"></i><strong>Offer Actionable Solutions</strong>
</div>

Error messages and limits such as those in the previous example can be greatly improved by adding buttons or links to helpful information.

- Add a button to `Increase Disk Space`
- Add a link to a documentation page called `Troubleshoot saving data`

In adhering to these principles, you'll make undesirable situations more manageable for users instead of feeling stranded.

---

<div class="focus">
  <i class="fa fa-check"></i><strong>Minimize Repetitive Steps</strong>
</div>

There are many cases where a user wants to perform an action on more than one file or folder. However in order to do the action, the user must repeat certain steps such as:

1. Click on `Open File` from a menu or button
2. Navigate through file system
  - Click Folder One
  - Click Folder Two
  - Click Folder Three
  - Click Folder Four
3. Select proper file
4. Complete task on file

That subtle act of clicking through a file system can prove to be significant if a user needs to open more than a couple files in the same directory. We can alleviate some of the work by changing the process:

1. Click on `Open File` from a menu or button
2. Remember last open folder/file system
3. Select proper file
4. Complete task

Clearly, cutting out something as simple as navigating through the file system can save a user quite a bit of time. Alternatively, adding a button or menu item like `Open Multiple Files` might be even better, because remembering and using relevant hotkeys is often something only power users know how to do!

---

## GNOME, KDE, and Xfce

The desktop GUIs that QubesOS versions 1 - 3.1 offer are [KDE](https://www.kde.org) and [Xfce](https://xfce.org). We are currently migrating towards using [GNOME](https://www.gnome.org). We know some people prefer KDE, but we believe Gnome is easier to use for average non-technical users. Xfce will always be supported, and technical users will always have the choice to use KDE or other desktop environments.

This change means you should use [GTK](https://www.gtk.org/) rather than Qt for new GUIs.

All three of these mentioned desktop environments have their own [human interface guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines), and we suggest you familiarize yourself with the platform you developing for.

- [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/3.18/)
- [KDE HIG](https://techbase.kde.org/Projects/Usability/HIG)
- [Xfce UI Guidlines](https://wiki.xfce.org/dev/hig/general)

---

## Further Learning & Inspiration

Learning to make well designing intuitive interfaces and software is specialized skillset that can take years to cultivate, but if you are interested in furthering your understanding, we suggest the following resources:

- [Learn Design Principles](http://learndesignprinciples.com) by Melissa Mandelbaum
- [Usability in Free Software](http://jancborchardt.net/usability-in-free-software) by Jan C. Borchardt
- [Superheroes & Villains in Design](https://vimeo.com/70030549) by Aral Balkan
- [First Rule of Usability? Don’t Listen to Users](http://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/) by Jakob Nielsen
- [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) by Jakob Nielsen
- [Hack Design](https://hackdesign.org/) - online learning program
