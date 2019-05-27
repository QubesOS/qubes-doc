---
layout: doc
title: Optical Discs
permalink: /doc/optical-discs/
redirect_from:
 - /doc/recording-optical-discs/
 - /en/doc/recording-optical-discs/
---

Optical Discs
=============

Passthrough reading and recording (a.k.a., "burning") are not supported by Xen.
Currently, the only options for reading and recording optical discs (e.g., CDs, DVDs, BRDs) in Qubes are:

 1. Use a USB optical drive.
 2. Attach a SATA optical drive to a secondary SATA controller, then assign this secondary SATA controller to a VM.
 3. Use a SATA optical drive attached to dom0.
    (**Caution:** This option is [potentially dangerous](/doc/security-guidelines/#dom0-precautions).)

