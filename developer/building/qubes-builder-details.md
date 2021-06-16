---
lang: en
layout: doc
redirect_from:
- /doc/qubes-builder-details/
- /en/doc/qubes-builder-details/
- /doc/QubesBuilderDetails/
- /wiki/QubesBuilderDetails/
ref: 65
title: Qubes Builder Details
---

========================================

Components Makefile.builder file
--------------------------------

[QubesBuilder](/doc/qubes-builder/) expects that each component have *Makefile.builder* file in its root directory. This file specifies what should be done to build the package. As name suggests, this is normal makefile, which is included by builder as its configuration. Its main purpose is to set some variables. Generally all available variables/settings are described as comments at the beginning of Makefile.\* in [QubesBuilder](/doc/qubes-builder/).

Variables for Linux build:

- `RPM_SPEC_FILES` List (space separated) of spec files for RPM package build. Path should be relative to component root directory. [QubesBuilder](/doc/qubes-builder/) will install all BuildRequires (in chroot environment) before the build. In most Qubes components all spec files are kept in *rpm\_spec* directory. This is mainly used for Fedora packages build.
- `ARCH_BUILD_DIRS` List (space separated) of directories with PKGBUILD files for Archlinux package build. Similar to RPM build, [QubesBuilder](/doc/qubes-builder/) will install all makedepends, then build the package.

Most components uses *archlinux* directory for this purpose, so its good to keep this style.

Variables for Windows build:

- `WIN_COMPILER` Choose which compiler should be used for this component, thus which build scripts. Currently two options available:
  - `WDK` - Windows Driver Kit (default). Command used to build: *build -cZg*.
  - `mingw` - MinGW (Windows gcc port). Command used to build: *make all*
- `WIN_SOURCE_SUBDIRS` List of directories in which above command should be run. In most cases it will be only one entry: current directory (*.*).
- `WIN_PREBUILD_CMD` Command to run before build, mostly useful for WDK build (in mingw case, you can use makefile for this purpose). Can be used to set some variables, preprocess some files etc.
- `WIN_SIGN_CMD` Command used to sign resulting binaries. Note that default value is *sign.bat*. If you don't want to sign binaries, specify some placeholder here (eg. *true*). Check existing components (eg. vmm-xen-windows-pvdrivers) for example scripts. This command will be run with certain environment variables:
  - `CERT_FILENAME` Path to key file (pfx format)
  - `CERT_PASSWORD` Key password
  - `CERT_PUBLIC_FILENAME` Certificate path in the case of self-signed cert
  - `CERT_CROSS_CERT_FILENAME` Certificate path in the case of correct autheticode cert
  - `SIGNTOOL` Path to signtool
- `WIN_PACKAGE_CMD` Command used to produce installation package (msi or msm). Default value is *wix.bat*, similar to above - use *true* if you don't want this command.
- `WIN_OUTPUT_HEADERS` Directory (relative to `WIN_SOURCE_SUBDIRS` element) with public headers of the package - for use in other components.
- `WIN_OUTPUT_LIBS` Directory (relative to `WIN_SOURCE_SUBDIRS` element) with libraries (both DLL and implib) of the package - for use in other components. Note that [QubesBuilder](/doc/qubes-builder/) will copy files specified as *\$(WIN\_OUTPUT\_LIBS)/\*/\** to match WDK directory layout (*\<specified directory\>/\<arch directory\>/\<actual libraries\>*), so you in mingw build you need to place libraries in some additional subdirectory.
- `WIN_BUILD_DEPS` List of components required to build this one. [QubesBuilder](/doc/qubes-builder/) will copy files specified with `WIN_OUTPUT_HEADERS` and `WIN_OUTPUT_LIBS` of those components to some directory and provide its path with `QUBES_INCLUDES` and `QUBES_LIBS` variables. Use those variables in your build scripts (*sources* or *Makefile* - depending on selected compiler). You can assume that the variables are always set and directories always exists, even if empty.

builder.conf settings
---------------------

Most settings are documented in *builder.conf.default* file, which can be used as template the actual configuration.

**TODO**

Notes
-----

* For a list of custom TemplateVMs available in QubesBuilder look at [Supported Versions page](/doc/supported-versions/).
