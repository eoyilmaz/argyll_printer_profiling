#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the advanced GUI version of the Windows Command Line script
that does the ICC Profile creation.
"""
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


__version__ = "0.1.0"


class ICCGenerator(object):
    """Generates ICC profiles by using ArgyllCMS.

    This is a generic utility that works in all the operating systems.

    Windows Workflow Notes:

    - Use Dry Creek Photo Profile Target Printer (best option) or Adobe Color Print Utility (buggy, and scales images
      while printing).

    Linux Workflow notes:

    - Gimp + GutenPrint seems to be a very good option (set Color Correction to Uncorrected and Image Type to
      Photograph)

    - Use /usr/share/color/icc/ or ~/.local/share/icc to install the profiles

    If the ``use_high_density_mode`` is set to True the system uses the i1pro patch pattern which is much denser than
    the one for ColorMunki.

    If the ``use_high_density_mode`` is set to anything other than True, then the system will use two A4 pages or one A3
    page use:

    420 patches for A4 (in 2 A4 pages)
    460 patches for A3

    by setting the device to ``i1pro`` and the margins to 2 mm it is possible to print 600 (25x24) 8x10 mm patches for
    A4 and 1260 (36x35) 8x10 mm patches for A3 on a single page.

    what I want to achieve here is to use the minimum amount of paper for
    profiling and still have an excellent result

    Generated temp files are located under these folders:

        For Windows:

            $APPDATA/ICCGenerator/%{printer_brand}_%{printer_model}/%{profile_date}

        For Linux:

            ~/.cache/IccGenerator/%{printer_brand}_%{printer_model}/%{profile_date}

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
                 number_of_pages=1, copyright_info="", precondition_profile_path=""):

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

        self._precondition_profile_path = None
        self.precondition_profile_path = precondition_profile_path

        import datetime
        now = datetime.datetime.now()
        date_str = now.strftime("%Y%m%d")
        time_str = now.strftime("%H%m")

        self.profile_date = date_str
        self.profile_time = time_str

        # Profile Path template
        self._profile_path_template = \
            "~/.cache/ICCGenerator/{printer_brand}_" \
            "{printer_model}/{profile_date}"

        # Profile name template
        self.profile_name_template = \
            "{printer_brand}_{printer_model}_{paper_brand}_" \
            "{paper_model}_{paper_finish}_{paper_size}_{ink_brand}_" \
            "{profile_date}_{profile_time}"
        self._profile_name = ""

        self.tif_files = []

        # The output path is defined by the Operating system
        import os
        self.output_path = "~/.local/share/icc/"
        if os.name == 'nt':
            self.output_path = '%WINDIR%/System32/spool/drivers/color/'

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
    def precondition_profile_path(self):
        return self._precondition_profile_path

    @precondition_profile_path.setter
    def precondition_profile_path(self, precondition_profile_path):
        """getter for the precondition_profile_path attribute
        """
        if not isinstance(precondition_profile_path, str):
            raise TypeError(
                "%s.precondition_profile_path should be a str, not %s" % (
                    self.__class__.__name__, precondition_profile_path.__class__.__name__
                )
            )
        self._precondition_profile_path = precondition_profile_path

    @property
    def profile_path(self):
        """getter for the profile_path attribute
        """
        # update the output path according to the OS
        return self._profile_path_template.format(
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

    @property
    def profile_name(self):
        """getter for the profile_name attribute
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

    @property
    def gray_patch_count(self):
        """getter for the gray_patch_count attribute
        """
        return self.number_of_pages * 16

    @classmethod
    def run_external_process(cls, command):
        """Runs an external process and yields the output

        :param command: The command to run
        """
        import subprocess
        process = subprocess.Popen(
            command, stderr=subprocess.PIPE
        )
        # loop until process finishes and capture stderr output
        stderr_buffer = []
        while True:
            stderr = process.stderr.readline()

            if stderr == b'' and process.poll() is not None:
                break

            if stderr != b'':
                stderr = stderr.decode('utf-8').strip()
                stderr_buffer.append(stderr)
                yield stderr

        # flatten the buffer
        stderr_buffer = '\n'.join(stderr_buffer)
        return_code = process.returncode

        if return_code:
            # there is an error
            raise RuntimeError(stderr_buffer)

    def generate_target(self):
        """generates the required ti1 file
        """
        import os
        profile_path = os.path.expanduser(self.profile_path)
        profile_full_path = \
            os.path.expanduser(
                os.path.join(
                    self.profile_path, self.profile_name
                )
            )

        os.makedirs(profile_path, exist_ok=True)

        # ************************
        # targen command
        command = [
            "targen", "-v", "-d", "2", "-G",
            "-g", "%s" % self.gray_patch_count,
            "-f", "%s" % self.patch_count
        ]
        if self.precondition_profile_path:
            command += ["-c", self.precondition_profile_path]
        command += [profile_full_path]

        # first call the targen command
        # print("generate_target command: %s" % ' '.join(command))
        yield from self.run_external_process(command)

    def generate_tif_files(self):
        """generates the required Tiff file or files depending on the page
        count
        """
        import os
        profile_path = os.path.expanduser(self.profile_path)
        profile_full_path = \
            os.path.expanduser(
                os.path.join(
                    self.profile_path, self.profile_name
                )
            )

        os.makedirs(profile_path, exist_ok=True)

        # ************************
        # printtarg command
        command = ["printtarg", "-v"]
        if self.use_high_density_mode:
            command += ['-ii1']  # Use i1 Pro
        else:
            command += ['-iCM']  # Use ColorMunki

        command += [
            "-h", "-R1", "-T300", "-M2", "-L", "-P", "-p", self.paper_size,
            profile_full_path
        ]

        # update tif files
        self.tif_files = []
        if self.number_of_pages == 1:
            self.tif_files.append(
                os.path.expanduser(
                    os.path.join(
                        self.profile_path,
                        "%s.tif" % self.profile_name
                    )
                )
            )
        else:
            for i in range(self.number_of_pages):
                self.tif_files.append(
                    os.path.expanduser(
                        os.path.join(
                            self.profile_path,
                            "%s_%02i.tif" % (self.profile_name, i + 1)
                        )
                    )
                )

        # first call the targen command
        # print("generate_tif_files command: %s" % ' '.join(command))
        yield from self.run_external_process(command)

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
        import os
        if os.name == 'nt':  # Windows
            # call Dry Creek Photo Print Utility first
            # if it fails then try to call ACPU
            # if this fails too, raise a RuntimeError
            pass
        elif os.name == 'posix':  # Linux
            # call Gimp with the TIFF Files
            command = ['/usr/bin/gimp'] + self.tif_files
            yield from self.run_external_process(command)

    def read_charts(self, resume=False, read_mode=0):
        """Reads the printed chart using the device

        :param bool resume: If a .ti3 files already exists and ``resume`` is
          set to True. The process will start from where it left before.
          Default value is False

        :param int read_mode: There are two possible modes:

            0: Strip Mode
            1: Patch-By-Patch

          Use ``read_mode=1`` (Patch-By-Patch) with ``resume=True`` to fix
          erroneously read patches.

        :return:
        """
        import os
        profile_path = os.path.expanduser(self.profile_path)
        profile_full_path = \
            os.path.expanduser(
                os.path.join(
                    self.profile_path, self.profile_name
                )
            )

        os.makedirs(profile_path, exist_ok=True)

        # ************************
        # chartread command
        command = ["chartread", "-v", "-H", "-T 0.4"]
        if read_mode == 0:  # Default
            command += ["-p", "-P"]

        if resume:
            command += ["-r"]

        command += [profile_full_path]

        # first call the targen command
        yield from self.run_external_process(command)

    def generate_profile(self):
        """
        """
        import os
        profile_path = os.path.expanduser(self.profile_path)
        profile_full_path = \
            os.path.expanduser(
                os.path.join(
                    self.profile_path, self.profile_name
                )
            )

        os.makedirs(profile_path, exist_ok=True)

        # ************************
        # colprof command
        command = [
            "colprof", "-v", "-ph", "-r0.5", "-S", "AdobeRGB.icc", "-cmt", "-dpp",
            "-D%s" % self.profile_name, "-Zr"
        ]

        if self.copyright_info:
            command.append("-C%s" % self.copyright_info)

        command += [profile_full_path]

        # call the command
        yield from self.run_external_process(command)

    def check_profile(self):
        """Checks the profile quality
        """
        import os
        profile_path = os.path.expanduser(self.profile_path)
        profile_full_path = \
            os.path.expanduser(
                os.path.join(
                    self.profile_path, self.profile_name
                )
            )

        os.makedirs(profile_path, exist_ok=True)

        # ************************
        # prof_check
        command = [
            "profcheck", "-k", "-v2",
            "%s.ti3" % profile_full_path,
            "%s.icm" % profile_full_path
        ]

        # call the command
        yield from self.run_external_process(command)

    def install_profile(self):
        """Installs the generated profile to appropriate folders depending on the current OS

        For Windows:

            %WINDIR%/System32/spool/drivers/color/

        For Linux:

            ~/.local/share/icc/

        """
        import os
        import shutil

        profile_absolute_path = os.path.expanduser(self.profile_path)
        profile_absolute_full_path = \
            os.path.expanduser(
                os.path.join(
                    self.profile_path, self.profile_name
                )
            )

        # check if the profile is not generated yet
        icc_profile_absolute_full_path = "%s.icc" % profile_absolute_full_path
        if not os.path.exists(icc_profile_absolute_full_path):
            raise RuntimeError("ICC file doesn't exist, please generate it first!")

        profile_install_path = os.path.expandvars(
            os.path.expanduser(
                os.path.join(
                    self.output_path,
                    '%s.icc' % self.profile_name
                )
            )
        )

        shutil.copy2(
            icc_profile_absolute_full_path,
            profile_install_path
        )


class UI(object):
    """The UI
    """
    pass
