---
layout: doc
title: Application Troubleshooting
permalink: /doc/application-troubleshooting/
---

# Troubleshooting default applications on Qubes #

## Fullscreen Firefox is frozen ##

Press F11 twice.

## Firefox crashes ##

If you are facing frequent crashes or lags when using Firefox browser (especially when watching videos), you may need to turn off Hardware Acceleration. You can do this by navigating to "Preferences", then "Performance". Untick the "Use recommended performance settings" checkbox, followed by "Use hardware acceleration when available". 

If this doesn't fix the issue, try turning off smooth scrolling by unticking "Use smoothing scrolling" under the "Browsing" section. 

## LibreOffice open as a tiny window ##

Some programs like LibreOffice  open as a tiny window -- small enough that the content of the file is not even visible. 

You can open LibreOffice as a larger window using this workaround:

### Using the command line
1. In the VM where you want to open the LibreOffice, open the `registrymodifications.xcu` file in an editor:
    ~~~
    sudo nano ~/.config/libreoffice/4/user/registrymodifications.xcu
    ~~~

2. Find the lines containing `ooSetupFactoryWindowAttributes`. It will look like this:
~~~
<item oor:path="/org.openoffice.Setup/Office/Factories/org.openoffice.Setup:Factory['com.sun.star.sheet.SpreadsheetDocument']"><prop oor:name="ooSetupFactoryWindowAttributes" oor:op="fuse"><value>61,61,1807,982;5;38,56,1807,982;</value></prop></item>

3. We are interested in the values between the `<value>` tag. These window position values are specified as: `x-pos,y-pos,width,height ; window-state ; maximized-x-pos,maximized-y-pos,maximized-width,maximized-height`. Edit the third and fourth values to your desired width and height (for example, to 1800 and 900).
4. Do this once for every template and the program will always open at this size.

### Using the GUI
1. Open any Libreoffice app.
2. Navigate to the "Tools" menu, select "Options", then "Advanced". Click the "Open Expert Configuration" button.
3. Search for "ooSetupFactoryWindowAttributes".
4. Scroll right to see the values set for each component as a string value. For example:  `61,61,1807,982;5;38,56,1807,982;`. These window position values are specified as: `x-pos,y-pos,width,height ; window-state ; maximized-x-pos,maximized-y-pos,maximized-width,maximized-height`. Edit the third and fourth values to your desired width and height (for example, to 1800 and 900).
5. Do this once for every template and the program will always open at this size.

