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
download [Adobe Color Printer Utility](https://helpx.adobe.com/photoshop/kb/no-color-management-option-missing.html).
Extract the ``ACPU.zip`` file content inside the project folder. So the
``Adobe Color Printer Utility.exe`` is in the ``ACPU`` folder
(``ACPU\Adobe Color Printer Utility.exe``).

And then just run the commands in order. Start with ``1_setup_vars`` and follow
the instructions. And finally finish it by installing your ICC profile to your
system.