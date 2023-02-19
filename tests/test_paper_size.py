# -*- coding: utf-8 -*-
"""Tests for the PaperSize class."""

import pytest

from icc_generator.api import PaperSize


def test_paper_size_class_initialization():
    """PaperSize class init okay."""
    paper_size = PaperSize(name="A4", width=210, height=297)
    assert isinstance(paper_size, PaperSize)


def test_name_arg_is_skipped():
    """TypeError raised if name arg is skipped."""
    with pytest.raises(TypeError) as cm:
        _ = PaperSize(width=210, height=297)
    assert (
        str(cm.value)
        == "PaperSize.__init__() missing 1 required positional argument: 'name'"
    )


def test_name_arg_is_not_a_str():
    """TypeError raised if name arg is not a str."""
    with pytest.raises(TypeError) as cm:
        _ = PaperSize(name=123, width=210, height=297)
    assert str(cm.value) == "PaperSize.name should be a str, not int"


def test_name_attr_is_not_a_str():
    """TypeError raised if name attr is not a str."""
    a4 = PaperSize(name="a4", width=210, height=297)
    with pytest.raises(TypeError) as cm:
        a4.name = 123
    assert str(cm.value) == "PaperSize.name should be a str, not int"


def test_width_arg_is_skipped():
    """TypeError raised if width arg is skipped."""
    with pytest.raises(TypeError) as cm:
        _ = PaperSize(name="A4", height=297)
    assert (
        str(cm.value)
        == "PaperSize.__init__() missing 1 required positional argument: 'width'"
    )


def test_width_arg_is_not_a_int_or_float():
    """TypeError raised if width arg is not an int or float."""
    with pytest.raises(TypeError) as cm:
        _ = PaperSize(name="A4", width="210", height=297)
    assert str(cm.value) == "PaperSize.width should be a int or float, not str"


def test_width_attr_is_not_a_int_or_float():
    """TypeError raised if width attr is not an int or float."""
    a4 = PaperSize(name="A4", width=210, height=297)
    with pytest.raises(TypeError) as cm:
        a4.width = "210"
    assert str(cm.value) == "PaperSize.width should be a int or float, not str"


@pytest.mark.parametrize("width", [0, -1, -212.3, -0.000001])
def test_width_arg_is_not_positive(width):
    """ValueError raised if width arg is not a positive value."""
    with pytest.raises(ValueError) as cm:
        _ = PaperSize(name="A4", width=width, height=297)
    assert str(cm.value) == "PaperSize.width should be a positive value, not {}".format(
        width
    )


@pytest.mark.parametrize("width", [0, -1, -212.3, -0.000001])
def test_width_attr_is_not_positive(width):
    """TypeError raised if width attr is not a positive value."""
    a4 = PaperSize(name="A4", width=210, height=297)
    with pytest.raises(ValueError) as cm:
        a4.width = width
    assert str(cm.value) == "PaperSize.width should be a positive value, not {}".format(
        width
    )


def test_height_arg_is_skipped():
    """TypeError raised if height arg is skipped."""
    with pytest.raises(TypeError) as cm:
        _ = PaperSize(name="A4", width=210)
    assert (
        str(cm.value)
        == "PaperSize.__init__() missing 1 required positional argument: 'height'"
    )


def test_height_arg_is_not_a_int_or_float():
    """TypeError raised if height arg is not an int or float."""
    with pytest.raises(TypeError) as cm:
        _ = PaperSize(name="A4", width=210, height="297")
    assert str(cm.value) == "PaperSize.height should be a int or float, not str"


def test_height_attr_is_not_a_int_or_float():
    """TypeError raised if height attr is not an int or float."""
    a4 = PaperSize(name="A4", width=210, height=297)
    with pytest.raises(TypeError) as cm:
        a4.height = "297"
    assert str(cm.value) == "PaperSize.height should be a int or float, not str"


@pytest.mark.parametrize("height", [0, -1, -212.3, -0.000001])
def test_height_arg_is_not_positive(height):
    """ValueError raised if height arg is not a positive value."""
    with pytest.raises(ValueError) as cm:
        _ = PaperSize(name="A4", width=210, height=height)
    assert str(
        cm.value
    ) == "PaperSize.height should be a positive value, not {}".format(height)


@pytest.mark.parametrize("height", [0, -1, -212.3, -0.000001])
def test_height_attr_is_not_positive(height):
    """TypeError raised if height attr is not a positive value."""
    a4 = PaperSize(name="A4", width=210, height=297)
    with pytest.raises(ValueError) as cm:
        a4.height = height
    assert str(
        cm.value
    ) == "PaperSize.height should be a positive value, not {}".format(height)


@pytest.mark.parametrize(
    "name,width,height,expected_value",
    [
        ["A4", 210, 297, (210, 297)],
        ["A3", 297, 420, (297, 420)],
        ["A2", 420, 594, (420, 594)],
    ],
)
def test_size_returns_width_and_height_as_list(name, width, height, expected_value):
    """size property returns [width, height]."""
    paper_size = PaperSize(name=name, width=width, height=height)
    assert expected_value == paper_size.size


@pytest.mark.parametrize(
    "width,height,size_value",
    [
        [210, 297, [210, 297]],
        [297, 420, [297, 420]],
        [420, 594, [420, 594]],
    ],
)
def test_size_accepts_a_list_of_ints(width, height, size_value):
    """size property accepts a list of ints."""
    paper_size = PaperSize(name="init", width=1, height=1)
    paper_size.size = size_value
    assert width == paper_size.width
    assert height == paper_size.height


@pytest.mark.parametrize(
    "width,height,size_value",
    [
        [210.0, 297.0, [210.0, 297.0]],
        [297.0, 420.0, [297.0, 420.0]],
        [420.0, 594.0, [420.0, 594.0]],
        [215.9, 355.6, [215.9, 355.6]],
    ],
)
def test_size_accepts_a_list_of_floats(width, height, size_value):
    """size property accepts a list of floats."""
    paper_size = PaperSize(name="init", width=1, height=1)
    paper_size.size = size_value
    assert width == paper_size.width
    assert height == paper_size.height


@pytest.mark.parametrize("test_value", [[1, 2, 3], [1.23, 2.34, 5.32, 3.343]])
def test_size_accepts_length_of_2(test_value):
    """size property accepts a list of length 2."""
    paper_size = PaperSize(name="Legal", width=215.9, height=355.6)
    with pytest.raises(ValueError) as cm:
        paper_size.size = test_value
    assert str(
        cm.value
    ) == "PaperSize.size should be a list or tuple of 2 items, not {}".format(
        len(test_value)
    )


@pytest.mark.parametrize(
    "width,height,size_value",
    [
        [210, 297, [210.0, 297]],
        [297, 420, [297, 420.0]],
        [420, 594, [420, 594.0]],
        [216, 355.6, [216, 355.6]],
    ],
)
def test_size_accepts_mixed_data_of_int_and_float(width, height, size_value):
    """size property accepts mixed type of int and float"""
    paper_size = PaperSize(name="init", width=1, height=1)
    paper_size.size = size_value
    assert width == paper_size.width
    assert height == paper_size.height


@pytest.mark.parametrize(
    "test_value",
    [
        ["210", 297],
        ["210", "297"],
        [None, 2.34],
        [2.34, None],
        [None, None],
    ],
)
def test_size_only_accepts_int_or_float(test_value):
    """setting size with a list of non int or float raises TypeError."""
    paper_size = PaperSize(name="Legal", width=215.9, height=355.6)
    with pytest.raises(TypeError):
        paper_size.size = test_value


def test_area_is_read_only():
    """area is a read-only property."""
    paper_size = PaperSize(name="Legal", width=215.9, height=355.6)
    with pytest.raises(AttributeError):
        paper_size.area = 23


@pytest.mark.parametrize(
    "name,width,height,expected_result",
    [
        ["A2", 420.0, 594.0, 249480.0],
        ["A3", 297.0, 420.0, 124740.0],
        ["A4", 210.0, 297.0, 62370.0],
        ["A4R", 297.0, 210.0, 62370.0],
        ["Legal", 215.9, 355.6, 76774.04],
        ["Letter", 215.9, 279.4, 60322.46],
        ["LetterR", 279.4, 215.9, 60322.46],
    ]
)
def test_area_returns_paper_area_in_mm2(name, width, height, expected_result):
    """area returns paper area in mm2."""
    paper_size = PaperSize(name=name, width=width, height=height)
    assert expected_result == pytest.approx(paper_size.area, 0.001)


@pytest.mark.parametrize(
    "name,width,height",
    [
        ["A2", 420.0, 594.0],
        ["A3", 297.0, 420.0],
        ["A4", 210.0, 297.0],
        ["A4R", 297.0, 210.0],
        ["Legal", 215.9, 355.6],
        ["Letter", 215.9, 279.4],
        ["LetterR", 279.4, 215.9],
    ]
)
def test_equality_op(name, width, height):
    """Test equality operator."""
    paper_size1 = PaperSize(name=name, width=width, height=height)
    paper_size2 = PaperSize(name=name, width=width, height=height)
    assert paper_size1 == paper_size2
