---
lang: en
layout: doc
permalink: /doc/media-troubleshooting/
ref: 235
title: Media Troubleshooting
---

# Video and Audio Troubleshooting

## Can't play media videos in a VM due to missing codecs

If you’re having trouble playing a video file in a qube, you’re probably missing the required codecs.
The easiest way to resolve this is to install VLC Media Player and use that to play your video files.
You can do this in multiple different TemplateVM distros by following the instructions [here](/faq/#how-do-i-play-video-files).

## Video lagging

Playing videos may cause lags since software decoding uses a lot of CPU.

Depending on your video player, there are some settings that may smoothen video plays:

* If using VLC media player, go to Tools--> Preferences --> Video --> Output.
By default, the Output is set to "Automatic".
Go through the list and try out other output options to see if any makes videos run smoother.
* If using mpv media player, you may be able to improve performance by entering `mpv --profile=sw-fast --vo=x11` in a terminal.
* For video lags when playing videos from a browser, disable hardware acceleration in the browser. If the problem arises when watching streams, it may be smoother to use `streamlink` to view streams in mpv instead of using the browser.
