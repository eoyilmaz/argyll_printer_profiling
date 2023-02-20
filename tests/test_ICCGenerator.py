# -*- coding: utf-8 -*-
"""Tests for the ICCGenerator class."""

import datetime
import json
import logging
import os
import platform
import tempfile

import pytest

from icc_generator import logger
from icc_generator.api import ICCGenerator, HERE, PaperSizeLibrary


def test_initializing_without_any_args():
    """class ICCGenerator initializes correctly."""
    icc_gen = ICCGenerator()

    # check default values
    assert icc_gen.printer_brand == "Canon"
    assert icc_gen.printer_model == "iX6850"
    assert icc_gen.paper_brand == "Kodak"
    assert icc_gen.paper_model == "UPPP"
    assert icc_gen.paper_finish == "Glossy"
    assert icc_gen.paper_size == PaperSizeLibrary.A4
    assert icc_gen.ink_brand == "CanonInk"
    assert icc_gen.use_high_density_mode is True
    assert icc_gen.number_of_pages == 1
    assert icc_gen.copyright_info == ""


def test_printer_brand_arg_is_skipped():
    """Default value is used if printer_brand arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.printer_brand == "Canon"


def test_printer_brand_arg_is_none():
    """printer_brand arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(printer_brand=None)
    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not NoneType"


def test_printer_brand_attr_is_set_to_none():
    """TypeError raised if printer_brand attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_brand = None
    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not NoneType"


def test_printer_brand_arg_is_not_a_str():
    """TypeError raised if printer_brand arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(printer_brand=312)
    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not int"


def test_printer_brand_attr_is_not_set_to_a_str():
    """TypeError raised if printer_brand attr is not a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_brand = 443

    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not int"


def test_printer_brand_arg_is_working_properly():
    """printer_brand arg value is properly passed to the printer_brand attr."""
    test_value = "Epson"
    icc_gen = ICCGenerator(printer_brand=test_value)
    assert icc_gen.printer_brand == test_value


def test_printer_brand_attr_is_working_properly():
    """printer_brand attr is working properly."""
    test_value = "Epson"
    icc_gen = ICCGenerator()
    assert icc_gen.printer_brand != test_value
    icc_gen.printer_brand = test_value
    assert icc_gen.printer_brand == test_value


def test_printer_model_arg_is_skipped():
    """default value is used if printer_model arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.printer_model == "iX6850"


def test_printer_model_arg_is_none():
    """printer_model arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(printer_model=None)
    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not NoneType"


def test_printer_model_attr_is_set_to_none():
    """TypeError raised if printer_model attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_model = None

    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not NoneType"


def test_printer_model_arg_is_not_a_str():
    """TypeError raised if printer_model arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(printer_model=312)
    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not int"


def test_printer_model_attr_is_not_set_to_a_str():
    """TypeError raised if printer_model attr is not a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_model = 443
    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not int"


def test_printer_model_arg_is_working_properly():
    """printer_model arg value is properly passed to the printer_model attr."""
    test_value = "iP7250"
    icc_gen = ICCGenerator(printer_model=test_value)
    assert icc_gen.printer_model == test_value


def test_printer_model_attr_is_working_properly():
    """printer_model attr is working properly."""
    test_value = "iP7250"
    icc_gen = ICCGenerator()
    assert icc_gen.printer_model != test_value
    icc_gen.printer_model = test_value
    assert icc_gen.printer_model == test_value


def test_paper_brand_arg_is_skipped():
    """default value is used if paper_brand arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.paper_brand == "Kodak"


def test_paper_brand_arg_is_none():
    """paper_brand arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(paper_brand=None)
    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not NoneType"


def test_paper_brand_attr_is_set_to_none():
    """TypeError raised if paper_brand attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_brand = None
    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not NoneType"


def test_paper_brand_arg_is_not_a_str():
    """TypeError raised if paper_brand arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(paper_brand=312)

    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not int"


def test_paper_brand_attr_is_not_set_to_a_str():
    """TypeError raised if paper_brand attr is set to a value other than a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_brand = 443
    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not int"


def test_paper_brand_arg_is_working_properly():
    """paper_brand arg value is properly passed to the paper_brand attr."""
    test_value = "Hahnemuhle"
    icc_gen = ICCGenerator(paper_brand=test_value)
    assert icc_gen.paper_brand == test_value


def test_paper_brand_attr_is_working_properly():
    """paper_brand attr is working properly."""
    test_value = "Hahnemuhle"
    icc_gen = ICCGenerator()
    assert icc_gen.paper_brand != test_value
    icc_gen.paper_brand = test_value
    assert icc_gen.paper_brand == test_value


def test_paper_model_arg_is_skipped():
    """default value is used if paper_model arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.paper_model == "UPPP"


def test_paper_model_arg_is_none():
    """paper_model arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(paper_model=None)
    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not NoneType"


def test_paper_model_attr_is_set_to_none():
    """TypeError raised if paper_model attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_model = None
    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not NoneType"


def test_paper_model_arg_is_not_a_str():
    """TypeError raised if paper_model arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(paper_model=312)
    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not int"


def test_paper_model_attr_is_not_set_to_a_str():
    """TypeError raised if paper_model attr is set to a value other than a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_model = 443
    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not int"


def test_paper_model_arg_is_working_properly():
    """paper_model arg value is properly passed to the paper_model attr."""
    test_value = "FineArt"
    icc_gen = ICCGenerator(paper_model=test_value)
    assert icc_gen.paper_model == test_value


def test_paper_model_attr_is_working_properly():
    """paper_model attr is working properly."""
    test_value = "FineArt"
    icc_gen = ICCGenerator()
    assert icc_gen.paper_model != test_value
    icc_gen.paper_model = test_value
    assert icc_gen.paper_model == test_value


def test_paper_finish_arg_is_skipped():
    """default value is used if paper_finish arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.paper_finish == "Glossy"


def test_paper_finish_arg_is_none():
    """paper_finish arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(paper_finish=None)
    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not NoneType"


def test_paper_finish_attr_is_set_to_none():
    """TypeError raised if paper_finish attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_finish = None
    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not NoneType"


def test_paper_finish_arg_is_not_a_str():
    """TypeError raised if paper_finish arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(paper_finish=312)
    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not int"


def test_paper_finish_attr_is_not_set_to_a_str():
    """TypeError raised if paper_finish attr is set to a value other than a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_finish = 443
    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not int"


def test_paper_finish_arg_is_working_properly():
    """paper_finish arg value is properly passed to the paper_finish attr."""
    test_value = "Silk"
    icc_gen = ICCGenerator(paper_finish=test_value)
    assert icc_gen.paper_finish == test_value


def test_paper_finish_attr_is_working_properly():
    """paper_finish attr is working properly."""
    test_value = "Silk"
    icc_gen = ICCGenerator()
    assert icc_gen.paper_finish != test_value
    icc_gen.paper_finish = test_value
    assert icc_gen.paper_finish == test_value


def test_ink_brand_arg_is_skipped():
    """default value is used if ink_brand arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.ink_brand == "CanonInk"


def test_ink_brand_arg_is_none():
    """ink_brand arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(ink_brand=None)
    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not NoneType"


def test_ink_brand_attr_is_set_to_none():
    """TypeError raised if ink_brand attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.ink_brand = None
    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not NoneType"


def test_ink_brand_arg_is_not_a_str():
    """TypeError raised if ink_brand arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(ink_brand=312)
    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not int"


def test_ink_brand_attr_is_not_set_to_a_str():
    """TypeError raised if ink_brand attr is set to a value other than a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.ink_brand = 443
    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not int"


def test_ink_brand_arg_is_working_properly():
    """ink_brand arg value is properly passed to the ink_brand attr."""
    test_value = "PhotoInk"
    icc_gen = ICCGenerator(ink_brand=test_value)
    assert icc_gen.ink_brand == test_value


def test_ink_brand_attr_is_working_properly():
    """ink_brand attr is working properly."""
    test_value = "PhotoInk"
    icc_gen = ICCGenerator()
    assert icc_gen.ink_brand != test_value
    icc_gen.ink_brand = test_value
    assert icc_gen.ink_brand == test_value


def test_paper_size_arg_is_skipped():
    """default value is used if paper_size arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.paper_size == PaperSizeLibrary.A4


def test_paper_size_arg_is_none():
    """paper_size arg is set to None will use the default."""
    ig = ICCGenerator(paper_size=None)
    assert PaperSizeLibrary.A4 == ig.paper_size


def test_paper_size_attr_is_set_to_none():
    """TypeError raised if paper_size attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_size = None
    assert (
        str(cm.value) ==
        "ICCGenerator.paper_size should be a PaperSize instance, not NoneType"
    )


def test_paper_size_arg_is_not_a_paper_size_object():
    """TypeError raised if paper_size arg value is not a PaperSize instance."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(paper_size=312)
    assert (
        str(cm.value)
        == "ICCGenerator.paper_size should be a PaperSize instance, not int"
    )


def test_paper_size_attr_is_not_set_to_a_paper_size_instance():
    """TypeError raised if paper_size attr is not a PaperSize instance."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_size = 443
    assert (
        str(cm.value)
        == "ICCGenerator.paper_size should be a PaperSize instance, not int"
    )


def test_paper_size_arg_is_working_properly():
    """paper_size arg value is properly passed to the paper_size attr."""
    test_value = PaperSizeLibrary.A3
    icc_gen = ICCGenerator(paper_size=test_value)
    assert icc_gen.paper_size == test_value


def test_paper_size_attr_is_working_properly():
    """paper_size attr is working properly."""
    test_value = PaperSizeLibrary.A3
    icc_gen = ICCGenerator()
    assert icc_gen.paper_size != test_value
    icc_gen.paper_size = test_value
    assert icc_gen.paper_size == test_value


def test_number_of_pages_arg_is_skipped():
    """default value is used if number_of_pages arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.number_of_pages == 1


def test_number_of_pages_arg_is_none():
    """number_of_pages arg is set to None will raise an TypeError"""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(number_of_pages=None)
    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not NoneType"


def test_number_of_pages_attr_is_set_to_none():
    """TypeError raised if number_of_pages attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.number_of_pages = None
    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not NoneType"


def test_number_of_pages_arg_is_not_a_str():
    """TypeError raised if number_of_pages arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(number_of_pages="312")
    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not str"


def test_number_of_pages_attr_is_not_set_to_a_str():
    """TypeError raised if number_of_pages attr is set to a value other than a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.number_of_pages = "443"
    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not str"


def test_number_of_pages_arg_is_working_properly():
    """number_of_pages arg value is properly passed to the number_of_pages attr."""
    test_value = 10
    icc_gen = ICCGenerator(number_of_pages=test_value)
    assert icc_gen.number_of_pages == test_value


def test_number_of_pages_attr_is_working_properly():
    """number_of_pages attr is working properly."""
    test_value = 10
    icc_gen = ICCGenerator()
    assert icc_gen.number_of_pages != test_value
    icc_gen.number_of_pages = test_value
    assert icc_gen.number_of_pages == test_value


def test_copyright_info_arg_is_skipped():
    """default value is used if copyright_info arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.copyright_info == ""


def test_copyright_info_arg_is_none():
    """copyright_info arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(copyright_info=None)

    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not NoneType"


def test_copyright_info_attr_is_set_to_none():
    """TypeError raised if copyright_info attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.copyright_info = None
    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not NoneType"


def test_copyright_info_arg_is_not_a_str():
    """TypeError raised if copyright_info arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(copyright_info=312)
    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not int"


def test_copyright_info_attr_is_not_set_to_a_str():
    """TypeError raised if copyright_info attr is set to a value other than a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.copyright_info = 443
    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not int"


def test_copyright_info_arg_is_working_properly():
    """copyright_info arg value is properly passed to the copyright_info attr."""
    test_value = "Erkan Ozgur Yilmaz"
    icc_gen = ICCGenerator(copyright_info=test_value)
    assert icc_gen.copyright_info == test_value


def test_copyright_info_attr_is_working_properly():
    """copyright_info attr is working properly."""
    test_value = "Erkan Ozgur Yilmaz"
    icc_gen = ICCGenerator()
    assert icc_gen.copyright_info != test_value
    icc_gen.copyright_info = test_value
    assert icc_gen.copyright_info == test_value


def test_precondition_profile_path_arg_is_skipped():
    """default value is used if precondition_profile_path arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.precondition_profile_path == ""


def test_precondition_profile_path_arg_is_none():
    """precondition_profile_path arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(precondition_profile_path=None)

    assert (
        str(cm.value)
        == "ICCGenerator.precondition_profile_path should be a str, not NoneType"
    )


def test_precondition_profile_path_attr_is_set_to_none():
    """TypeError raised if precondition_profile_path attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.precondition_profile_path = None

    assert (
        str(cm.value)
        == "ICCGenerator.precondition_profile_path should be a str, not NoneType"
    )


def test_precondition_profile_path_arg_is_not_a_str():
    """TypeError raised if precondition_profile_path arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(precondition_profile_path=312)
    assert (
        str(cm.value)
        == "ICCGenerator.precondition_profile_path should be a str, not int"
    )


def test_precondition_profile_path_attr_is_not_set_to_a_str():
    """TypeError raised if precondition_profile_path attr is not a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.precondition_profile_path = 443

    assert (
        str(cm.value)
        == "ICCGenerator.precondition_profile_path should be a str, not int"
    )


def test_precondition_profile_path_arg_is_working_properly():
    """precondition_profile_path arg is passed to the precondition_profile_path attr."""
    test_value = "Epson"
    icc_gen = ICCGenerator(precondition_profile_path=test_value)
    assert icc_gen.precondition_profile_path == test_value


def test_precondition_profile_path_attr_is_working_properly():
    """precondition_profile_path attr is working properly."""
    test_value = "Epson"
    icc_gen = ICCGenerator()
    assert icc_gen.precondition_profile_path != test_value
    icc_gen.precondition_profile_path = test_value
    assert icc_gen.precondition_profile_path == test_value


def test_use_high_density_mode_arg_is_skipped():
    """default value is used if use_high_density_mode arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.use_high_density_mode is True


def test_use_high_density_mode_arg_is_none():
    """use_high_density_mode arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(use_high_density_mode=None)
    assert str(cm.value) == (
        "ICCGenerator.use_high_density_mode should be a bool (True or False), "
        "not NoneType"
    )


def test_use_high_density_mode_attr_is_set_to_none():
    """TypeError raised if the use_high_density_mode attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.use_high_density_mode = None

    assert str(cm.value) == (
        "ICCGenerator.use_high_density_mode should be a bool (True or False), "
        "not NoneType"
    )


def test_use_high_density_mode_arg_is_not_a_bool():
    """TypeError raised if the use_high_density_mode arg value is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(use_high_density_mode=312)
    assert str(cm.value) == (
        "ICCGenerator.use_high_density_mode should be a bool (True or False), not int"
    )


def test_use_high_density_mode_attr_is_not_set_to_a_str():
    """TypeError raised if the use_high_density_mode attr is not a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.use_high_density_mode = 443

    assert str(cm.value) == (
        "ICCGenerator.use_high_density_mode should be a bool (True or False), not int"
    )


def test_use_high_density_mode_arg_is_working_properly():
    """use_high_density_mode arg is passed to the use_high_density_mode attr."""
    test_value = False
    icc_gen = ICCGenerator(use_high_density_mode=test_value)
    assert icc_gen.use_high_density_mode == test_value


def test_use_high_density_mode_attr_is_working_properly():
    """use_high_density_mode attr is working properly."""
    test_value = False
    icc_gen = ICCGenerator()
    assert icc_gen.use_high_density_mode != test_value
    icc_gen.use_high_density_mode = test_value
    assert icc_gen.use_high_density_mode == test_value


def test_initializing_non_default_values():
    """class ICCGenerator initializes non default values correctly."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_name = "Canon_iX6850_Kodak_UPPP_Glossy_A4_CanonInk_%s_%s" % (
        date_str,
        time_str,
    )
    assert icc_gen.profile_name == profile_name


def test_paper_sizes():
    """default page sizes are working properly."""
    icc_gen = ICCGenerator()
    assert icc_gen.paper_size == PaperSizeLibrary.A4


def test_per_page_patch_count_is_updated_properly():
    """per_page_patch_count is updated with the paper size and use_high_density_mode."""
    icc_gen = ICCGenerator()

    # Set the paper size to A4
    icc_gen.paper_size = PaperSizeLibrary.A4
    icc_gen.use_high_density_mode = False
    assert icc_gen.per_page_patch_count == 210

    icc_gen.use_high_density_mode = True
    assert icc_gen.per_page_patch_count == 672

    # Set the paper size to A3
    icc_gen.paper_size = PaperSizeLibrary.A3
    icc_gen.use_high_density_mode = False
    assert icc_gen.per_page_patch_count == 445

    icc_gen.use_high_density_mode = True
    assert icc_gen.per_page_patch_count == 1392


def test_patch_count_is_read_only():
    """patch_count is a read only property."""
    icc_gen = ICCGenerator()
    with pytest.raises(AttributeError) as _:
        icc_gen.patch_count = 120


def test_gray_patch_count_arg_is_skipped():
    """default value is used if gray_patch_count arg is skipped."""
    icc_gen = ICCGenerator()
    assert icc_gen.gray_patch_count == 128


def test_gray_patch_count_arg_is_none():
    """gray_patch_count arg is set to None will raise an TypeError."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(gray_patch_count=None)
    assert (
        str(cm.value) == "ICCGenerator.gray_patch_count should be an int, "
        "not NoneType"
    )


def test_gray_patch_count_attr_is_set_to_none():
    """TypeError raised if gray_patch_count attr is set to None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.gray_patch_count = None
    assert str(cm.value) == (
        "ICCGenerator.gray_patch_count should be an int, not NoneType"
    )


def test_gray_patch_count_arg_is_not_an_int():
    """TypeError raised if gray_patch_count arg value is not an int."""
    with pytest.raises(TypeError) as cm:
        _ = ICCGenerator(gray_patch_count="312")
    assert str(cm.value) == "ICCGenerator.gray_patch_count should be an int, " "not str"


def test_gray_patch_count_attr_is_not_set_to_an_int():
    """TypeError raised if gray_patch_count attr is set to a value other than an int."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.gray_patch_count = "443"
    assert str(cm.value) == "ICCGenerator.gray_patch_count should be an int, " "not str"


def test_gray_patch_count_arg_is_working_properly():
    """gray_patch_count arg value is properly passed to the gray_patch_count attr."""
    test_value = 64
    icc_gen = ICCGenerator(gray_patch_count=test_value)
    assert icc_gen.gray_patch_count == test_value


def test_gray_patch_count_attr_is_working_properly():
    """gray_patch_count attr is working properly."""
    test_value = 64
    icc_gen = ICCGenerator()
    assert icc_gen.gray_patch_count != test_value
    icc_gen.gray_patch_count = test_value
    assert icc_gen.gray_patch_count == test_value


def test_gray_patch_count_is_updated_properly():
    """gray_patch_count is updated with the paper size and use_high_density_mode."""
    icc_gen = ICCGenerator()

    # Set the paper size to A4
    icc_gen.paper_size = PaperSizeLibrary.A4
    icc_gen.number_of_pages = 1
    assert icc_gen.gray_patch_count == 128

    icc_gen.number_of_pages = 2
    assert icc_gen.gray_patch_count == 128

    icc_gen.number_of_pages = 3
    assert icc_gen.gray_patch_count == 128

    icc_gen.number_of_pages = 4
    assert icc_gen.gray_patch_count == 128

    icc_gen.gray_patch_count = 25
    assert icc_gen.number_of_pages == 4
    assert icc_gen.gray_patch_count == 25


def test_gray_patch_count_is_not_read_only():
    """gray_patch_count is not a read only property."""
    icc_gen = ICCGenerator()
    icc_gen.gray_patch_count = 120
    assert icc_gen.gray_patch_count == 120


def test_patch_count_is_updating_properly():
    """patch_count is updating with page_size, page_count and use_high_density_mode."""
    icc_gen = ICCGenerator()

    # Paper Size:A4
    # Use High Density Mode: False
    icc_gen.paper_size = PaperSizeLibrary.A4
    icc_gen.use_high_density_mode = False

    # 1 Page
    icc_gen.number_of_pages = 1
    assert icc_gen.patch_count == 210

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 420

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 630

    # Use High Density Mode: True
    icc_gen.use_high_density_mode = True

    # 1 Page
    icc_gen.number_of_pages = 1
    assert icc_gen.patch_count == 672

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 1344

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 2016

    # Paper Size:A3
    # Use High Density Mode: False
    icc_gen.paper_size = PaperSizeLibrary.A3
    icc_gen.use_high_density_mode = False

    # 1 Page
    icc_gen.number_of_pages = 1
    assert icc_gen.patch_count == 445

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 890

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 1335

    # Use High Density Mode: True
    icc_gen.use_high_density_mode = True

    # 1 Page
    icc_gen.number_of_pages = 1
    assert icc_gen.patch_count == 1392

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 2784

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 4176


def test_profile_name_template_default_value():
    """profile_name_template default value is correct."""
    icc_gen = ICCGenerator()
    assert (
        icc_gen.profile_name_template
        == "{printer_brand}_{printer_model}_{paper_brand}_"
        "{paper_model}_{paper_finish}_{paper_size}_{ink_brand}_"
        "{profile_date}_{profile_time}"
    )


def test_profile_name_default_value_is_properly_calculated():
    """profile_name default value is properly calculated."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_name = "Canon_iX6850_Kodak_UPPP_Glossy_A4_CanonInk_%s_%s" % (
        date_str,
        time_str,
    )
    assert icc_gen.profile_name == profile_name


def test_profile_name_is_working_properly():
    """profile_name attr is working properly."""
    icc_gen = ICCGenerator()

    # the profile_name could be updated in any ways the user wanted
    test_value = "This is a valid profile name (but a bad one)"
    icc_gen.profile_name = test_value
    assert icc_gen.profile_name == test_value


def test_profile_path_template_default_value():
    """profile_path_template default value is correct."""
    icc_gen = ICCGenerator()

    assert (
        icc_gen._profile_path_template == "~/.cache/ICCGenerator/{printer_brand}_"
        "{printer_model}/{profile_date}"
    )


def test_profile_path_default_value_is_properly_calculated():
    """profile_path default value is properly calculated."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    assert icc_gen.profile_path == profile_path


def test_profile_path_is_read_only():
    """profile_path property is read only."""
    icc_gen = ICCGenerator()

    # the profile_path could be updated in any ways the user wanted
    with pytest.raises(AttributeError):
        icc_gen.profile_path = "some value"


def test_profile_absolute_path_is_properly_calculated():
    """profile_absolute_path is properly calculated."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    assert icc_gen.profile_absolute_path == os.path.expanduser(profile_path)


def test_profile_absolute_path_is_is_read_only():
    """profile_absolute_path is properly calculated."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    with pytest.raises(AttributeError) as cm:
        icc_gen.profile_absolute_path = os.path.expanduser(profile_path)

    assert str(cm.value) == "can't set attribute 'profile_absolute_path'"


def test_profile_absolute_full_path_is_properly_calculated():
    """profile_absolute_full_path is properly calculated."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    assert icc_gen.profile_absolute_full_path == os.path.join(
        os.path.expandvars(os.path.expanduser(profile_path)), icc_gen.profile_name
    )


def test_profile_absolute_full_path_is_is_read_only():
    """profile_absolute_full_path is properly calculated."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    with pytest.raises(AttributeError) as cm:
        icc_gen.profile_absolute_full_path = os.path.expanduser(profile_path)

    assert str(cm.value) == "can't set attribute 'profile_absolute_full_path'"


def test_generate_target_creates_the_output_folder(file_collector):
    """generate_target will create the output folder."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = PaperSizeLibrary.A4
    file_collector.append(icc_gen.profile_absolute_path)
    icc_gen.generate_target()
    assert os.path.exists(os.path.expanduser(os.path.join(icc_gen.output_path)))


def test_generate_target_generates_ti_file(file_collector):
    """generate_target will generate ti file."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = PaperSizeLibrary.A4
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    expected_path = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, ".ti1"))
    )
    assert os.path.exists(expected_path)


def test_generate_tif_files_will_generate_tif_files_from_target_file(file_collector):
    """generate_tif_files will generate tif file or files from target file."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = PaperSizeLibrary.A4
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    profile_absolute_full_path = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, ".tif"))
    )
    assert os.path.exists(profile_absolute_full_path)
    assert not os.path.exists(
        os.path.expanduser(
            os.path.join(
                icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, "_02.tif")
            )
        )
    )


def test_generate_tif_files_will_generates_correct_amount_of_tif_files(file_collector):
    """generate_tif_files correct amount of tif files."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = PaperSizeLibrary.A4
    # append the folder to the file_collector
    # so, it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    assert os.path.exists(
        os.path.expanduser(
            os.path.join(
                icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, "_01.tif")
            )
        )
    )
    assert os.path.exists(
        os.path.expanduser(
            os.path.join(
                icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, "_02.tif")
            )
        )
    )


def test_generate_tif_files_will_fill_tif_files_attr_single_page(file_collector):
    """generate_tif_files fills the tif_files correctly if there is only one page."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = PaperSizeLibrary.A4
    # append the folder to the file_collector
    # so, it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    tif1 = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, ".tif"))
    )

    assert icc_gen.tif_files[0] == tif1


def test_generate_tif_files_will_fill_tif_files_attr_more_than_one_page(file_collector):
    """generate_tif_files will fill the tif_files list correctly."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = PaperSizeLibrary.A4
    # append the folder to the file_collector
    # so, it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    tif1 = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, "_01.tif"))
    )

    tif2 = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, "_02.tif"))
    )

    assert icc_gen.tif_files[0] == tif1
    assert icc_gen.tif_files[1] == tif2


def test_generate_tif_files_will_clear_the_tif_files_list(file_collector):
    """generate_tif_files will clear the tif_files list before running."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = PaperSizeLibrary.A4
    # append the folder to the file_collector
    # so, it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    tif1 = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, "_01.tif"))
    )

    tif2 = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, "_02.tif"))
    )
    assert len(icc_gen.tif_files) == 2
    assert icc_gen.tif_files[0] == tif1
    assert icc_gen.tif_files[1] == tif2

    # change number of pages to 1
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    tif1 = os.path.expanduser(
        os.path.join(icc_gen.profile_path, "%s%s" % (icc_gen.profile_name, ".tif"))
    )

    assert len(icc_gen.tif_files) == 1
    assert icc_gen.tif_files[0] == tif1


def test_generate_tif_files_with_high_density_mode(
    file_collector, patch_run_external_process
):
    """generate_tif_files uses i1Pro if the use_high_density_mode is True."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = PaperSizeLibrary.A4
    # append the folder to the file_collector
    # so, it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()
    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert any(["-ii1" in arg for arg in final_command])


def test_generate_tif_files_with_normal_density_mode(
    file_collector, patch_run_external_process
):
    """generate_tif_files uses ColorMunki if the use_high_density_mode is False."""
    icc_gen = ICCGenerator()
    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = PaperSizeLibrary.A4
    icc_gen.use_high_density_mode = False
    # append the folder to the file_collector
    # so, it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()
    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert any(["-iCM" in arg for arg in final_command])


def test_print_charts(file_collector, patch_run_external_process):
    """print_charts is working properly."""
    # patch the run_external_process and check the command
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    system_name = platform.system().lower()
    if "linux" in system_name:
        assert "gimp" in final_command[0]
    elif "darwin" in system_name:
        assert "/Applications/Print-Tool.app/Contents/MacOS/Print-Tool"


def test_read_charts_calls_chartread_command(
    file_collector, patch_run_external_process
):
    """read_charts method will call chartread."""
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts()

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert "chartread" in final_command[0]


def test_read_charts_with_resume_set_to_true(
    file_collector, patch_run_external_process
):
    """read_charts method with resume=True will call chartread with -r option."""
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts(resume=True)

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert "chartread" in final_command[0]
    assert any(["-r" in arg for arg in final_command])


def test_read_charts_with_read_mode_set_to_1(
    file_collector, patch_run_external_process
):
    """read_charts with read_mode=1 calls chartread with -p and -P options."""
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts(read_mode=1)

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert "chartread" in final_command[0]
    assert any(["-p" in arg for arg in final_command])
    assert any(["-P" in arg for arg in final_command])


def test_generate_profile_1(file_collector, patch_run_external_process):
    """generate_profile method is working properly."""
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts()
    icc_gen.generate_profile()

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert "colprof" in final_command[0]

    assert any(["-v" in arg for arg in final_command])
    assert any(["-qh" in arg for arg in final_command])
    assert any(["-r0.5" in arg for arg in final_command])
    assert any(["-S" in arg for arg in final_command])
    assert any(["-cmt" in arg for arg in final_command])
    assert any(["-dpp" in arg for arg in final_command])
    assert any(["-D" in arg for arg in final_command])


def test_generate_profile_2(file_collector, patch_run_external_process):
    """generate_profile method is working properly."""
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    icc_gen.copyright_info = "Erkan Ozgur Yilmaz(c)2021"
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts()
    icc_gen.generate_profile()

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert "colprof" in final_command[0]
    assert any(["-CErkan Ozgur Yilmaz(c)2021" in arg for arg in final_command])


def test_check_profile(file_collector, patch_run_external_process):
    """check_profile method is working properly."""
    icc_gen = ICCGenerator()
    file_collector.append(icc_gen.profile_path)
    icc_gen.number_of_pages = 1
    icc_gen.copyright_info = "Erkan Ozgur Yilmaz(c)2021"
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts()
    icc_gen.generate_profile()
    icc_gen.check_profile()

    final_command = patch_run_external_process[-1]
    assert "profcheck" in final_command[0]
    assert any(["-k" in arg for arg in final_command])
    assert any(["-v2" in arg for arg in final_command])
    assert not any(["-s" in arg for arg in final_command])


def test_check_profile_with_sort(file_collector, patch_run_external_process):
    """check_profile method is working properly."""
    icc_gen = ICCGenerator()
    file_collector.append(icc_gen.profile_path)
    icc_gen.number_of_pages = 1
    icc_gen.copyright_info = "Erkan Ozgur Yilmaz(c)2021"
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts()
    icc_gen.generate_profile()
    icc_gen.check_profile(sort_by_de=True)

    final_command = patch_run_external_process[-1]
    assert "profcheck" in final_command[0]
    assert any(["-k" in arg for arg in final_command])
    assert any(["-v2" in arg for arg in final_command])
    assert any(["-s" in arg for arg in final_command])


def test_check_profile_with_correct_file_extension(
    file_collector, patch_run_external_process
):
    """check_profile uses the correct profile file extension"""
    # ICM on Windows and ICC on Linux
    icc_gen = ICCGenerator()
    file_collector.append(icc_gen.profile_path)
    icc_gen.number_of_pages = 1
    icc_gen.copyright_info = "Erkan Ozgur Yilmaz(c)2021"
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts()
    icc_gen.generate_profile()
    icc_gen.check_profile(sort_by_de=True)

    final_command = patch_run_external_process[-1]
    assert "profcheck" in final_command[0]

    if os.name == "nt":
        assert any([".icm" in arg for arg in final_command])
        assert not any([".icc" in arg for arg in final_command])
    else:
        assert not any([".icm" in arg for arg in final_command])
        assert any([".icc" in arg for arg in final_command])


def test_install_profile_1(file_collector, patch_run_external_process):
    """install_profile method is working properly."""
    icc_gen = ICCGenerator()
    file_collector.append(icc_gen.profile_path)
    icc_gen.number_of_pages = 1
    icc_gen.copyright_info = "Erkan Ozgur Yilmaz(c)2021"
    file_collector.append(icc_gen.profile_path)

    # create a dummy icc file
    dummy_icc_profile_full_path = os.path.expandvars(
        os.path.expanduser(
            os.path.join(icc_gen.profile_path, "%s.icc" % icc_gen.profile_name)
        )
    )
    os.makedirs(
        os.path.expandvars(os.path.expanduser(icc_gen.profile_path)), exist_ok=True
    )
    assert os.path.expandvars(os.path.expanduser(icc_gen.profile_path))
    with open(dummy_icc_profile_full_path, "w+") as f:
        f.write("dummy icc file!!!")
    assert os.path.exists(dummy_icc_profile_full_path)
    file_collector.append(dummy_icc_profile_full_path)

    icc_gen.install_profile()

    # this is easy
    # just check if ICC file is copied to the correct folder
    profile_install_path = None
    system_name = platform.system().lower()
    if "win32" in system_name:
        profile_install_path = os.path.expandvars(
            "$WINDIR/System32spool/drivers/color/%s.icc" % icc_gen.profile_name
        )
    elif "linux" in system_name:
        profile_install_path = os.path.expandvars(
            os.path.expanduser("~/.local/share/icc/%s.icc" % icc_gen.profile_name)
        )
    elif "darwin" in system_name :
        profile_install_path = os.path.expandvars(
            os.path.expanduser("~/Library/ColorSync/Profiles/{}.icc".format(
                icc_gen.profile_name
            ))
        )

    assert profile_install_path is not None
    file_collector.append(profile_install_path)
    assert os.path.exists(os.path.expandvars(profile_install_path))


def test_install_profile_2(file_collector, patch_run_external_process):
    """install_profile will raise a RuntimeError if ICC has not been generated yet."""
    icc_gen = ICCGenerator()
    file_collector.append(icc_gen.profile_path)
    icc_gen.number_of_pages = 1
    icc_gen.copyright_info = "Erkan Ozgur Yilmaz(c)2021"
    file_collector.append(icc_gen.profile_path)
    with pytest.raises(RuntimeError) as cm:
        icc_gen.install_profile()
    assert str(cm.value) == "ICC file doesn't exist, please generate it first!"


def test_default_logger_is_created(file_collector):
    """default logger has been created."""
    assert isinstance(logger, logging.Logger)


def test_default_log_level_is_warning(file_collector):
    """default log level is warning."""
    assert logger.level == logging.WARNING


def test_output_path_for_windows(set_to_windows):
    """output_path variable is correctly set for Windows."""
    icc_gen = ICCGenerator()
    assert icc_gen.output_path == "%WINDIR%/System32/spool/drivers/color/"


def test_output_path_for_linux(set_to_linux):
    """output_path variable is correctly set for Linux."""
    icc_gen = ICCGenerator()
    assert icc_gen.output_path == "~/.local/share/icc/"


def test_output_path_for_macos(set_to_macos):
    """output_path variable is correctly set for macOS."""
    icc_gen = ICCGenerator()
    assert icc_gen.output_path == "~/Library/ColorSync/Profiles/"


def test_color_correct_image_printer_profile_path_is_skipped(
    file_collector, patch_run_external_process
):
    """color_correct_image raises ValueError if printer_profile_path arg is skipped."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert str(cm.value) == "Please specify a proper printer_profile_path!"


def test_color_correct_image_printer_profile_path_is_none(
    file_collector, patch_run_external_process
):
    """color_correct_image raises TypeError if printer_profile_path arg is None."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=None,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert str(cm.value) == "Please specify a proper printer_profile_path!"


def test_color_correct_image_printer_profile_path_doesnt_exist(
    file_collector, patch_run_external_process
):
    """color_correct_image raises ValueError if printer_profile_path doesn't exist."""
    printer_profile_path = tempfile.mktemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(ValueError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert (
        str(cm.value)
        == "printer_profile_path doesn't exists: %s" % printer_profile_path
    )


def test_color_correct_image_printer_profile_path_is_not_an_icc_or_icm_file(
    file_collector, patch_run_external_process
):
    """ValueError raised if printer_profile_path arg is not path to an ICC or ICM."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(
        suffix=".not_an_icc_file"
    )
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(ValueError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert (
        str(cm.value)
        == "printer_profile_path should be a valid ICC/ICM file: %s"
        % printer_profile_path
    )


def test_color_correct_image_input_image_path_is_skipped(
    file_collector, patch_run_external_process
):
    """color_correct_image raises ValueError if input_image_path arg is skipped."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )
    assert str(cm.value) == "Please specify a proper input_image_path!"


def test_color_correct_image_input_image_is_none(
    file_collector, patch_run_external_process
):
    """color_correct_image raises TypeError if input_image arg is None."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=None,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert str(cm.value) == "Please specify a proper input_image_path!"


def test_color_correct_image_input_image_doesnt_exist(
    file_collector, patch_run_external_process
):
    """color_correct_image raises ValueError if input_image arg value doesn't exist."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path = tempfile.mktemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(ValueError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert str(cm.value) == "input_image_path doesn't exists: %s" % input_image_path


def test_color_correct_image_input_image_path_is_not_an_jpg_or_tif_file(
    file_collector, patch_run_external_process
):
    """TypeError raised if input_image_path is not a path of a JPG or TIF file."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".bmp")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(ValueError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert (
        str(cm.value)
        == "input_image_path should be a valid JPG/TIF file: %s" % input_image_path
    )


def test_color_correct_image_output_image_path_is_skipped(
    file_collector, patch_run_external_process_class_method_version
):
    """proper output_image_path generated if output_image_path arg is skipped."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    _output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        image_profile=image_profile,
        intent=intent,
    )

    input_image_name, input_image_ext = os.path.splitext(input_image_path)
    expected_path = "%s_corrected_1%s" % (input_image_name, input_image_ext)
    assert any(
        expected_path in arg
        for arg in patch_run_external_process_class_method_version[0]
    )


def test_color_correct_image_output_image_path_is_none(
    file_collector, patch_run_external_process_class_method_version
):
    """proper output_image_path generated if output_image_path arg is None."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    _output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        image_profile=image_profile,
        intent=intent,
    )

    input_image_name, input_image_ext = os.path.splitext(input_image_path)
    expected_path = "%s_corrected_1%s" % (input_image_name, input_image_ext)
    assert any(
        expected_path in arg
        for arg in patch_run_external_process_class_method_version[0]
    )


def test_color_correct_image_output_image_path_is_not_a_tif_file(file_collector):
    """ValueError raised if output_image_path is not a tif file path."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".bmp")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    with pytest.raises(ValueError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert (
        str(cm.value)
        == "output_image_path should be a valid JPG/TIF file: %s" % output_image_path
    )


def test_color_correct_image_intent_is_skipped(
    file_collector, patch_run_external_process_class_method_version
):
    """default value used if intent arg is skipped."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    _intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
    )

    assert "-i" in patch_run_external_process_class_method_version[0]
    assert "r" in patch_run_external_process_class_method_version[0]


def test_color_correct_image_intent_is_none(
    file_collector, patch_run_external_process_class_method_version
):
    """default value used if intent arg is None."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    _intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
        intent=None,
    )

    assert "-i" in patch_run_external_process_class_method_version[0]
    assert "r" in patch_run_external_process_class_method_version[0]


def test_color_correct_image_intent_is_not_a_str(file_collector):
    """TypeError raised if intent arg is not a str."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = 123

    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert str(cm.value) == "intent should be a str, not int"


def test_color_correct_image_intent_is_not_correct_enum_value(file_collector):
    """TypeError raised if intent arg is not one of p, r, s, a."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "not one of the desired values"

    with pytest.raises(ValueError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert str(cm.value) == "intent should be one of p, r, s, a, not %s" % intent


def test_color_correct_image_intent_is_working_properly(
    file_collector, patch_run_external_process_class_method_version
):
    """default value used if intent arg is None."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
        intent=intent,
    )

    assert "-i" in patch_run_external_process_class_method_version[0]
    assert "r" in patch_run_external_process_class_method_version[0]


def test_color_correct_image_profile_is_none(
    file_collector, patch_run_external_process_class_method_version
):
    """default value used if image_profile arg is None."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    _image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=None,
        intent=intent,
    )

    assert "-p" in patch_run_external_process_class_method_version[0]
    assert any(
        [
            "AdobeRGB" in arg
            for arg in patch_run_external_process_class_method_version[0]
        ]
    )


def test_color_correct_image_image_profile_is_not_a_str(file_collector):
    """TypeError raised if image_profile arg is not a str."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = 123123
    intent = "r"

    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert (
        str(cm.value) == "image_profile should be one of sRGB or AdobeRGB, not 123123"
    )


def test_color_correct_image_image_profile_is_not_correct_enum_value(file_collector):
    """TypeError raised if image_profile arg is not one of AdobeRGB or sRGB."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "not one of the desired values"
    intent = "r"

    with pytest.raises(ValueError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent,
        )

    assert (
        str(cm.value)
        == "image_profile should be one of sRGB or AdobeRGB, not %s" % image_profile
    )


def test_color_correct_image_image_profile_is_working_properly(
    file_collector, patch_run_external_process_class_method_version
):
    """TypeError raised if image_profile arg is working properly."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "sRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
        intent=intent,
    )

    assert any(
        "-p" in arg for arg in patch_run_external_process_class_method_version[0]
    )
    assert any(
        "sRGB" in arg for arg in patch_run_external_process_class_method_version[0]
    )


def test_color_correct_image_image_profile_is_a_path_to_srgb_or_adobergb_file(
    file_collector, patch_run_external_process_class_method_version
):
    """image_profile can be a path to sRGB or AdobeRGB file."""
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix=".icc")
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix=".tif")
    output_image_path = tempfile.mktemp(suffix=".tif")
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)

    image_profile = os.path.normpath(os.path.join(HERE, "..", "sRGB.icc"))
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
        intent=intent,
    )

    assert any(
        "-p" in arg for arg in patch_run_external_process_class_method_version[0]
    )
    assert any(
        "sRGB" in arg for arg in patch_run_external_process_class_method_version[0]
    )
    assert any(
        image_profile in arg
        for arg in patch_run_external_process_class_method_version[0]
    )


def test_save_settings_path_is_skipped(file_collector):
    """profile_path used if path arg value is skipped."""
    icc_gen = ICCGenerator()
    settings_file_path = os.path.join(
        icc_gen.profile_path, "%s.json" % icc_gen.profile_name
    )

    file_collector.append(settings_file_path)

    assert not os.path.exists(os.path.expanduser(settings_file_path))
    icc_gen.save_settings()
    assert os.path.exists(os.path.expanduser(settings_file_path))


def test_save_settings_path_is_none(file_collector):
    """profile_path used if path arg value is None."""
    icc_gen = ICCGenerator()
    settings_file_path = os.path.join(
        icc_gen.profile_path, "%s.json" % icc_gen.profile_name
    )

    file_collector.append(settings_file_path)

    assert not os.path.exists(os.path.expanduser(settings_file_path))
    icc_gen.save_settings(path=None)
    assert os.path.exists(os.path.expanduser(settings_file_path))


def test_save_settings_path_is_not_a_str():
    """TypeError raised if path arg value is not a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.save_settings(1)

    assert str(cm.value) == "Please specify a valid path"


def test_save_settings_is_working_properly(file_collector, patch_run_external_process):
    """save_settings function is working properly."""
    icc_gen = ICCGenerator()
    path = tempfile.mktemp()
    file_collector.append(path)
    icc_gen.save_settings(path)

    assert os.path.exists(path)

    # check file content
    with open(path, "r") as f:
        data = json.load(f)

    assert data is not None
    icc_gen.ink_brand = data["ink_brand"]
    icc_gen.paper_brand = data["paper_brand"]
    icc_gen.paper_finish = data["paper_finish"]
    icc_gen.paper_model = data["paper_model"]
    icc_gen.paper_size.name = data["paper_size"]
    icc_gen.printer_brand = data["printer_brand"]
    icc_gen.printer_model = data["printer_model"]
    icc_gen.profile_date = data["profile_date"]
    icc_gen.profile_time = data["profile_time"]


def test_load_settings_path_is_skipped():
    """RuntimeError raised if path arg is skipped."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.load_settings()

    assert (
        str(cm.value) == "ICCGenerator.load_settings() missing 1 required "
        "positional argument: 'path'"
    )


def test_load_settings_path_is_none():
    """RuntimeError raised if path arg value is None."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.load_settings(None)

    assert str(cm.value) == "Please specify a valid path"


def test_load_settings_path_is_not_a_str():
    """TypeError raised if path arg value is not a str."""
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.load_settings(123)

    assert str(cm.value) == "Please specify a valid path"


def test_load_settings_path_does_not_exist():
    """RuntimeError raised if path doesn't exist."""
    icc_gen = ICCGenerator()
    with pytest.raises(RuntimeError) as cm:
        icc_gen.load_settings("Some random error")

    assert str(cm.value) == "File does not exist!: Some random error"


def test_load_settings_is_working_properly(file_collector):
    """load_settings function is working properly."""
    icc_gen = ICCGenerator()

    # set some values
    icc_gen.ink_brand = "Epson673"
    icc_gen.paper_brand = "Agfa"
    icc_gen.paper_finish = "Glossy"
    icc_gen.paper_model = "HGPIP"
    icc_gen.paper_size = PaperSizeLibrary.A4
    icc_gen.printer_brand = "Epson"
    icc_gen.printer_model = "L800"

    path = tempfile.mktemp()
    file_collector.append(path)
    icc_gen.save_settings(path)

    assert os.path.exists(path)

    # check file content
    icc_gen2 = ICCGenerator()
    icc_gen2.load_settings(path)

    icc_gen.ink_brand = icc_gen2.ink_brand
    icc_gen.paper_brand = icc_gen2.paper_brand
    icc_gen.paper_finish = icc_gen2.paper_finish
    icc_gen.paper_model = icc_gen2.paper_model
    icc_gen.paper_size = icc_gen2.paper_size
    icc_gen.printer_brand = icc_gen2.printer_brand
    icc_gen.printer_model = icc_gen2.printer_model
    icc_gen.profile_date = icc_gen2.profile_date
    icc_gen.profile_time = icc_gen2.profile_time
