---
lang: en
layout: doc
permalink: /doc/how-to-open-urls-and-files-in-other-qubes/
title: How to open URLs and files in other qubes
---

This page is about opening URLs and files from one qube in a different qube. The most straightforward way to do this is simply to [copy and paste URLs](/doc/how-to-copy-and-paste-text/) or [copy and move files](/doc/how-to-copy-and-move-files/) from the source qube to the target qube, then manually open them in the target qube. However, some users might wish to use [RPC policies](/doc/rpc-policy/) in order to regiment their workflows and safeguard themselves from making mistakes.

Naming conventions:

- `<SOURCE_QUBE>` is the qube in which the URL or file originates.
- `<TARGET_QUBE>` is the qube in which we wish to open the URL or file.

## Configuring RPC policies

The `qvm-open-in-vm` and `qvm-open-in-dvm` scripts are invoked in a qube to open files and URLs in another qube. Those scripts make use of the `qubes.OpenInVM` and `qubes.OpenURL` [RPC services](/doc/qrexec/#qubes-rpc-services). Qubes [RPC policies](/doc/rpc-policy/) control which RPC services are allowed between qubes.

Policy files are in `/etc/qubes/policy.d/`.

### Using the `ask` action

This action displays a confirmation prompt in dom0 with a drop-down list of allowed target qubes each time the associated RPC service is called. This setup makes it possible to always control whether and in which qube a URL or file opened.

The selected qube will automatically start if it wasn't running. 

**Note:** When using `ask`, the target qube given as an argument to `qvm-open-in-vm` is ignored if no `allow` rule matches the current RPC service and source/target qubes.

### Using the `allow` action

This action allows a specified RPC service to be invoked between source and target qubes without displaying a confirmation prompt in dom0.

When an `allow` action is defined for a target other than `@dispvm`, the target qube is the one given as an argument to `qvm-open-in-vm` in `<SOURCE_QUBE>`. The corresponding RPC policies must be configured accordingly.

**Warning:** Since there is no user confirmation with `allow`, applications in `<SOURCE_QUBE>` could leak data through URLs or file names.

### Using disposables and the `@dispvm` keyword in policies

It is possible to further restrict a target disposable qube by specifying the template on which it is based with the `@dispvm:<DISPOSABLE_TEMPLATE>` syntax ([learn more](/doc/how-to-use-disposables/#opening-a-link-in-a-disposable-based-on-a-non-default-disposable-template-from-a-qube)).

**Note:** The keyword `@dispvm` designates any disposable based on the calling qube's default disposable template. It does *not* designate any disposable whatsoever. For example, if you were to run `qvm-open-in-vm @dispvm:<ONLINE_DISPOSABLE_TEMPLATE> https://www.qubes-os.org` in `<SOURCE_QUBE>` while `<ONLINE_DISPOSABLE_TEMPLATE>` is *not* `<SOURCE_QUBE>`'s default disposable template, it wouldn't work if your policy line merely had `@dispvm` as the target. You would have to use `@dispvm:<ONLINE_DISPOSABLE_TEMPLATE>` as the target instead.

## Sample RPC user policy

_See the main document, [RPC policies](/doc/rpc-policy/), for more information._

The following is a partial example of the kinds of `qubes.OpenInVM` and `qubes.OpenURL` rules that you could write in `/etc/qubes/policy.d/30-user.policy`:

~~~
# Deny opening files or URLs from or in 'vault'
qubes.OpenInVM   *   @anyvm   vault         deny
qubes.OpenURL    *   @anyvm   vault         deny
qubes.OpenInVM   *   vault    @anyvm        deny
qubes.OpenURL    *   vault    @anyvm        deny

# Allow 'work' to open URLs in disposable qubes without prompting the user
qubes.OpenURL    *   work     @dispvm       allow

# Allow 'work' to open files in 'untrusted' without prompting the user
qubes.OpenInVM   *   work     @dispvm       allow target=untrusted

# Allow any qube to open files and URLs in disposables based on the
# disposable templates 'foo' and 'bar'
qubes.OpenInVM   *   @anyvm   @dispvm:foo   allow
qubes.OpenURL    *   @anyvm   @dispvm:bar   allow

# Prompt the user before opening any file or URL in any other qube, but prefill
# the target with 'personal' for files and 'untrusted' for URLs
qubes.OpenInVM   *   @anyvm   @anyvm        ask default_target=personal
qubes.OpenURL    *   @anyvm   @anyvm        ask default_target=untrusted
~~~

## Configuring application handlers

It is possible to (re)define a default application handler so that it is automatically called by *any* application in `<SOURCE_QUBE>` to open files or URLs provided that the applications adhere to the [freedesktop](https://en.wikipedia.org/wiki/Freedesktop.org) standard (which is almost always the case nowadays).

For application-specific configurations or applications that don't adhere to the freedesktop standard, please refer to the unofficial, external [community documentation](https://github.com/Qubes-Community/Contents/blob/master/docs/common-tasks/opening-urls-in-vms.md).

Defining a new handler simply requires creating a [.desktop](https://specifications.freedesktop.org/desktop-entry-spec/latest/) file and registering it. The following example shows how to open http/https URLs (along with common "web" [media types](https://en.wikipedia.org/wiki/Media_type)) with `qvm-open-in-vm`:

- Create `$HOME/.local/share/applications/mybrowser.desktop` with the following content:

	~~~
	[Desktop Entry]
	Encoding=UTF-8
	Name=MyBrowser
	Exec=qvm-open-in-vm <TARGET_QUBE> %u
	Terminal=false
	X-MultipleArgs=false
	Type=Application
	Categories=Network;WebBrowser;
	MimeType=x-scheme-handler/unknown;x-scheme-handler/about;text/html;text/xml;application/xhtml+xml;application/xml;application/vnd.mozilla.xul+xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;
	~~~

- Register the `.desktop` file with `xdg-settings set default-web-browser mybrowser.desktop`. 

The same can be done with any other media type (see `man xdg-mime` and `xdg-settings`).

### Notes

- Some applications may not use the new XDG application handler (e.g., if you had previously configured default applications), in which case you'd have to manually configure the application to use the XDG handler.

- `qvm-open-in-vm target-qube %u` can be replaced by a user wrapper with custom logic for selecting different target qubes depending on the URL/file type, level of trust, etc. The RPC policies should be configured accordingly.

- Advanced users may wish to consider basing app qubes on [minimal templates](/doc/templates/minimal/). That way, unless a default handler is set, it is unlikely that any other program will be present that can open the URL or file.
