---
layout: doc
title: Updating Debian and Whonix
permalink: /doc/troubleshooting/updating-debian-and-whonix/
---

Updating Debian and Whonix
==========================

Despite Qubes shipping with [Debian Templates](/doc/templates/debian/), most of Qubes core components run on Fedora and thus our documentation has better coverage for Fedora. However, Qubes has been working closely with the [Whonix](https://whonix.org) project which is based on Debian.

This troubleshooting guide is collection of tips about updating Whonix that also pertain to updating the normal Debian package manager. If you plan to use Debian heavily, **we highly recommend you install the Whonix templates and use them to update your normal Debian TemplateVM.**

*Note: some of the links on this page go to documentation on Whonix's website*

### Updating Error Messages

After running the commands to update Debian or Whonix, hopefully everything will complete perfectly.

~~~
sudo apt-get update && sudo apt-get dist-upgrade
~~~

However, if you see something like the following, then something went wrong.

~~~
W: Failed to fetch http://ftp.us.debian.org/debian/dist/jessie/contrib/binary-i386/Packages 404 Not Found

W: Failed to fetch http://ftp.us.debian.org/debian/dist/jessie/non-free/binary-i386/Packages 404 Not Found

E: Some index files failed to download. They have been ignored, or old ones used instead.

Err http://ftp.us.debian.org jessie Release.gpg
  Could not resolve 'ftp.us.debian.org'
Err http://deb.torproject.org jessie Release.gpg
  Could not resolve 'deb.torproject.org'
Err http://security.debian.org jessie/updates Release.gpg
  Could not resolve 'security.debian.org'
Reading package lists... Done
W: Failed to fetch http://security.debian.org/dists/jessie/updates/Release.gpg  Could not resolve 'security.debian.org'

W: Failed to fetch http://ftp.us.debian.org/debian/dists/jessie/Release.gpg  Could not resolve 'ftp.us.debian.org'

W: Failed to fetch http://deb.torproject.org/torproject.org/dists/jessie/Release.gpg  Could not resolve 'deb.torproject.org'

W: Some index files failed to download. They have been ignored, or old ones used instead.
~~~

This could be a temporary Tor exit relay or server failure that should fix itself. Here are some simple things to try:

- Check if your network connection is functional
- Try to [change your Tor circuit](https://www.whonix.org/wiki/Arm), then try again
- Running [whonixcheck](https://www.whonix.org/wiki/Whonixcheck) might also help diagnose the problem

Sometimes if you see a message such as:

~~~
Could not resolve 'security.debian.org'
~~~

It helps to run the following command:

~~~
nslookup security.debian.org
~~~

And then trying running the `update` and `upgrade` commands again.

~~~
sudo apt-get update && sudo apt-get dist-upgrade
~~~

*Please note: if you [disabled the Whonix APT Repository](https://www.whonix.org/wiki/Whonix-APT-Repository#Disable_Whonix_APT_Repository) you'll have to manually check for new Whonix releases and [manually install them from source code](https://www.whonix.org/wiki/Dev/Build_Documentation).*

### Never Install Unsigned Packages

If you see something like this:

~~~
WARNING: The following packages cannot be authenticated!
  icedove
Install these packages without verification [y/N]?
~~~

Don't proceed! Press `N` and `<enter>`. Running `apt-get update` again should fix it. If not, something is broken or it's a [Man in the middle attack](https://www.whonix.org/wiki/Warning#Man-in-the-middle_attacks), which isn't that unlikely, since we are updating over Tor exit relays and some of them are malicious. Try to [change your Tor circuit](https://www.whonix.org/wiki/Arm#Arm).


### Signature Verification Warnings

There should be none at the moment. If there was such a warning, it would look like this:

~~~
W: A error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://deb.torproject.org stable Release: The following signatures were invalid: KEYEXPIRED 1409325681 KEYEXPIRED 1409325681 KEYEXPIRED 1409325681 KEYEXPIRED 1409325681
~~~

Even though, `apt-get` will automatically ignore repositories with expired keys or signatures, you will not receive upgrades from that repository. Unless the issue is already known/documented, it should be reported so it can be further investigated.

There are two possible reasons why this could happen, either there is an issue with the repository that the maintainers have to fix, or you are victim of a [Man-in-the-middle_attacks](https://www.whonix.org/wiki/Warning#Man-in-the-middle_attacks). The latter would not be a big issue and might go away after a while automatically or try to [change your Tor circuit](https://www.whonix.org/wiki/Arm#Arm)

In past various apt repositories were signed with expired key. If you want to see how the documentation looked at that point, please click on expand on the right.

[The Tor Project's apt repository key was expired](https://trac.torproject.org/projects/tor/ticket/12994). You saw the following warning.

~~~
W: A error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://deb.torproject.org stable Release: The following signatures were invalid: KEYEXPIRED 1409325681 KEYEXPIRED 1409325681 KEYEXPIRED 1409325681 KEYEXPIRED 1409325681

W: Failed to fetch http://deb.torproject.org/torproject.org/dists/stable/Release  
W: Some index files failed to download. They have been ignored, or old ones used instead.
~~~

It had already been [reported](https://trac.torproject.org/projects/tor/ticket/12994). There was no immediate danger. You could have just ignored it. Just make sure, you never install unsigned packages as explained above.

If you were to see other signature verification errors, those should be reported, but it shouldn't happen at this time.

### Changed Configuration Files

If you see something like the following.

~~~
Setting up ifupdown ...
Configuration file /etc/network/interfaces
 ==> Modified (by you or by a script) since installation.
 ==> Package distributor has shipped an updated version.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : background this process to examine the situation
 The default action is to keep your current version.
*** interfaces (Y/I/N/O/D/Z) [default=N] ? N
~~~

Be careful. If the updated file isn't coming from Whonix specific package (some are called `whonix-...`), then press `n`. Otherwise anonymity/privacy/security settings deployed with Whonix might get lost. If you are an advanced user and know better, you can of course manually check the difference and merge them.

How could you find out if the file is coming from a Whonix specific package or not?

* Whonix specific packages are sometimes called `whonix-...`. In the example above it's saying `Setting up ifupdown ...`, so the file isn't coming from a Whonix specific package. In this case, you should press `n` as advised in the paragraph above.
* If the package name does include `whonix-...`, it's a Whonix specific package. In that case, your safest bet should be pressing `y`, but then you would lose your customized settings. You can re-add them afterwards. Such conflicts will hopefully rarely happen, if you use [Whonix modular flexible .d style configuration folders](https://www.whonix.org/wiki/Whonix_Configuration_Files).
