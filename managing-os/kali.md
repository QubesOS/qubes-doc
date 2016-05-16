---
layout: doc
title: How to create a Kali Linux VM
permalink: /doc/kali/
---

How to Create a Kali Linux VM
=============================

This guide is being created to give guidance on ways in which you could implement Kali Pen-Testing distrubution within Qubes-OS.

There are multiple ways in which this can be achieved, for example you could create a HVM and use the ISO to install the system straight to that virtual machine.


Build Based on Debian Template
---

1 - Install debian-8 template (if not already installed)

2 - Clone debian-8 template

3 - Add kali repo to /etc/apt/sources.list:

    * deb http://http.kali.org/kali kali-rolling main non-free contrib
    
4 - Find and add kali signing keys:

    * gpg --key-server hkp://key.gnupg.net --recv-key 7D8D0BF6 (this is the key ID I found on Kali web site)
    
    * gpg --list-keys --with-fingerprint 7D8D0BF6 
    
    * gpg --export --armor 7D8D0BF6 > kali.asc 
    
    * sudo apt-key add kali.asc 
    
    * sudo apt-key list 
    
5 - sudo apt-get update 

6 - sudo halt 

7 - backup template (cloned...) 

8 - sudo apt-get apt-get install kali-*** (or similar) --> installs fine but break the template X settings. As mentioned, X packaged need to be masked prior to this, I did not take the time to look-up how to do that... 

9 - Create a appvm from the kali template and attach necessary devices.


Note:

If you do not want to modify the sources.list file and add the signing keys yourself, alternatively you can use KATOOLIN after cloning the Debian Template. Guide on how to use KATOOLIN - http://www.tecmint.com/install-kali-linux-tools-using-katoolin-on-ubuntu-debian/ 



Alternative Options to Kali
---

PenTester Framework (PTF)


