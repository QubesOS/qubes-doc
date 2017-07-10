---
layout: doc
title: Martus
permalink: /doc/martus/
---

Martus
======

[Martus] is a free, open source, secure information collection and management tool 
that empowers rights activists to be stronger in their fight against injustice and abuse.

To install Martus in a qube:

1. Create a Debian 8 backports template using the Qubes VM Manager or running
   `qvm-clone debian-8 debian-8-backports` in dom0.

2. Add backports to the sources for the new template by opening a terminal in
   the new template, run `sudo vi /etc/apt/sources.list` and add
   `deb http://http.debian.net/debian jessie-backports main`.

   (If you are new to `vi` text editing, type `i` to be able to edit, and when
   done editing press `ESC` then type `:x` and press `ENTER`.)

3. Update source list: `sudo apt-get update`.

4. Install `openjdk` and `openjfx` from backports:
   `sudo apt-get -t jessie-backports install openjdk-8-jre openjfx`.

5. You may need to install `unzip` to be able to unzip Martus after you
   download it: `sudo apt-get install unzip`.

6. Create a new qube/appvm based on your `debian-8-martus` template with
   whatever color and networking you want (`sys-whonix` probably preferred)
   using the Qubes VM Manager or running
   `qvm-create -t debian-8-backports -l blue martus` and
   `qvm-prefs -s martus netvm sys-whonix` in dom0.

7. Download the latest Martus version from https://martus.org.

8. Unzip the Martus package `unzip Martus-5.1.1.zip`.

9. `cd` into new folder: `cd Martus-5.1.1`.

10. Run Martus: `java -jar martus.jar`.


[Martus]: https://martus.org/

