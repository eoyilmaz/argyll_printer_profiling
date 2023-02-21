# -*- coding: utf-8 -*-
"""The API of the library."""

import datetime
import json
import os
import pathlib
import platform
import shutil
import subprocess
import traceback
from typing import Union

from icc_generator import logger


HERE = pathlib.Path(__file__).parent.absolute()


class PaperSize(object):
    """Represents a standard paper size.

    Has attributes like width, height, size, area. All measurements are in millimeters.

    Args:
        name (str): The name of the paper size.
        width (float | int): The width of the paper in mm.
        height (float | int): The height of the paper in mm.
    """

    def __init__(self, name: str, width: Union[float, int], height: Union[float, int]):
        self._name = None
        self._width = None
        self._height = None
        self.name = name
        self.width = width
        self.height = height

    @property
    def name(self) -> str:
        """Return name value.

        Returns:
            str: The name value.
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Set the name value.

        Args:
            name (str): The name value.

        Raises:
            TypeError: If the given name arg value is not a str.
        """
        if not isinstance(name, str):
            raise TypeError(
                f"{self.__class__.__name__}.name should be a str, "
                f"not {name.__class__.__name__}"
            )
        self._name = name

    @property
    def width(self) -> float:
        """Return the width.

        Returns:
            float: The width value.
        """
        return self._width

    @width.setter
    def width(self, width: Union[float, int]):
        """Set the width.

        Args:
            width (int | float): The width of the PaperSize instance in mm.

        Raises:
            TypeError: If the given width value is not a float or int.
            ValueError: If the given width value is not a positive number.
        """
        if not isinstance(width, (float, int)):
            raise TypeError(
                f"{self.__class__.__name__}.width should be a int or float, "
                f"not {width.__class__.__name__}"
            )
        if width <= 0:
            raise ValueError(
                f"{self.__class__.__name__}.width should be a positive value, "
                f"not {width}"
            )
        self._width = width

    @property
    def height(self) -> float:
        """Return the height.

        Returns:
            float: The height value.
        """
        return self._height

    @height.setter
    def height(self, height: Union[float, int]):
        """Set the height.

        Args:
            height (int | float): The height of the PaperSize instance in mm.

        Raises:
            TypeError: If the given height value is not a float or int.
            ValueError: If the given height value is not a positive number.
        """
        if not isinstance(height, (float, int)):
            raise TypeError(
                f"{self.__class__.__name__}.height should be a int or float, "
                f"not {height.__class__.__name__}"
            )
        if height <= 0:
            raise ValueError(
                f"{self.__class__.__name__}.height should be a positive value, "
                f"not {height}"
            )
        self._height = height

    @property
    def size(self) -> tuple[float, float]:
        """Return the width and height as a list.

        Returns:
            List[float, float]: The width and height as a list.
        """
        return self.width, self.height

    @size.setter
    def size(self, size: Union[list, tuple]):
        """Set the size attr.

        Args:
            size (Union[List[Union[int, float]], Tuple[Union[int, float]]): The size as
                a list of 2 items or tuple.

        Raises:
            TypeError: If the given size arg value is not a list or tuple.
            ValueError: If the given size arg value has more than 2 items.
        """
        if not isinstance(size, (list, tuple)):
            raise TypeError(
                f"{self.__class__.__name__}.size should be a list, "
                f"not {size.__class__.__name__}"
            )

        if len(size) != 2:
            raise ValueError(
                f"{self.__class__.__name__}.size should be a list or tuple of 2 items, "
                f"not {len(size)}"
            )

        self.width = size[0]
        self.height = size[1]

    @property
    def area(self) -> Union[int, float]:
        """Return the area in mm2.

        Returns:
            float: The area in mm2.
        """
        return self.width * self.height

    def __eq__(self, other) -> bool:
        """Check equality with other PaperSize instance.

        Args:
            other (PaperSize): The other PaperSize instance.

        Returns:
            bool: True if the other PaperSize is equal to this one.
        """
        return (
            isinstance(other, PaperSize)
            and self.name == other.name
            and self.width == other.width
            and self.height == other.height
        )

    def __hash__(self) -> int:
        """Override hash value.

        Returns:
            int: The hash value.
        """
        return hash(self.name) + 2 * hash(self.width) + 3 * hash(self.height)


class PaperSizeLibrary(object):
    """Data class for different paper sizes."""

    def __init__(self):
        raise RuntimeError(
            "PaperSizeLibrary is meant to be used as a storage class. "
            "Do not instantiate it."
        )

    p4x6 = PaperSize(name="4x6", width=101.6, height=152.4)
    p11x17 = PaperSize(name="11x17", width=279.4, height=431.8)
    A2 = PaperSize(name="A2", width=420.0, height=594)
    A3 = PaperSize(name="A3", width=297.0, height=420.0)
    A3R = PaperSize(name="A3R", width=420.0, height=297.0)
    A4 = PaperSize(name="A4", width=210.0, height=297.0)
    A4R = PaperSize(name="A4R", width=297.0, height=210.0)
    Legal = PaperSize(name="Legal", width=215.9, height=355.6)
    Letter = PaperSize(name="Letter", width=215.9, height=279.4)
    LetterR = PaperSize(name="LetterR", width=279.4, height=215.9)

    paper_sizes = {
        "4x6": p4x6,
        "11x17": p11x17,
        "A2": A2,
        "A3": A3,
        "A3R": A3R,
        "A4": A4,
        "A4R": A4R,
        "Legal": Legal,
        "Letter": Letter,
        "LetterR": LetterR,
    }

    @classmethod
    def get_paper_size(cls, paper_size_name: str) -> Union[PaperSize, None]:
        """Return paper size.

        Args:
            paper_size_name (str): The paper size name.

        Raises:
            TypeError: If the paper_size_name arg value is not a str.

        Returns:
            PaperSize: If the given paper size name exists in the library it returns the
                PaperSize instance, otherwise returns None.
        """
        if not isinstance(paper_size_name, str):
            raise TypeError(
                "paper_size_name should be a str, "
                f"not {paper_size_name.__class__.__name__}"
            )

        return cls.paper_sizes.get(paper_size_name)


class ICCGenerator(object):
    """Generates ICC profiles by using ArgyllCMS.

    This is a generic utility that works in all the operating systems.

    Windows Workflow Notes:

    - Use Dry Creek Photo Profile Target Printer (best option) or Adobe Color Print
      Utility (buggy, and scales images while printing).

    Linux Workflow notes:

    - Gimp + GutenPrint seems to be a very good option (set Color Correction to
      Uncorrected and Image Type to Photograph)

    - Use /usr/share/color/icc/ or ~/.local/share/icc to install the profiles

    MacOS Workflow notes:

    - Printing the targets with macOS requires an application that can disable the ICC
      profiles. Don't use Adobe Photoshop as there is no way to disable the usage of ICC
      profiles. Adobe Color Printer Utility is also not working properly with the latest
      versions of macOS. The best alternative I found so far is
      [Print-Tool](https://www.quadtonerip.com/html/QTRprinttool.html "Print-Tool") is a
      very suitable tool, albeit non-free.

    If the ``use_high_density_mode`` is set to True the system uses the i1pro patch
    pattern which is much denser than the one for ColorMunki.

    If the ``use_high_density_mode`` is set to anything other than True, then the system
    will use two A4 pages or one A3 page use:

    420 patches for A4 (in 2 A4 pages)
    460 patches for A3

    by setting the device to ``i1pro`` and the margins to 2 mm it is possible to print
    672 (28x24) 7x8.75 mm patches for A4 and 1392 (58x24) 7x8.75 mm patches for A3 on a
    single page.

    what I want to achieve here is to use the minimum amount of paper for
    profiling and still have an excellent result

    Generated temp files are located under these folders:

        For Windows:

            $APPDATA/ICCGenerator/%{printer_brand}_%{printer_model}/%{profile_date}

        For Linux nad MacOS:

            ~/.cache/IccGenerator/%{printer_brand}_%{printer_model}/%{profile_date}

    folders.

    The final ICC profiles will be placed under these folders:

        For Windows:

            %WINDIR%/System32/spool/drivers/color/

        For Linux:

            ~/.local/share/icc/

        For MacOS:

            ~/Library/ColorSync/Profiles/

    """

    NORMAL_DENSITY = "normal_density"
    HIGH_DENSITY = "high_density"

    __data__ = {
        "paper_size": {
            PaperSizeLibrary.p11x17: {
                "patch_count": {
                    NORMAL_DENSITY: int(
                        210
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["11x17"].area
                    ),
                    HIGH_DENSITY: int(
                        672
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["11x17"].area
                    ),
                }
            },
            PaperSizeLibrary.p4x6: {
                "patch_count": {
                    NORMAL_DENSITY: int(
                        210
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["4x6"].area
                    ),
                    HIGH_DENSITY: int(
                        672
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["4x6"].area
                    ),
                }
            },
            PaperSizeLibrary.A2: {
                "patch_count": {
                    NORMAL_DENSITY: int(
                        445
                        / PaperSizeLibrary.paper_sizes["A3"].area
                        * PaperSizeLibrary.paper_sizes["A2"].area
                    ),
                    HIGH_DENSITY: int(
                        1392
                        / PaperSizeLibrary.paper_sizes["A3"].area
                        * PaperSizeLibrary.paper_sizes["A2"].area
                    ),
                }
            },
            PaperSizeLibrary.A3: {
                "patch_count": {
                    NORMAL_DENSITY: 445,
                    HIGH_DENSITY: 1392,
                }
            },
            PaperSizeLibrary.A3R: {
                "patch_count": {
                    NORMAL_DENSITY: 445,
                    HIGH_DENSITY: 1392,
                }
            },
            PaperSizeLibrary.A4: {
                "patch_count": {
                    NORMAL_DENSITY: 210,
                    HIGH_DENSITY: 672,
                }
            },
            PaperSizeLibrary.A4R: {
                "patch_count": {
                    NORMAL_DENSITY: 210,
                    HIGH_DENSITY: 672,
                }
            },
            PaperSizeLibrary.Legal: {
                "patch_count": {
                    NORMAL_DENSITY: int(
                        210
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["Legal"].area
                    ),
                    HIGH_DENSITY: int(
                        672
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["Legal"].area
                    ),
                }
            },
            PaperSizeLibrary.Letter: {
                "patch_count": {
                    NORMAL_DENSITY: int(
                        210
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["Letter"].area
                    ),
                    HIGH_DENSITY: int(
                        672
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["Letter"].area
                    ),
                }
            },
            PaperSizeLibrary.LetterR: {
                "patch_count": {
                    NORMAL_DENSITY: int(
                        210
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["LetterR"].area
                    ),
                    HIGH_DENSITY: int(
                        672
                        / PaperSizeLibrary.paper_sizes["A4"].area
                        * PaperSizeLibrary.paper_sizes["LetterR"].area
                    ),
                }
            },
        }
    }

    def __init__(
        self,
        printer_brand: str = "Canon",
        printer_model: str = "iX6850",
        paper_brand: str = "Kodak",
        paper_model: str = "UPPP",
        paper_finish: str = "Glossy",
        paper_size: Union[None, PaperSize] = None,
        ink_brand: str = "CanonInk",
        use_high_density_mode: bool = True,
        number_of_pages: int = 1,
        copyright_info: str = "",
        precondition_profile_path: Union[str, pathlib.Path] = "",
        output_commands: bool = False,
        gray_patch_count: int = 128,
    ):
        self.output_commands = output_commands

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

        # set the default value for paper_size
        if paper_size is None:
            paper_size = PaperSizeLibrary.A4
        self._paper_size = None
        self.paper_size = paper_size

        self._ink_brand = None
        self.ink_brand = ink_brand

        self._use_high_density_mode = None
        self.use_high_density_mode = use_high_density_mode

        self._number_of_pages = None
        self.number_of_pages = number_of_pages

        self._gray_patch_count = None
        self.gray_patch_count = gray_patch_count

        self._copyright_info = None
        self.copyright_info = copyright_info

        self._precondition_profile_path = None
        self.precondition_profile_path = precondition_profile_path

        now = datetime.datetime.now()
        date_str = now.strftime("%Y%m%d")
        time_str = now.strftime("%H%M")

        self.profile_date = date_str
        self.profile_time = time_str

        # Profile Path template
        self._profile_path_template = (
            "~/.cache/ICCGenerator/{printer_brand}_" "{printer_model}/{profile_date}"
        )

        # Profile name template
        self.profile_name_template = (
            "{printer_brand}_{printer_model}_{paper_brand}_"
            "{paper_model}_{paper_finish}_{paper_size}_{ink_brand}_"
            "{profile_date}_{profile_time}"
        )
        self._profile_name = ""

        self.tif_files = []

        # The output path is defined by the Operating system
        system_name = platform.system().lower()
        self.output_path = pathlib.Path("~/.local/share/icc/").expanduser()

        if "win32" in system_name:
            self.output_path = pathlib.Path(
                os.path.expandvars("%WINDIR%/System32/spool/drivers/color/")
            )
        elif "darwin" in system_name:
            self.output_path = pathlib.Path(
                "~/Library/ColorSync/Profiles/"
            ).expanduser()

    def save_settings(self, path: Union[str, pathlib.Path] = None):
        """Save the settings to the given path.

        Args:
            path (Union[str, pathlib.Path]): The settings file path. If skipped the
                profile path will be used along with the profile name to generate a
                proper profile path.

        Raises:
            TypeError: If the given path doesn't exist.
        """
        if not path:
            path = self.profile_path / f"{self.profile_name}.json"

        if not isinstance(path, (str, pathlib.Path)):
            raise TypeError("Please specify a valid path")

        if isinstance(path, str):
            path = pathlib.Path(path)

        data = {
            "ink_brand": self.ink_brand,
            "paper_brand": self.paper_brand,
            "paper_finish": self.paper_finish,
            "paper_model": self.paper_model,
            "paper_size": self.paper_size.name,
            "printer_brand": self.printer_brand,
            "printer_model": self.printer_model,
            "profile_date": self.profile_date,
            "profile_time": self.profile_time,
        }

        # create the folder
        os.makedirs(path.parent, exist_ok=True)

        logger.info(f"Saving profile settings to: {path.resolve()}")
        with open(path, "w+") as f:
            json.dump(data, f)

    def load_settings(self, path: Union[str, pathlib.Path]):
        """Load the settings from the given path.

        Args:
            path (Union[str, pathlib.Path]): The path to load the data from.

        Raises:
            TypeError: If the given path arg value is not a str or pathlib.Path
                instance.
            RuntimeError: If the given path doesn't exist.
        """
        if not path or not isinstance(path, (str, pathlib.Path)):
            raise TypeError("Please specify a valid path")

        if isinstance(path, str):
            path = pathlib.Path(path)

        if not path.exists():
            raise RuntimeError(f"File does not exist!: {path}")

        with open(path, "r") as f:
            data = json.load(f)

        self.ink_brand = data["ink_brand"]
        self.paper_brand = data["paper_brand"]
        self.paper_finish = data["paper_finish"]
        self.paper_model = data["paper_model"]
        self.paper_size = PaperSizeLibrary.get_paper_size(data["paper_size"])
        self.printer_brand = data["printer_brand"]
        self.printer_model = data["printer_model"]
        self.profile_date = data["profile_date"]
        self.profile_time = data["profile_time"]

    @property
    def printer_brand(self) -> str:
        """Return printer_brand attribute value.

        Returns:
            str: The printer brand.
        """
        return self._printer_brand

    @printer_brand.setter
    def printer_brand(self, printer_brand: str):
        """Set the printer_brand attribute.

        Args:
            printer_brand (str): The printer brand.

        Raises:
            TypeError: If the given printer_brand arg value is not a str.
        """
        if not printer_brand or not isinstance(printer_brand, str):
            raise TypeError(
                f"{self.__class__.__name__}.printer_brand should be a str, "
                f"not {printer_brand.__class__.__name__}"
            )
        self._printer_brand = printer_brand

    @property
    def printer_model(self) -> str:
        """Return the printer_model attribute value.

        Returns:
            str: The printer_model attribute value.
        """
        return self._printer_model

    @printer_model.setter
    def printer_model(self, printer_model: str):
        """Set the printer_model attribute.

        Args:
            printer_model (str): The printer_model.

        Raises:
            TypeError: If the given printer_model arg value is not a str.
        """
        if not printer_model or not isinstance(printer_model, str):
            raise TypeError(
                f"{self.__class__.__name__}.printer_model should be a str, "
                f"not {printer_model.__class__.__name__}"
            )
        self._printer_model = printer_model

    @property
    def paper_brand(self) -> str:
        """Return the paper_brand attribute value.

        Returns:
            str: The paper_brand attribute value.
        """
        return self._paper_brand

    @paper_brand.setter
    def paper_brand(self, paper_brand: str):
        """Set the paper_brand attribute.

        Args:
            paper_brand (str): The paper_brand.

        Raises:
            TypeError: If the given paper_brand arg value is not a str.
        """
        if not paper_brand or not isinstance(paper_brand, str):
            raise TypeError(
                f"{self.__class__.__name__}.paper_brand should be a str, "
                f"not {paper_brand.__class__.__name__}"
            )
        self._paper_brand = paper_brand

    @property
    def paper_model(self) -> str:
        """Return the paper_model attribute value.

        Returns:
            str: The paper_model attribute value.
        """
        return self._paper_model

    @paper_model.setter
    def paper_model(self, paper_model: str):
        """Set the paper_model attribute.

        Args:
            paper_model (str): The paper_model.

        Raises:
            TypeError: If the given paper_model arg value is not a str.
        """
        if not paper_model or not isinstance(paper_model, str):
            raise TypeError(
                f"{self.__class__.__name__}.paper_model should be a str, "
                f"not {paper_model.__class__.__name__}"
            )
        self._paper_model = paper_model

    @property
    def paper_finish(self) -> str:
        """Return the paper_finish attribute value.

        Returns:
            str: The paper_finish attribute value.
        """
        return self._paper_finish

    @paper_finish.setter
    def paper_finish(self, paper_finish: str):
        """Set the paper_finish attribute.

        Args:
            paper_finish (str): The paper finish (i.e Glossy, Matte).

        Raises:
            TypeError: If the given paper_finish arg value is not a str.
        """
        if not paper_finish or not isinstance(paper_finish, str):
            raise TypeError(
                f"{self.__class__.__name__}.paper_finish should be a str, "
                f"not {paper_finish.__class__.__name__}"
            )
        self._paper_finish = paper_finish

    @property
    def paper_size(self) -> PaperSize:
        """Return the paper_size attribute value.

        Returns:
            PaperSize: The paper_size attribute value.
        """
        return self._paper_size

    @paper_size.setter
    def paper_size(self, paper_size: PaperSize):
        """Set the paper_size attribute.

        Args:
            paper_size (PaperSize): The paper size.

        Raises:
            TypeError: If the given paper_size attribute value is not a PaperSize
                instance.
        """
        if not paper_size or not isinstance(paper_size, PaperSize):
            raise TypeError(
                f"{self.__class__.__name__}.paper_size should be a PaperSize instance, "
                f"not {paper_size.__class__.__name__}"
            )
        self._paper_size = paper_size

    @property
    def ink_brand(self) -> str:
        """Return the ink_brand attribute value.

        Returns:
            str: The ink_brand attribute value.
        """
        return self._ink_brand

    @ink_brand.setter
    def ink_brand(self, ink_brand: str):
        """Set the ink_brand attribute.

        Args:
            ink_brand (str): The ink brand.

        Raises:
            TypeError: If the given ink_brand arg value is not a str.
        """
        if not ink_brand or not isinstance(ink_brand, str):
            raise TypeError(
                f"{self.__class__.__name__}.ink_brand should be a str, "
                f"not {ink_brand.__class__.__name__}"
            )
        self._ink_brand = ink_brand

    @property
    def use_high_density_mode(self):
        """Return the use_high_density_mode attribute value.

        Returns:
            bool: The use_high_density_mode attribute value.
        """
        return self._use_high_density_mode

    @use_high_density_mode.setter
    def use_high_density_mode(self, use_high_density_mode: bool):
        """Set the use_high_density_mode attribute value.

        Args:
            use_high_density_mode (bool): If set to to True (default) higher resolution
                for the patches will be used, which will increase the patches printed
                per page, allowing less paper use for profiling.

        Raises:
            TypeError: If the given use_high_density_mode arg value is not a bool.
        """
        if not isinstance(use_high_density_mode, bool):
            raise TypeError(
                f"{self.__class__.__name__}.use_high_density_mode should be a bool "
                f"(True or False), not {use_high_density_mode.__class__.__name__}"
            )
        self._use_high_density_mode = use_high_density_mode

    @property
    def number_of_pages(self) -> int:
        """Return the number_of_pages attribute value.

        Returns:
            int: The number_of_pages attribute value.
        """
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages: int):
        """Set the number_of_pages attribute.

        Args:
            number_of_pages (int): The number of pages.

        Raises:
            TypeError: If the given number_of_pages arg value is not an int.
        """
        if not number_of_pages or not isinstance(number_of_pages, int):
            raise TypeError(
                f"{self.__class__.__name__}.number_of_pages should be a int, "
                f"not {number_of_pages.__class__.__name__}"
            )
        self._number_of_pages = number_of_pages

    @property
    def copyright_info(self) -> str:
        """Return the copyright_info attribute value.

        Returns:
            str: The copyright_info attribute value.
        """
        return self._copyright_info

    @copyright_info.setter
    def copyright_info(self, copyright_info: str):
        """Set the copyright_info attribute.

        Args:
            copyright_info (str): The copyright info value.

        Raises:
            TypeError: If the given copyright_info is not a str.
        """
        if not isinstance(copyright_info, str):
            raise TypeError(
                f"{self.__class__.__name__}.copyright_info should be a str, "
                f"not {copyright_info.__class__.__name__}"
            )
        self._copyright_info = copyright_info

    @property
    def precondition_profile_path(self) -> Union[None, pathlib.Path]:
        """Return the precondition_profile_path attribute value.

        Returns:
            Union[None, pathlib.Path]: The precondition_profile_path.
        """
        return self._precondition_profile_path

    @precondition_profile_path.setter
    def precondition_profile_path(
        self, precondition_profile_path: Union[str, pathlib.Path]
    ):
        """Set the precondition_profile_path attribute value.

        Args:
            precondition_profile_path (Union[str, pathlib.Path]): The precondition
                profile path.

        Raises:
            TypeError: If the precondition_profile_path arg value is not a str or
                pathlib.Path instance.
        """
        # TODO: precondition_profile_path can also be pathlib.Path
        if not isinstance(precondition_profile_path, str):
            raise TypeError(
                f"{self.__class__.__name__}.precondition_profile_path should be a str, "
                f"not {precondition_profile_path.__class__.__name__}"
            )
        self._precondition_profile_path = precondition_profile_path

    @property
    def profile_path(self) -> pathlib.Path:
        """Return the profile_path attribute.

        Returns:
            pathlib.Path: The rendered profile path value.
        """
        # update the output path according to the OS
        return pathlib.Path(
            self._profile_path_template.format(
                printer_brand=self.printer_brand,
                printer_model=self.printer_model,
                paper_brand=self.paper_brand,
                paper_model=self.paper_model,
                paper_finish=self.paper_finish,
                paper_size=self.paper_size.name,
                ink_brand=self.ink_brand,
                profile_date=self.profile_date,
                profile_time=self.profile_time,
            )
        ).expanduser()

    @property
    def profile_absolute_path(self) -> pathlib.Path:
        """Return the absolute path of profile_path variable.

        Returns:
            pathlib.Path: The absolute path of the profile.
        """
        return self.profile_path.resolve()

    @property
    def profile_absolute_full_path(self) -> pathlib.Path:
        """Return the absolute path of the profile_path property.

        Returns:
            pathlib.Path: The absolute path of the profile_path property.
        """
        return self.profile_absolute_path / self.profile_name

    def render_profile_name(self) -> str:
        """Return the rendered profile name.

        Returns:
            str: The rendered profile name.
        """
        return self.profile_name_template.format(
            printer_brand=self.printer_brand,
            printer_model=self.printer_model,
            paper_brand=self.paper_brand,
            paper_model=self.paper_model,
            paper_finish=self.paper_finish,
            paper_size=self.paper_size.name,
            ink_brand=self.ink_brand,
            profile_date=self.profile_date,
            profile_time=self.profile_time,
        )

    @property
    def profile_name(self) -> str:
        """Return the profile_name attribute value.

        Returns:
            str: The profile_name attribute value.
        """
        if not self._profile_name:
            self.profile_name = self.render_profile_name()
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name: str):
        """Set the profile_name attribute value.

        Args:
            profile_name (str): The profile name.
        """
        self._profile_name = profile_name

    @property
    def per_page_patch_count(self) -> int:
        """Return the per_page_patch_count attribute value.

        Returns:
            int: The per page patch count value.
        """
        # Per Page Patch Count is Defined by the Paper Size and
        # the High Resolution mode
        resolution_str = (
            self.HIGH_DENSITY if self.use_high_density_mode else self.NORMAL_DENSITY
        )
        return self.__data__["paper_size"][self.paper_size]["patch_count"][
            resolution_str
        ]

    @property
    def patch_count(self) -> int:
        """Return the patch_count attribute.

        Uses the per_page_patch_count and number_of_pages to figure out the total number
        of patches.

        Returns:
            int: The calculated patch count.
        """
        return self.per_page_patch_count * self.number_of_pages

    @property
    def gray_patch_count(self) -> int:
        """Return the gray_patch_count attribute value.

        Returns:
            int: The gray path count.
        """
        return self._gray_patch_count

    @gray_patch_count.setter
    def gray_patch_count(self, gray_patch_count: int):
        """Set the gray_patch_count attribute.

        Args:
            gray_patch_count (int): The gray path count.

        Raises:
            TypeError: If the given gray_path_count is not an int.
        """
        if not gray_patch_count or not isinstance(gray_patch_count, int):
            raise TypeError(
                f"{self.__class__.__name__}.gray_patch_count should be an int, "
                f"not {gray_patch_count.__class__.__name__}"
            )

        self._gray_patch_count = gray_patch_count

    @classmethod
    def run_external_process(cls, command: list, shell: bool = False):
        """Run an external process and yields the output.

        Args:
            command (list): The command to run.
            shell (bool): A bool value for executing the command in shell or not.

        Raises:
            RuntimeError: If the command return code is not 0.

        Yields:
            str: The command output.
        """
        if not shell:
            process = subprocess.Popen(command, stderr=subprocess.PIPE)
            # loop until process finishes and capture stderr output
            stderr_buffer = []
            while True:
                stderr = process.stderr.readline()

                if stderr == b"" and process.poll() is not None:
                    break

                if stderr != b"":
                    stderr = stderr.decode("utf-8").strip()
                    stderr_buffer.append(stderr)
                    yield stderr

            # flatten the buffer
            stderr_buffer = "\n".join(stderr_buffer)
            return_code = process.returncode

            if return_code:
                # there is an error
                raise RuntimeError(stderr_buffer)
        else:
            command = " ".join(command)
            os.system(command)

    def generate_target(self):
        """Generate the required ti1 file."""
        os.makedirs(self.profile_absolute_path, exist_ok=True)

        # ************************
        # targen command
        command = [
            "targen",
            "-v",
            "-d",
            "2",
            "-G",
            "-g",
            f"{self.gray_patch_count}",
            "-f",
            f"{self.patch_count}",
        ]
        if self.precondition_profile_path:
            command += ["-c", self.precondition_profile_path]
        command += [str(self.profile_absolute_full_path)]

        # first call the targen command
        # yield from self.run_external_process(command)
        if self.output_commands:
            print("command: {}".format(" ".join(command)))
        for output in self.run_external_process(command):
            print(output)

    def generate_tif(self):
        """Generate the required Tiff file or files depending on the page count."""
        os.makedirs(self.profile_absolute_path, exist_ok=True)

        # ************************
        # printtarg command
        command = ["printtarg", "-v"]
        if self.use_high_density_mode:
            command += ["-ii1", "-a 0.875"]  # Use an i1 Pro
        else:
            command += ["-iCM", "-h", "-P"]  # Use a ColorMunki

        command += [
            "-R1",
            "-T300",
            "-M2",
            "-L",
            "-p",
            "{:0.1f}x{:0.1f}".format(*self.paper_size.size),
            str(self.profile_absolute_full_path),
        ]

        self.update_tif_files()

        # first call the targen command
        # print("generate_tif_files command: {}".format(' '.join(command)))
        # yield from self.run_external_process(command)
        if self.output_commands:
            print("command: {}".format(" ".join(command)))
        for output in self.run_external_process(command):
            print(output)

    def update_tif_files(self):
        """Update the tiff file paths."""
        # update tif files
        self.tif_files = []
        if self.number_of_pages == 1:
            self.tif_files.append(
                (self.profile_path / f"{self.profile_name}.tif").resolve()
            )
        else:
            for i in range(self.number_of_pages):
                self.tif_files.append(
                    (
                        self.profile_path / f"{self.profile_name}_{i + 1:02}.tif"
                    ).resolve()
                )

    def print_charts(self):
        """Run the proper application with the charts already open.

        For Windows, it will first try to run Dry Creek Photo Print Utility if exist and
        if not then it will try to run Adobe Color Printer Utility, and if it doesn't
        exist either it will raise a proper RuntimeError stating that the user should
        install Dry Creek Photo Print Utility or ACPU.

        For Linux, it will first check if GIMP and GutenPrint is installed, if not will
        raise a RuntimeError to inform the user, if they exist properly it will open
        GIMP with the Tiff file.
        """
        command = []
        system_name = platform.system().lower()
        if "win32" in system_name:  # Windows
            # call Dry Creek Photo Print Utility first
            # if it fails then try to call ACPU
            # if this fails too, raise a RuntimeError
            # TODO: implement and test this on Windows
            pass
        elif "linux" in system_name:  # Linux
            # call Gimp with the TIFF Files
            command = ["/usr/bin/gimp"] + self.tif_files
        elif "darwin" in system_name:
            # command = [
            #     '/Applications/Adobe Color Printer Utility.app'
            #     '/Contents/MacOS/Adobe Color Printer Utility'
            # ] + self.tif_files
            command = [
                "/Applications/Print-Tool.app/Contents/MacOS/Print-Tool"
            ] + self.tif_files

        if self.output_commands:
            print("command: {}".format(" ".join(command)))
        for output in self.run_external_process(command):
            print(output)

    def read_charts(self, resume: bool = False, read_mode: int = 0):
        """Read the printed chart using the device.

        Args:
            resume (bool): If a .ti3 files already exists and ``resume`` is set to True.
                The process will start from where it left before. Default value is
                False.
            read_mode (int): There are two possible modes:
                0: Strip Mode
                1: Patch-By-Patch
                Use ``read_mode=1`` (Patch-By-Patch) with ``resume=True`` to fix
                erroneously read patches.
        """
        os.makedirs(self.profile_absolute_path, exist_ok=True)

        # ************************
        # chartread command
        command = ["chartread", "-v", "-H", "-T 0.4"]
        if read_mode == 1:
            command += ["-p", "-P"]

        if resume:
            command += ["-r"]

        command += [str(self.profile_absolute_full_path)]

        # first call the targen command
        if self.output_commands:
            print("command: {}".format(" ".join(command)))
        for output in self.run_external_process(command, shell=True):
            print(output)

    def generate_profile(self):
        """Generate the profile."""
        os.makedirs(self.profile_absolute_path, exist_ok=True)

        # ************************
        # colprof command
        command = [
            "colprof",
            "-v",
            "-qh",
            "-r0.5",
            "-S",
            str(HERE.parent / "data" / "AdobeRGB.icc"),
            "-cmt",
            "-dpp",
            "-Zr",
            "-Zm",
            f"-D{self.profile_name}",
        ]

        if self.copyright_info:
            command.append(f"-C{self.copyright_info}")

        command += [str(self.profile_absolute_full_path)]

        # call the command
        # yield from self.run_external_process(command)
        if self.output_commands:
            print("command: {}".format(" ".join(command)))
        for output in self.run_external_process(command):
            print(output)

    def check_profile(self, sort_by_de: bool = False):
        """Check the profile quality.

        Args:
            sort_by_de (bool): Sort by dE value or not. Default is False.
        """
        os.makedirs(self.profile_absolute_path, exist_ok=True)

        # ************************
        # prof_check
        command = [
            "profcheck",
            "-k",
            "-v2",
        ]
        if sort_by_de:
            command.append("-s")

        command.append(f"{self.profile_absolute_full_path}.ti3")

        system_name = platform.system().lower()
        if "win32" in system_name:
            # windows uses *.icm file extension
            command.append(f"{self.profile_absolute_full_path}.icm")
        else:
            # OSX and Linux uses *.icc file extension
            command.append(f"{self.profile_absolute_full_path}.icc")

        # call the command
        # yield from self.run_external_process(command)
        if self.output_commands:
            print("command: {}".format(" ".join(command)))
        for output in self.run_external_process(command):
            print(output)

    def install_profile(self):
        """Install the generated profile to appropriate folders for the current OS.

        For Windows:
            %WINDIR%/System32/spool/drivers/color/

        For Linux:
            ~/.local/share/icc/

        For MacOS:
            ~/Library/ColorSync/Profiles/

        Raises:
            RuntimeError: If icc_profile_absolute_full_path doesn't exist.
        """
        # check if the profile is not generated yet
        icc_profile_absolute_full_path = self.profile_absolute_full_path.with_suffix(
            ".icc"
        )
        if not icc_profile_absolute_full_path.exists():
            raise RuntimeError("ICC file doesn't exist, please generate it first!")

        profile_install_path = self.output_path / f"{self.profile_name}.icc"
        try:
            shutil.copy2(icc_profile_absolute_full_path, profile_install_path)
        except Exception:
            traceback.print_exc()
        else:
            logger.info(f"Profile installed: {self.profile_absolute_path}")

    @classmethod
    def color_correct_image(
        cls,
        printer_profile_path: Union[str, pathlib.Path] = None,
        input_image_path: Union[str, pathlib.Path] = None,
        output_image_path: Union[str, pathlib.Path, None] = None,
        image_profile: Union[str, pathlib.Path] = "AdobeRGB",
        intent: str = "r",
    ):
        """Apply color correction to the given image.

        Accepts TIFF or JPEG files.

        cctiff
         ~/.local/share/icc/Canon_iX6850_Generic_Plain_Matte_A4_CanonInk_20210207_1402.icc
         ~/Documents/development/ICCGenerator/sRGB.icc
         Primary_Colors_3.jpeg
         Primary_Colors_3_corrected2.jpeg

        cctiff
          ~/Documents/development/ICCGenerator/sRGB-elle-V2-srgbtrc.icc
          ~/.local/share/icc/Canon_iX6850_Generic_Plain_Matte_A4_CanonInk_20210207_1402.icc
          Primary_Colors_3.jpeg
          Primary_Colors_3_corrected.jpeg

        Args:
            printer_profile_path (Union[str, pathlib.Path]): The path of the ICC/ICM
                file of the printer profile.
            image_profile (Union[str, pathlib.Path]): Can be either "sRGB" or
                "AdobeRGB", default is "AdobeRGB".
            input_image_path (Union[str, pathlib.Path]): The input JPG/TIFF image path.
            output_image_path (Uniton[str, pathlib.Path, None]): The output TIFF image
                path. Can be set to None then a suitable path will be generated
                automatically.
            intent (str): Rendering intent, one of the following:

                p = perceptual, r = relative colorimetric (default)
                s = saturation, a = absolute colorimetric

        Raises:
            ValueError: Raises ValueError in following conditions:
                - If printer_profile_path doesn't exist.
                - If printer_profile_path suffix is not ".icc" or ".icm".
                - If image_profile_path doesn't exist.
                - If input_image_path doesn't exist.
                - If input_image_path suffix is not one of ".jpg", ".tif" or ".tiff"
                - If output_image_path suffix is not one of ".jpg", ".tif" or ".tiff"
                - If intent is not one of ["p", "r", "s", "a"].
                - If image_profile filename isn't one of "AdobeRGB" or "sRGB".
            TypeError: Raises TypeError in following conditions:
                - If printer_profile_path is not a str or pathlib.Path instance.
                - If input_path is not a str or pathlib.Path instance.
                - If intent is not a str.
                - If image_profile is not a str or pathlib.Path.
        """
        # ---------------------
        # Printer Profile Path
        if printer_profile_path is None or not isinstance(
            printer_profile_path, (str, pathlib.Path)
        ):
            raise TypeError("Please specify a proper printer_profile_path!")

        if isinstance(printer_profile_path, str):
            printer_profile_path = pathlib.Path(printer_profile_path)

        if not printer_profile_path.exists():
            raise ValueError(
                f"printer_profile_path doesn't exists: {printer_profile_path}"
            )

        if printer_profile_path.suffix.lower() not in [".icc", ".icm"]:
            raise ValueError(
                f"printer_profile_path should be a valid ICC/ICM file: "
                f"{printer_profile_path}"
            )

        # ---------------------
        # Input Image Path
        if not isinstance(input_image_path, (str, pathlib.Path)):
            raise TypeError("Please specify a proper input_image_path!")

        if isinstance(input_image_path, str):
            input_image_path = pathlib.Path(input_image_path)

        if not input_image_path.exists():
            raise ValueError(f"input_image_path doesn't exists: {input_image_path}")

        if input_image_path.suffix.lower() not in [".jpg", ".tif", ".tiff"]:
            raise ValueError(
                f"input_image_path should be a valid JPG/TIF file: {input_image_path}"
            )

        if not output_image_path:
            # generate the output_image_path from input_image_path
            dir_name = input_image_path.parent
            base_name_wo_ext = input_image_path.stem
            ext = input_image_path.suffix
            i = 1
            while i < 100000:
                output_image_path = dir_name / f"{base_name_wo_ext}_corrected_{i}{ext}"
                if not output_image_path.exists():
                    break
                i += 1
        else:
            if isinstance(output_image_path, str):
                output_image_path = pathlib.Path(output_image_path)

        if output_image_path.suffix.lower() not in [
            ".jpg",
            ".tif",
            ".tiff",
        ]:
            raise ValueError(
                f"output_image_path should be a valid JPG/TIF file: {output_image_path}"
            )

        # ---------------------
        # Intent
        if not intent:
            # use default
            intent = "r"

        if not isinstance(intent, str):
            raise TypeError(f"intent should be a str, not {intent.__class__.__name__}")

        if intent not in ["p", "r", "s", "a"]:
            raise ValueError(f"intent should be one of p, r, s, a, not {intent}")

        # ---------------------
        # Image Profile
        if image_profile is None:
            image_profile = "AdobeRGB"

        if not isinstance(image_profile, (str, pathlib.Path)):
            raise TypeError(
                f"image_profile should be one of sRGB or AdobeRGB, not {image_profile}"
            )

        image_profile = pathlib.Path(image_profile)
        if not image_profile.is_file():
            base_name = image_profile.stem
            if base_name.lower() not in ["adobergb", "srgb"]:
                raise ValueError(
                    f"image_profile should be one of sRGB or AdobeRGB, not "
                    f"{image_profile}"
                )
            image_profile_path = HERE.parent / f"{image_profile}.icc"
        else:
            image_profile_path = image_profile

        # ************************
        # cctiff
        command = [
            "cctiff",
            "-i",
            intent,
            "-p",
            str(image_profile_path),
            str(printer_profile_path),
            str(input_image_path),
            str(output_image_path),
        ]

        # call the command
        # yield from self.run_external_process(command)
        print("command: {}".format(" ".join(command)))
        for output in cls.run_external_process(command):
            print(output)
