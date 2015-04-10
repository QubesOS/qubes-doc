---
layout: doc
title: QubesR3Building
permalink: /doc/QubesR3Building/
redirect_from: /wiki/QubesR3Building/
---

Building Qubes OS 3.0 ISO
=========================

Ensure your system is rpm-based and that you have necessary dependencies installed (see [QubesBuilder](/wiki/QubesBuilder) for more info):

{% highlight trac-wiki %}
sudo yum install git createrepo rpm-build make wget rpmdevtools pandoc
{% endhighlight %}

Get the necessary keys to verify the sources:

{% highlight trac-wiki %}
$ wget https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
$ gpg --import qubes-master-signing-key.asc 
$ gpg --edit-key 36879494
# Verify fingerprint!, set trust to *ultimate*
$ wget https://keys.qubes-os.org/keys/qubes-developers-keys.asc
$ gpg --import qubes-developers-keys.asc
{% endhighlight %}

Note we do *not* relay above on the security of our server (keys.qubes-os.org) nor the connection (ssl, cert) -- we only rely on you getting the Qubes Master Signing Key fingerprint *somehow* and ensure they match!

Now lets bootstrap the builder. Unfortunately the builder cannot verify itself (the classic Chicken and Egg problem), so we need to verify the signature manually:

{% highlight trac-wiki %}
$ git clone git://git.qubes-os.org/qubes-r3/qubes-builder.git
$ cd qubes-builder
$ git describe --exact-match HEAD
<some tag>
$ git tag -v <some tag>
{% endhighlight %}

Assuming the verification went fine, we're good to go with all the rest without ever thinking more about verifying digital signatures on all the rest of the components, as the builder will do that for us, for each component, every time we, even for all aux files (e.g. Xen or Linux kernel sources).

Let's configure the builder first (we can use one of the example configs, either for R2 or "master", which currently means pre-released R3):

{% highlight trac-wiki %}
cp example-configs/qubes-os-master.conf builder.conf
{% endhighlight %}

You can take a loot at the `builder.conf.default` for a description of all available options. Nevertheless, the default config should be enough for start:

{% highlight trac-wiki %}
$ make get-sources qubes
$ make sign-all # this requires setting SIGN_KEY in the builder.conf, can be skipped for test builds.
$ make iso
{% endhighlight %}

Enjoy your new ISO!
