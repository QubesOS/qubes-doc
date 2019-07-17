---
layout: doc
title: SecBrowser
permalink: /doc/secbrowser/
---

SecBrowser
==========

[SecBrowser](https://www.whonix.org/wiki/SecBrowser) is a security-focused browser that provides vulnerability surface reduction for users that need high security, thereby reducing the risk of infection from malicious, arbitrary code. A built-in security slider provides enhanced usability, as website features which have historically been used as attack vectors (like JavaScript) can be easily disabled.  Without any customization, SecBrowser’s default configuration offers better security than Firefox, Google Chrome or Microsoft Edge.<sup>[[1]](https://2019.www.torproject.org/projects/torbrowser/design/)</sup> It also provides better protections from online tracking, [fingerprinting](https://www.whonix.org/wiki/Data_Collection_Techniques) and the [linkability](https://www.whonix.org/wiki/Data_Collection_Techniques#Fingerprinting_of_Browser_.28HTTP.29_Header) of activities across different websites.

SecBrowser is a derivative of the Tor Browser Bundle, but without Tor. This means unlike Tor Browser, SecBrowser does not route traffic over the Tor network. Even without the aid of the Tor network, SecBrowser still benefits from the numerous [patches](https://gitweb.torproject.org/tor-browser.git) that Tor developers have merged into the code base. Even with developer skills, these enhancements would be arduous and time-consuming to duplicate in other browsers, with the outcome unlikely to match SecBrowser's many security benefits. While browser extensions can be installed to mitigate specific attack vectors, this ad hoc approach is insufficient. SecBrowser leverages the combines experience and knowledge of the Tor Project developers, Whonix developers and the battle-tested Tor Browser. 


Security Enhancements
------------------------------------

**Table:** _SecBrowser Security and Privacy Benefits_


| **Features**                          | **Description**                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTTPS Everywhere                      | This browser extension encrypts communications with many major websites, making your browsing more secure.<sup>[[2]](https://www.eff.org/https-everywhere)</sup>                                                                                                                                                                                                       |
| NoScript                              | NoScript can provide significant protection with the correct configuration.<sup>[[3]](https://en.wikipedia.org/wiki/NoScript)</sup> NoScript blocks active (executable) web content and protects against [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS). "The add-on also offers specific countermeasures against security exploits". |
| DNS and Proxy Configuration Obedience | Proxy obedience is achieved through custom patches, Firefox proxy settings, and build flags. Plugins which can bypass proxy setting are disabled.<sup>[[4]](https://2019.www.torproject.org/projects/torbrowser/design/#proxy-obedience)</sup>                                                                                                                         |
| Reproducible Builds                   | Build security is achieved through a reproducible build process that enables anyone to produce byte-for-byte identical binaries to the ones the Tor Project releases.<sup>[[5]](https://blog.torproject.org/deterministic-builds-part-two-technical-details)</sup><sup>[[6]](https://2019.www.torproject.org/projects/torbrowser/design/#BuildSecurity)</sup>              |
| Slider Security                       | Enables improved security by disabling certain web features that can be used as attack vectors.<sup>[[7]](https://tb-manual.torproject.org/security-slider/)</sup><sup>[[8]](https://2019.www.torproject.org/projects/torbrowser/design/#proxy-obedience)</sup>                                                                                                             |
| WebRTC Disabled by Default            | WebRTC can compromise the security of VPN tunnels, by exposing the external (real) IP address of a user.<sup>[[9]](https://en.wikipedia.org/wiki/WebRTC#Concerns)</sup><sup>[[10]](https://torrentfreak.com/huge-security-flaw-leaks-vpn-users-real-ip-addresses-150130/)</sup>                                                                                              |

Settings
--------

While SecBrowser has numerous security enhancements they can come at a cost of decreased usability. Since it is also highly configurable, security settings and behavior can be customized according to personal requirements.

* **Private Browsing Mode:** In the default configuration Tor Browser has private browsing mode enabled. This setting prevents browsing and download history as well as cookies from remaining persistent across browser restarts. While private browsing mode increases security, usability can be affected to the point that some websites will not function properly or not at all.<sup>[[11]](https://trac.torproject.org/projects/tor/ticket/10569)</sup> To enhance usability  SecBrowser comes packaged with a custom `user_pref` that disables private browsing mode. If privacy is paramount users can enable private browsing mode by commenting out the corresponding user preference.

* **Security Slider:** By default the security slider is set to "Safest" which is the highest security setting.This will prevent some web pages from functioning properly, so security needs must be weighed against the degree of usability that is required. 

* **Persistent NoScript Settings:** SecBrowser includes a `user_pref` that allows custom NoScript settings to persist across browser sessions. This is a security vs usability trade-off.

* **Remember Logins and Passwords for Sites:** To increase usability, users have the option to save site login information such as user names or passwords.  

Privacy and Fingerprinting Resistance 
-------------------------------------

Research from a pool of 500,000 Internet users has shown that the vast majority (84%) have unique browser configurations and version information which makes them trackable across the Internet. When Java or Flash is installed, this figures rises to 94%.<sup>[[12]](https://www.eff.org/deeplinks/2010/05/every-browser-unique-results-fom-panopticlick)</sup> SecBrowser shares the fingerprint with around [three million](https://metrics.torproject.org/userstats-relay-country.html) other Tor Browser users, which allows people who use SecBrowser to "blend in" with the larger population and better protect their privacy. 

The [EFF has found](https://www.eff.org/deeplinks/2010/05/every-browser-unique-results-fom-panopticlick) that while most browsers are uniquely fingerprintable, resistance is afforded via four methods:

* Disabling JavaScript with tools like NoScript.
* Use of Torbutton, which is bundled with SecBrowser and enabled by default.
* Use of mobile devices like Android and iPhone.
* Corporate desktop machines which are clones of one another.

With JavaScript disabled, SecBrowser provides significant resistance to browser fingerprinting.<sup>[[13]](https://blog.torproject.org/effs-panopticlick-and-torbutton)</sup>

* The User Agent is uniform for all Torbutton users.
* Plugins are blocked.
* The screen resolution is rounded down to 50 pixel multiples.
* The timezone is set to GMT.
* DOM Storage is cleared and disabled.

The EFF's [Panoptickick](https://panopticlick.eff.org/) fingerprint test shows that SecBrowser resists fingerprinting.

_Note:_ Because tracking techniques are complex, Panopticlick does not measure all forms of tracking and protection.

* SecBrowser conveys 6.26 bits of identifying information. 
* One in 76.46 browsers having the same fingerprint.
* Browser's that convey lower bits of identification are better at resisting fingerprinting.<sup>[[14]](https://33bits.wordpress.com/about/)</sup>


When Tor Browser's and SecBrowser's HTTP headers are compared using [Fingerprint central](https://fpcentral.irisa.fr/) the test results are near identical.


**Table:** _Tor Browser vs SecBrowser HTTP Headers Comparison_ 

_Percentage (%) out of 1652 with fingerprints tags [Firefox,Windows]:_

| Name                      | Value                                                             | Tor Browser | SecBrowser  |
|---------------------------|-------------------------------------------------------------------|:-------------:|:-------------:|
|                           |                                                                   | %           | %           |
|  User-Agent               | Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0 | 2.48        | 2.42        |
| Accept                    | text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8   | 97.15       | 97.15       |
| Host                      | fpcentral.irisa.fr                                                | 90.44       | 90.43       |
| Content-Length            |                                                                   | 100.00      | 100.00      |
| Accepted-Language         | en-US,en;q=0.5                                                    | 32.63       | 32.95       |
| Referer                   | https://fpcentral.irisa.fr/                                       | 69.37       | 69.35       |
| Upgrade-Insecure-Requests | 1                                                                 | 83.05       | 83.04       |
| Accepting-Encoding        | gzip, deflate, br                                                 | 82.14       | 82.13       |
| Content-Type              |                                                                   | 100.00      | 100.00      |
| Connection                | close                                                             | 100.00      | 100.00      |

Install SecBrowser 
------------------

SecBrowser can be installed using `tb-updater` which is a package developed and maintained by Whonix developers. When run, `tb-updater` seamlessly automates the download and verification of SecBrowser (from The Tor Project's website). One of the many benefits of `tb-updater` is the ability to disable Tor is prebuilt into the software. This improves usability and is convenient since a security-focused browser (SecBrowser), is readily available. Unlike other manual methods of disabling Tor, this greatly simplifies the procedure and lessens the chance of a configuration error. To install SecBrowser in Qubes, users can follow the detailed instructions found on the designated [SecBrowser Wiki](https://www.whonix.org/wiki/SecBrowser) .

Conclusion 
----------

SecBrowser is a highly configurable security-focused browser that affords users with numerous options to fine tune their browser's security and usability. This can be achieved through user preferences (`user_pref`) or on the fly by means of an easy to use and intuitive security slider. This allows for seemless changes in security posture to meet changes in dynamic environments. SecBrowser's fingerprinting resistance provides strong protection against web tracking and can be combined with a VPN to further enhance privacy. SecBrowser can be used with any Debian 10 (buster) based operating system including [SecOS](https://forums.whonix.org/t/hardened-debian-security-focused-linux-distribution-based-on-debian-in-development-feedback-wanted/5943) (a Hardened Debian based OS) which is in active development and coming soon.

[SecBrowser]:[https://www.whonix.org/wiki/SecBrowser]
