---
lang: en
layout: doc
permalink: /doc/how-to-open-urls-in-other-qubes/
ref: TBD
title: How to open URLs/files in other qubes
---

*This page is about opening untrusted files and URLs from "secure" offline or
firewalled qubes in "general-purpose" qubes - or any qubes you see fit. The
simplest solution is to [copy/paste](/doc/how-to-copy-and-paste-text/) URLs or
[copy files](/doc/how-to-copy-and-move-files/) between qubes and manually open
the resource in the destination qube. However this approach is error-prone so
using formal RPC policies like described below is preferable.*

Naming convention:

- `srcQube` is the qube where the files/URLs are
- `dstQube` is the qube we want to open them in

## Configuring RPC policies

The `qvm-open-in-vm` and `qvm-open-in-dvm` scripts are invoked in a qube to
open files and URLs in another qube. Those scripts make use of the the
`qubes.OpenInVM` and `qubes.OpenURL` [RPC
services](/doc/qrexec/#qubes-rpc-services). Qubes [RPC
policies](/doc/rpc-policy/) control which RPC services are allowed between
qubes.

Policy files are in `/etc/qubes/policy.d/`.

### Using the `ask` action

This action displays a selection widget with the list of allowed destination
qubes each time the associated RPC service is called. This setup makes it
possible to always control if, and on which qube and network (eg. "clearnet",
TOR, VPN) an URL is requested or file opened.

The selected qube will autostart if it wasn't running. 

Note: when using `ask`, the destination qube given as argument to
`qvm-open-in-vm` is ignored if no `allow` rule matches the current RPC service
and source/destination qubes.

### Using the `allow` action

This action allows a given RPC service and source/destination qubes without
prompting the user.

When an `allow` action is defined for a destination other than `@dispvm`, the
destination qube is the one given as an argument to `qvm-open-in-vm` in
`srcQube`. The corresponding RPC policies should obviously be configured
accordingly.

Caveat: since there is no user confirmation with `allow`, applications in
`srcQube` could leak data through URLs or file names. You might notice that an
URL has been open in the destination qube but it would be too late.

### Notes about using disposable qubes and the `@dispvm` keyword in policies

It is possible to further restrict a destination DispVM qube by specifying the
template it is based on with the `@dispvm:templatename` syntax. See the
[documentation](/doc/how-to-use-disposables/#opening-a-link-in-a-disposable-based-on-a-non-default-disposable-template-from-a-qube)
for further details and the sample section below.

Caveat: `@dispvm` means "DisposableVMs based on the default DisposableVM
template of the calling qube", not "*any* DisposableVMs". If you were to run
`qvm-open-in-vm @dispvm:onlinedvm https://www.qubes-os.org` in `srcQube` and
`onlinedvm` wasn't the default dvm template for `srcQube`, a policy line with only
`@dispvm` wouldn't match: it would have to be `@dispvm:onlinedvm`.

If for some reason a user needs to use a disposable qube with a static name -
which might come handy when using `allow` RPC policies like in the sample
section below - he/she can do like so (replace `fedora-dvm` with the dvm
template you want to use):

~~~
qvm-create --class DispVM --label red --template fedora-dvm qube_name
~~~

`qube_name` would then be started like a regular qube with the difference that
like standard disposable qubes its private disk is wiped after each use.
However, unlike standard disposable qubes, this qube won't "auto power off" when
the called application (eg. firefox) is closed, so it's up to the user to power
off (or restart) the qube when he/she deems necessary.

## Sample RPC user policy

`/etc/qubes/policy.d/30-user.policy`:

~~~
# Deny opening files or URLs from or to 'vault'
qubes.OpenInVM      *   @anyvm  vault       deny
qubes.OpenURL       *   @anyvm  vault       deny
qubes.OpenInVM      *   vault   @anyvm      deny
qubes.OpenURL       *   vault   @anyvm      deny

# Allow 'work' to open URLs in disposable qubes without prompting the user
qubes.OpenURL       *   work    @dispvm  allow

# Allow 'work' to open Files in 'untrusted' (a named disposable qube) without
# prompting the user ('unstrusted' might for instance be configured as an
# offline qube to prevent network leaks)
qubes.OpenInVM      *   work    @dispvm  allow target=untrusted

# Allow qubes to open files and URLs in disposable qubes that are based on the
# template named 'foo' and 'bar' respectively (like above, 'foo' might be
# configured as an offline dvm template to prevent network leaks).
qubes.OpenInVM      *   @anyvm  @dispvm:foo allow
qubes.OpenURL       *   @anyvm  @dispvm:bar allow

# Prompt the user before opening any file/URL in any other qube.
# Qube default selection:
#  - 'dispOffline' qube for files
#  - 'dispOnline' qube for URLs
qubes.OpenInVM      *   @anyvm  @anyvm      ask default_target=dispOffline
qubes.OpenURL       *   @anyvm  @anyvm      ask default_target=dispOnline
~~~


## Configuring qubes to open files and URLs with application handlers

It is possible to (re)define a default application handler so that it is
automatically called by *any* application in `srcQube` to open files or URLs -
provided that the applications adhere to the
[freedesktop](https://en.wikipedia.org/wiki/Freedesktop.org) standard (which is
most always the case nowadays).

For application-specific configurations and/or applications that don't adhere
to the freedesktop standard, please refer to the unofficial, external
[community
documentation](https://github.com/Qubes-Community/Contents/blob/master/docs/common-tasks/opening-urls-in-vms.md)).

Defining a new handler simply requires creating a
[.desktop](https://specifications.freedesktop.org/desktop-entry-spec/latest/)
file and registering it. The following example shows how to open http/https URLs (along with common
"web" [Mime](https://en.wikipedia.org/wiki/Media_type) types) with `qvm-open-in-vm`:

- create `$HOME/.local/share/applications/browser_vm.desktop` with the following
  content:

	~~~
	[Desktop Entry]
	Encoding=UTF-8
	Name=BrowserVM
	Exec=qvm-open-in-vm dstQube %u
	Terminal=false
	X-MultipleArgs=false
	Type=Application
	Categories=Network;WebBrowser;
	MimeType=x-scheme-handler/unknown;x-scheme-handler/about;text/html;text/xml;application/xhtml+xml;application/xml;application/vnd.mozilla.xul+xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;
	~~~

- register the .desktop file with `xdg-settings set default-web-browser
  browser_vm.desktop`. 

The same can be done with any other Mime type (see `man xdg-mime` and
`xdg-settings`).

Notes:

- some applications may not use the new xdg application/handler (eg. if you had
  previously configured default applications), in which case you'd have to
  manually configure the application to use the xdg handler.

- `qvm-open-in-vm dstQube %u` can be replaced by a user wrapper with a custom
  logic for selecting different destination qubes depending on the URL/file
  type, level of trust, ... ; The RPC policies should be configured accordingly.

- very security conscious users should consider basing AppVMs on minimal
  templates; that way, unless a default handler is set, nothing else is usually
  there to open those files by default.


