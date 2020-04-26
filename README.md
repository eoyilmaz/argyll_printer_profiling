ArgyllCMS Printer Profiling Commands (with X-Rite ColorMunki Photo)
===================================================================

This is a set of commands to create Inkjet Printer Profiles with Argyll CMS and
X-Rite ColorMunki Photo.

The commands are based on [Andres Torger's tutorial](https://www.ludd.ltu.se/~torger/photography/argyll-print.html).
Which is a great read if you want to do a quick entry to ArgyllCMS.

How To Use
----------

Download [ArgyllCMS](https://www.argyllcms.com/), extract it to a folder. Add
the ``Argyll_2.x.x/bin`` folder to your ``PATH`` environment variable, so you
would be able to call the commands anywhere from your command line.

Setup your ColorMunki Photo to use the [Argyll driver](http://argyllcms.com/doc/Installing_MSWindows.html).

To be able to print the generated color patches with **No Color Management**
download [Dry Creek Photo Print Utility](https://www.drycreekphoto.com/tools/ChartPrinter/DryCreekPhotoPrintUtilitySetup.exe) 
([Adobe Color Printer Utility](https://helpx.adobe.com/photoshop/kb/no-color-management-option-missing.html) 
also works but it has a bug and prints smaller then it needs to be making it
harder to read with the device).

Install the ``DryCreekPhotoPrintUtility`` or if you choose to use the 
``ACPU`` extract the ``ACPU.zip`` file content inside the project folder. So the
``Adobe Color Printer Utility.exe`` is in the ``ACPU`` folder
(``ACPU\Adobe Color Printer Utility.exe``).

And then just run the commands in order. Start with ``1_setup_vars.cmd`` and
follow the instructions. The final command will instal the generated ICC profile
to your system. And that's it. You can then use that profile to print from
applications like Photoshop, Lightroom, CaptureOne etc.

The system is setup to use 600 color patches per A4 or 1260 color patches per A3
size paper in ``high density mode`` and 210 color patches per A4 and 460 color
patches per A3. The high density mode is the default behaviour. But it may be
tedious to scan through. If that's the case for your simply don't use high
density mode and print more pages.