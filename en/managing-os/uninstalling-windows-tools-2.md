---
layout: doc
title: UninstallingWindowsTools2
permalink: /en/doc/uninstalling-windows-tools-2/
redirect_from:
- /doc/UninstallingWindowsTools2/
- /wiki/UninstallingWindowsTools2/
---

Uninstalling Qubes Tools for Windows v2.x
=========================================

**Do not try to uninstall Qubes Tools for Windows (QTW) 2.x from Windows Control Panel. It will render your HVM unbootable and will require manual fixing.**

Preface
-------

Version 2.x of QTW (used for Windows HVMs in Qubes R2) is difficult to uninstall due to issues with the Xen GPL PV drivers package that is used. However, uninstalling QTW version 2.x is required to migrate the HVM to Qubes R3.
HVMs with QTW 2.x *will not boot normally in Qubes R3* due to Xen drivers failing. They will boot in Safe Mode. It's easier to uninstall QTW 2.x from Qubes R2, but if that's not an option it's also possible in Qubes R3 (just a bit more complicated). Details below.

Uninstalling QTW 2.x in Qubes R2
--------------------------------

1. Copy the uninstall script posted at the end of this document and save it in the HVM as a .BAT file.
2. Reboot the HVM in Safe Mode: type `bcdedit /set safeboot minimal` in a command prompt with admin privileges then restart normally. The OS will now always start in Safe Mode until the setting is reverted.
3. In Safe Mode execute the uninstall script from step 1.
4. Open Device Manager. Manually uninstall Qubes Video device (in 'Display adapters') and Xen PCI driver (in 'System devices'). This will prevent the (already removed) devices from showing up.
5. Type `bcdedit /deletevalue safeboot` in a command prompt to disable Safe Mode boot.
6. Reboot. Open Device Manager and verify that there are no active Xen PV devices:
   - There should be one unidentified PCI device in System devices (this is the Xen PV device, not functioning because PV drivers are inactive).
   - Disk drives should be QEMU (emulated).
   - Network adapter should be Realtek (emulated).
   
Now you can backup the HVM, migrate it to Qubes R3 and install QTW 3.x there.

Uninstalling QTW 2.x in Qubes R3
--------------------------------

HVMs with QTW 2.x will not boot normally in Qubes R3 due to the old Xen drivers failing. If removing QTW from Qubes R2 is not an option (see above) then you will need to boot the HVM in Safe Mode.

### Preparation in dom0

Disable VM tools in VM's preferences:
* `qvm-prefs -s vmname qrexec_installed false`
* `qvm-prefs -s vmname guiagent_installed false`

### Enabling Safe Mode
* If you're quick you can mash F8 just as the HVM boots to access Windows' advanced boot options. The timing for it is very tight though. If you manage to get the boot menu, select Safe Mode boot.
* Alternatively, allow the HVM to (try to) boot. It will crash with a BSOD.
* After the crash start the HVM again. Now Windows will display the recovery menu which, for some unknown reason, does not include Safe Mode boot option. We need to try harder.
* Select **Launch Startup Repair**.
* If you're prompted to try System Restore, **don't**. Hit cancel.
* Grab a drink or read a book while Windows tries to do something but ultimately the repair process fails.
* *Now* you're presented with a choice of *advanced options* that include a command prompt. Why isn't this available from the start? 
* Launch the command prompt, log in and type `bcdedit /set {default} safeboot minimal`. The OS will now always start in Safe Mode until the setting is reverted. 
* Reboot and proceed with the uninstallation instructions from the previous paragraph (*Uninstalling QTW 2.x in Qubes R2*).

If you need network access to copy the uninstall script to the HVM, use *Safe Mode with Networking* instead of pure Safe Mode (replace `minimal` with `network` in the bcdedit commands above). Disable the Xen PV network device first. You may need to manually configure IP settings for the emulated Realtek adapter.


The uninstall script
====================

Save it as a .BAT file in the HVM and run in Safe Mode.

~~~
@echo off

:: This batch file uninstalls Qubes Tools for Windows version 2.x
:: Needs to be run in safe mode

:: Registry cleanup
reg delete "HKLM\Software\Invisible Things Lab" /f

:: services/drivers
reg delete HKLM\System\CurrentControlSet\Services\ShutdownMon /f
reg delete HKLM\System\CurrentControlSet\Services\QrexecAgent /f
reg delete HKLM\System\CurrentControlSet\Services\QTWHelper /f
reg delete HKLM\System\CurrentControlSet\Services\QubesNetworkSetup /f
reg delete HKLM\System\CurrentControlSet\Services\QVideo /f
reg delete HKLM\System\CurrentControlSet\Services\XenNet /f
reg delete HKLM\System\CurrentControlSet\Services\XenPCI /f
reg delete HKLM\System\CurrentControlSet\Services\XenVbd /f

:: xenpci filter entries
reg delete HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E96A-E325-11CE-BFC1-08002BE10318} /v UpperFilters /f
reg delete HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002bE10318} /v UpperFilters /f
reg delete HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E97B-E325-11CE-BFC1-08002BE10318} /v UpperFilters /f

:: files
rmdir /q /s "%ProgramFiles%\Invisible Things Lab"
rmdir /q /s "%ProgramFiles%\Xen PV Drivers"

del /q /s "%windir%\system32\move-profiles.exe"
del /q /s "%windir%\system32\windows-utils.dll"
del /q /s "%windir%\system32\qvgdi.dll"
del /q /s "%windir%\system32\drivers\qvmini.sys"
del /q /s "%windir%\system32\drivers\xennet.sys"
del /q /s "%windir%\system32\drivers\xenpci.sys"
del /q /s "%windir%\system32\drivers\xenvbd.sys"

:: driver store entries
FOR /F "delims=. tokens=1" %%I IN ('DIR /B "%SYSTEMROOT%\INF\OEM*.INF"') DO (
 TYPE "%SYSTEMROOT%\INF\%%I.inf" | FIND /c /i "Xen GPL PV" >%TEMP%\qtwuninstall
 FOR /f %%c IN (%TEMP%\qtwuninstall) DO (
  IF /I %%c NEQ 0 (
   DEL "%SYSTEMROOT%\INF\%%I.inf"
   DEL "%SYSTEMROOT%\INF\%%I.pnf"
  )
 )
)

FOR /F "delims=. tokens=1" %%I IN ('DIR /B "%SYSTEMROOT%\INF\OEM*.INF"') DO (
 TYPE "%SYSTEMROOT%\INF\%%I.inf" | FIND /c /i "Qubes" >%TEMP%\qtwuninstall
 FOR /f %%c IN (%TEMP%\qtwuninstall) DO (
  IF /I %%c NEQ 0 (
   DEL "%SYSTEMROOT%\INF\%%I.inf"
   DEL "%SYSTEMROOT%\INF\%%I.pnf"
  )
 )
)

echo.
echo Cleanup finished. Please manually uninstall Qubes Video and Xen devices from the Device Manager.
~~~
