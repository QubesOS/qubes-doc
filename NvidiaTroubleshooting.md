---
layout: doc
title: NvidiaTroubleshooting
permalink: /doc/NvidiaTroubleshooting/
redirect_from: /wiki/NvidiaTroubleshooting/
---

NVidia Troubleshooting Guide
============================

If you have an NVidia graphics card it will probably not work under Xen out of the box. If your system freezes during boot and you don't see the graphical login manager after you installed Xen, then this problem most likely affects you. The following steps should provide a work around so that you should be able to use your NVidia with X under Xen, however without any fancy "desktop effects".

1.  Boot your system using the "failsafe" boot menu, that should have been automatically added to your `grub.conf` when you installed the Dom0 kernel.

If the X Window System doesn't start now, this is probably a non-Xen related issue and this guide will probably not help you.

Assuming your X Window System works fine now when you booted from the "failsafe" configuration, do the next steps...

1.  Do not log into X, but instead switch to a text console (press Ctrl-Alt-F2)

1.  Log in as root

1.  Switch to runlevel 3 (this should kill your X server):

{% highlight trac-wiki %}
init 3
{% endhighlight %}

1.  Run X-autoconfiguration:

{% highlight trac-wiki %}
Xorg -configure
{% endhighlight %}

This should generate a file `xorg.conf.new` in the `/root` directory.

In most cases you can ignore any warning or error messages displayed by the X server, assuming it generated the xorg.conf.new file.

1.  Edit this newly generated `xorg.conf.new` file and introduce the following two modifications:

-   Uncomment the ShadowFB option, so that you should now have something like this:

    {% highlight trac-wiki %}
    Option     "ShadowFB"                   # [<bool>]
    {% endhighlight %}

-   Change the driver name to `nouveau` (you will probably have `nv` written there):

    {% highlight trac-wiki %}
    Driver      "nouveau"
    {% endhighlight %}

Save the modification, exit the editor.

1.  Move the file to `/etc/X11` and rename it as `xorg.conf`:

{% highlight trac-wiki %}
mv /root/xorg.conf.new /etc/X11/xorg.conf
{% endhighlight %}

1.  Verify that X will work with those new settings:

{% highlight trac-wiki %}
xinit
{% endhighlight %}

If you see a terminal window in the top left corner, it means you most likely succeeded, even if your keyboard or mouse do not work now (don't worry about them).

1.  Reboot and let the system boot from the normal boot configuration. You should be able to use X under Xen now.

