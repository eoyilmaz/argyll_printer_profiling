# ArgyllCMS Printer Profiling (with X-Rite ColorMunki Photo or X-Rite i1Pro 2) #

This is a Python module that lets the user to create Inkjet Printer Profiles
with Argyll CMS and X-Rite ColorMunki Photo and X-Rite i1Pro 2.

The system is based on [Andres Torger's tutorial](https://www.ludd.ltu.se/~torger/photography/argyll-print.html).
Which is a great read if you want to do a quick entry to ArgyllCMS.

## How To Use ##

The system is developed and tested under Fedora 31/32/33/34 and Windows 10.

### Windows ###

Follow the steps for Windows:

 - Download [ArgyllCMS](https://www.argyllcms.com/), extract it to a folder.
   Add the ``Argyll_2.x.x/bin`` folder to your ``PATH`` environment variable,
   so you would be able to call the commands anywhere from your command line.
 - Set up your ColorMunki Photo to use the [ArgyllCMS driver](http://argyllcms.com/doc/Installing_MSWindows.html).
 - To be able to print the generated color patches with **No Color Management**
   download [Dry Creek Photo Print Utility](https://www.drycreekphoto.com/tools/ChartPrinter/DryCreekPhotoPrintUtilitySetup.exe) 
   ([Adobe Color Printer Utility](https://helpx.adobe.com/photoshop/kb/no-color-management-option-missing.html) 
   also works, but it has a bug and prints smaller than it needs to be making
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

### MacOS ###

Nearly same as Linux:

 - Printing the targets with macOS requires an application that can disable the ICC
   profiles. Don't use Adobe Photoshop as there is no way to disable the usage of ICC
   profiles. Adobe Color Printer Utility is also not working properly with the latest
   versions of macOS. The best alternative I found so far is
   [Print-Tool](https://www.quadtonerip.com/html/QTRprinttool.html "Print-Tool") is a
   very suitable tool, albeit non-free.

### For Both Windows and Linux ###

For both windows and Linux the rest of the steps are same.

Just follow the steps in the UI. The final page will install the generated ICC
profile to your system. And that's it. You can then use that
profile to print from applications like Photoshop, Lightroom, CaptureOne, Gimp
etc.

The system is setup to use 600 color patches per A4 or 1212 color patches per
A3 size paper in ``high density mode`` and 210 color patches per A4 and 445
color patches per A3. The high density mode is the default behaviour. But it
may be tedious to scan through. If that's the case, simply don't use
high density mode and print more pages.

### Python Documentation ###

The system is now a Python library. You do not need to use the command line
tools.

```python
from icc_generator.api import ICCGenerator, PaperSizeLibrary

ig = ICCGenerator()

# Set Printer Details
ig.printer_brand = "Canon"
ig.printer_model = "iX6850"

# Set Paper Details
ig.paper_brand = "Kodak"
ig.paper_model = "UPPP"
ig.paper_finish = "Glossy"
ig.paper_size = PaperSizeLibrary.A4  # Or generate a custom size.

# Set Ink Details
ig.ink_brand = "CanonInk"

# Profiling workflow, run the following commands in the given order:
ig.gray_patch_count = 128  # default is 128, which should be quite enough.
ig.generate_target()
ig.generate_tif()  # This will output TIF file paths
ig.print_charts()  # Can be skipped and TIF file paths can be directly used.
ig.read_charts()
ig.generate_profile()
ig.check_profile(True)  # Look to the first couple of rows for high errors (dE > 3).

# Optional
# To fix misread patches (patches with too high dE values)
# re-read the chart in resume mode
ig.read_charts(resume=True, read_mode=0) # use read_mode=1 for patch-by-patch

# Finally install the profile
ig.install_profile()
```

Next, there will be a Qt UI in the near future.