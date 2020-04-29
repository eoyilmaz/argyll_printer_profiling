#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the advanced GUI version of the Windows Command Line script
that does the ICC Profile creation.
"""


class ICCGenerator(object):
    """Generates ICC profiles by using ArgyllCMS.

    This is a generic utility that works in all the operating systems.

    Windows Workflow Notes:

    - Use Dry Creek Photo Profile Target Printer or Adobe Color Print Utility.
    -

    Linux Workflow notes:

    - Gimp + GutenPrint seems to be a very good option
    - Use /usr/share/color/icc/ or ~/.local/share/icc to install the profiles

    If the ``use_high_density_mode`` is set to True the system uses
    the i1pro patch pattern which is much denser than the one for ColorMunki.

    If the ``use_high_density_mode`` is set to anything other than True, then
    the system will use two A4 pages or one A3 page use:

    420 patches for A4 (in 2 A4 pages)
    460 patches for A3

    by setting the device to ``i1pro`` and the margins to 2 mm it is possible
    to print 600 (25x24) 8x10 mm patches for A4 and 1260 (36x35) 8x10 mm
    patches for A3 on a single page.

    what I want to achieve here is to use the minimum amount of paper for
    profiling and still have an excellent result

    Generated temp files are located under these folders:

        For Windows:

            $APPDATA/ICCGenerator/Outputs/%{printer_brand}_%{printer_model}/%{profile_date}

        For Linux:

            ~/.cache/IccGenerator/Outputs/%{printer_brand}_%{printer_model}/%{profile_date}

    folders.

    The final ICC profiles will be placed under these folders:

        For Windows:

            %WINDIR%/System32/spool/drivers/color/

        For Linux:

            ~/.local/share/icc/

    """
    A3 = "A3"
    A4 = "A4"
    NORMAL_DENSITY = 'normal_density'
    HIGH_DENSITY = 'high_density'

    __data__ = {
        'paper_size':
            {
                A3: {
                    'patch_count': {
                        NORMAL_DENSITY: 460,
                        HIGH_DENSITY: 1260,
                    }
                },
                A4: {
                    'patch_count': {
                        NORMAL_DENSITY: 210,
                        HIGH_DENSITY: 600,
                    }
                }
            }
    }

    def __init__(self, printer_brand="Canon", printer_model="iX6850", paper_brand="Kodak", paper_model="UPPP",
                 paper_finish="Glossy", paper_size=A4, ink_brand="CanonInk", use_high_density_mode=True,
                 number_of_pages=1, copyright_info=""):

        self._printer_brand = None
        self.printer_brand = printer_brand

        self._printer_model = None
        self.printer_model = printer_model

        self._paper_brand = None
        self.paper_brand = paper_brand

        self._paper_model = None
        self.paper_model = paper_model

        self._paper_finish = None
        self.paper_finish = paper_finish

        self._paper_size = None
        self.paper_size = paper_size

        self._ink_brand = None
        self.ink_brand = ink_brand

        self._use_high_density_mode = None
        self.use_high_density_mode = use_high_density_mode

        self._number_of_pages = None
        self.number_of_pages = number_of_pages

        self._copyright_info = None
        self.copyright_info = copyright_info

        import datetime
        now = datetime.datetime.now()
        date_str = now.strftime("%Y%m%d")
        time_str = now.strftime("%H%m")

        self.profile_date = date_str
        self.profile_time = time_str

        # Generated temp files should be placed under a disposable folder

        # Profile Path template
        self.profile_path_template = \
            "~/.cache/ICCGenerator/Outputs/%{printer_brand}_" \
            "%{printer_model}/%{profile_date}"

        # update the output path according to the OS

        self.profile_path = ""

        # Profile name template
        self.profile_name_template = \
            "{printer_brand}_{printer_model}_{paper_brand}_" \
            "{paper_model}_{paper_finish}_{paper_size}_{ink_brand}_" \
            "{profile_date}_{profile_time}"
        self._profile_name = ""

        # The output path is defined by the Operating system
        self.output_path = "~/.local/share/icc/"

    @property
    def printer_brand(self):
        return self._printer_brand

    @printer_brand.setter
    def printer_brand(self, printer_brand):
        """getter for the printer_brand attribute
        """
        if not printer_brand or not isinstance(printer_brand, str):
            raise TypeError(
                "%s.printer_brand should be a str, not %s" % (
                    self.__class__.__name__, printer_brand.__class__.__name__
                )
            )
        self._printer_brand = printer_brand

    @property
    def printer_model(self):
        return self._printer_model

    @printer_model.setter
    def printer_model(self, printer_model):
        """getter for the printer_model attribute
        """
        if not printer_model or not isinstance(printer_model, str):
            raise TypeError(
                "%s.printer_model should be a str, not %s" % (
                    self.__class__.__name__, printer_model.__class__.__name__
                )
            )
        self._printer_model = printer_model

    @property
    def paper_brand(self):
        return self._paper_brand

    @paper_brand.setter
    def paper_brand(self, paper_brand):
        """getter for the paper_brand attribute
        """
        if not paper_brand or not isinstance(paper_brand, str):
            raise TypeError(
                "%s.paper_brand should be a str, not %s" % (
                    self.__class__.__name__, paper_brand.__class__.__name__
                )
            )
        self._paper_brand = paper_brand

    @property
    def paper_model(self):
        return self._paper_model

    @paper_model.setter
    def paper_model(self, paper_model):
        """getter for the paper_model attribute
        """
        if not paper_model or not isinstance(paper_model, str):
            raise TypeError(
                "%s.paper_model should be a str, not %s" % (
                    self.__class__.__name__, paper_model.__class__.__name__
                )
            )
        self._paper_model = paper_model

    @property
    def paper_finish(self):
        return self._paper_finish

    @paper_finish.setter
    def paper_finish(self, paper_finish):
        """getter for the paper_finish attribute
        """
        if not paper_finish or not isinstance(paper_finish, str):
            raise TypeError(
                "%s.paper_finish should be a str, not %s" % (
                    self.__class__.__name__, paper_finish.__class__.__name__
                )
            )
        self._paper_finish = paper_finish

    @property
    def paper_size(self):
        return self._paper_size

    @paper_size.setter
    def paper_size(self, paper_size):
        """getter for the paper_size attribute
        """
        if not paper_size or not isinstance(paper_size, str):
            raise TypeError(
                "%s.paper_size should be a str, not %s" % (
                    self.__class__.__name__, paper_size.__class__.__name__
                )
            )

        if paper_size not in self.__data__['paper_size']:
            raise ValueError(
                "%s.paper_size should be one of %s, not %s" % (
                    self.__class__.__name__,
                    list(self.__data__['paper_size'].keys()),
                    paper_size
                )
            )

        self._paper_size = paper_size

    @property
    def ink_brand(self):
        return self._ink_brand

    @ink_brand.setter
    def ink_brand(self, ink_brand):
        """getter for the ink_brand attribute
        """
        if not ink_brand or not isinstance(ink_brand, str):
            raise TypeError(
                "%s.ink_brand should be a str, not %s" % (
                    self.__class__.__name__, ink_brand.__class__.__name__
                )
            )
        self._ink_brand = ink_brand

    @property
    def use_high_density_mode(self):
        return self._use_high_density_mode

    @use_high_density_mode.setter
    def use_high_density_mode(self, use_high_density_mode):
        """getter for the use_high_density_mode attribute
        """
        if not isinstance(use_high_density_mode, bool):
            raise TypeError(
                "%s.use_high_density_mode should be a bool (True or False), not %s" % (
                    self.__class__.__name__, use_high_density_mode.__class__.__name__
                )
            )
        self._use_high_density_mode = use_high_density_mode

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        """getter for the number_of_pages attribute
        """
        if not number_of_pages or not isinstance(number_of_pages, int):
            raise TypeError(
                "%s.number_of_pages should be a int, not %s" % (
                    self.__class__.__name__, number_of_pages.__class__.__name__
                )
            )
        self._number_of_pages = number_of_pages

    @property
    def copyright_info(self):
        return self._copyright_info

    @copyright_info.setter
    def copyright_info(self, copyright_info):
        """getter for the copyright_info attribute
        """
        if not isinstance(copyright_info, str):
            raise TypeError(
                "%s.copyright_info should be a str, not %s" % (
                    self.__class__.__name__, copyright_info.__class__.__name__
                )
            )
        self._copyright_info = copyright_info

    @property
    def profile_name(self):
        """getter for the profile name attribute
        """
        if not self._profile_name:
            self.profile_name = self.profile_name_template.format(
                printer_brand=self.printer_brand,
                printer_model=self.printer_model,
                paper_brand=self.paper_brand,
                paper_model=self.paper_model,
                paper_finish=self.paper_finish,
                paper_size=self.paper_size,
                ink_brand=self.ink_brand,
                profile_date=self.profile_date,
                profile_time=self.profile_time
            )
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """setter for profile_name
        :param str profile_name:
        :return:
        """
        self._profile_name = profile_name

    @property
    def per_page_patch_count(self):
        """getter for the per_page_patch_count property
        """
        # Per Page Patch Count is Defined by the Paper Size and
        # the High Resolution mode
        resolution_str = self.HIGH_DENSITY if self.use_high_density_mode else self.NORMAL_DENSITY
        return self.__data__['paper_size'][self.paper_size]['patch_count'][resolution_str]

    @property
    def patch_count(self):
        """getter for the patch_count attribute
        """
        return self.per_page_patch_count * self.number_of_pages

    def generate_targets(self):
        """generates the required Tiff file or files depending on the page
        count
        """
        raise NotImplementedError

    def print_charts(self):
        """runs the proper application with the charts already open

        For Windows, it will first try to run Dry Creek Photo Print Utility if
        exist and if not then it will try to run Adobe Color Printer Utility,
        and if it doesn't exists either it will raise a proper RuntimeError
        stating that the user should install Dry Creek Photo Print Utility or
        ACPU.

        For Linux, it will first check if GIMP and GutenPrint is installed,
        if not will raise a RuntimeError to inform the user, if they exists
        properly it will open GIMP with the Tiff file.
        """
        raise NotImplementedError

    def read_charts(self):
        """
        """
        raise NotImplementedError

    def generate_profile(self):
        """
        """
        raise NotImplementedError

    def install_profile(self):
        """
        """
        raise NotImplementedError


class UI(object):
    """The UI
    """
    pass
