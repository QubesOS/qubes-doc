---
layout: doc
title: Recording Optical Discs
permalink: /doc/recording-optical-discs/
redirect_from: /en/doc/recording-optical-discs/
---

Recording Optical Discs
=======================

Passthrough recording (a.k.a., "burning") is not supported by Xen. Currently,
the only options for recording optical discs (e.g., CDs, DVDs, BRDs) in Qubes
are:

 1. Use a USB optical drive.
 2. Attach a SATA optical drive to a secondary SATA controller, then assign this
    secondary SATA controller to a VM.
 3. Use a SATA optical drive attached to dom0.  
    (**Caution:** This option may violate the Qubes security model if it entails
    transferring untrusted data (e.g., an ISO) to dom0 in order to record it on
    an optical disc.)

