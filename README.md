# ArgyllCMS Printer Profiling Commands (with X-Rite ColorMunki Photo) #

This is a set of commands to create Inkjet Printer Profiles with Argyll CMS and
X-Rite ColorMunki Photo.

The commands are based on [Andres Torger's tutorial](https://www.ludd.ltu.se/~torger/photography/argyll-print.html).
Which is a great read if you want to do a quick entry to ArgyllCMS.

## How To Use ##

The system is developed and tested under Fedora 31 and Windows 10.

### Windows ###

Follow the steps for Windows:

 - Download [ArgyllCMS](https://www.argyllcms.com/), extract it to a folder.
   Add the ``Argyll_2.x.x/bin`` folder to your ``PATH`` environment variable,
   so you would be able to call the commands anywhere from your command line.
 - Setup your ColorMunki Photo to use the [ArgyllCMS driver](http://argyllcms.com/doc/Installing_MSWindows.html).
 - To be able to print the generated color patches with **No Color Management**
   download [Dry Creek Photo Print Utility](https://www.drycreekphoto.com/tools/ChartPrinter/DryCreekPhotoPrintUtilitySetup.exe) 
   ([Adobe Color Printer Utility](https://helpx.adobe.com/photoshop/kb/no-color-management-option-missing.html) 
   also works but it has a bug and prints smaller then it needs to be making
   it harder to read with the device).
 - Install the ``DryCreekPhotoPrintUtility`` or if you choose to use the
   ``ACPU`` extract the ``ACPU.zip`` file content inside the project folder. So
    the ``Adobe Color Printer Utility.exe`` is in the ``ACPU`` folder (
    ``ACPU\Adobe Color Printer Utility.exe``).

### Linux ###

Follow the steps for Linux:

 - Install ArgyllCMS from your package manager or download executables from
   [ArgyllCMS download page](http://argyllcms.com/downloadlinux.html).
 - Your device drivers should automatically be installed. And the device should
   work without a problem when you attach it to your computer (Although a
   simple profiler based on ArgyllCMS may pop up. Don't use it. Under Fedora 31
   where the system is developed, it is not working and it doesn't have enough
   option ex: high resolution mode, continue reading patches, read mode
   alternatives etc.
 - You can use Gimp + GutenPrint, and print with **no color correction**.

### For Both Windows and Linux ###

For both windows and Linux the rest of the steps are same.

Just follow the steps in the UI. The final page will install the generated ICC
profile to your system. And that's it. You can then use that
profile to print from applications like Photoshop, Lightroom, CaptureOne, Gimp
etc.

The system is setup to use 600 color patches per A4 or 1260 color patches per
A3 size paper in ``high density mode`` and 210 color patches per A4 and 460
color patches per A3. The high density mode is the default behaviour. But it
may be tedious to scan through. If that's the case, simply don't use
high density mode and print more pages.