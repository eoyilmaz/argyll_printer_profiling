# -*- coding: utf-8 -*-
"""Tests for the PaperSizeLibrary class."""

import pytest

from icc_generator.api import PaperSizeLibrary, PaperSize


def test_paper_size_library_ment_to_be_used_as_a_storage():
    """Instantiating PaperSizeLibrary raise RuntimeError."""
    with pytest.raises(RuntimeError) as cm:
        PaperSizeLibrary()

    assert (
        str(cm.value) ==
        "PaperSizeLibrary is meant to be used as a storage class. "
        "Do not instantiate it."
    )


def test_paper_size_library_data():
    """PaperSizeLibrary contains predefined PaperSizes."""
    paper_sizes = {
        "4x6": PaperSize(name="4x6", width=101.6, height=152.4),
        "11x17": PaperSize(name="11x17", width=279.4, height=431.8),
        "A2": PaperSize(name="A2", width=420.0, height=594),
        "A3": PaperSize(name="A3", width=297.0, height=420.0),
        "A4": PaperSize(name="A4", width=210.0, height=297.0),
        "A4R": PaperSize(name="A4R", width=297.0, height=210.0),
        "Legal": PaperSize(name="Legal", width=215.9, height=355.6),
        "Letter": PaperSize(name="Letter", width=215.9, height=279.4),
        "LetterR": PaperSize(name="LetterR", width=279.4, height=215.9),
    }
    for paper_name in paper_sizes:
        paper_size = paper_sizes[paper_name]
        assert paper_name in PaperSizeLibrary.paper_sizes
        assert paper_size == PaperSizeLibrary.paper_sizes[paper_name]


def test_paper_size_library_paper_names():
    """PaperSizeLibrary contains predefined PaperSize names."""
    assert PaperSizeLibrary.p4x6 == PaperSizeLibrary.paper_sizes["4x6"]
    assert PaperSizeLibrary.p11x17 == PaperSizeLibrary.paper_sizes["11x17"]
    assert PaperSizeLibrary.A2 == PaperSizeLibrary.paper_sizes["A2"]
    assert PaperSizeLibrary.A3 == PaperSizeLibrary.paper_sizes["A3"]
    assert PaperSizeLibrary.A4 == PaperSizeLibrary.paper_sizes["A4"]
    assert PaperSizeLibrary.A4R == PaperSizeLibrary.paper_sizes["A4R"]
    assert PaperSizeLibrary.Legal == PaperSizeLibrary.paper_sizes["Legal"]
    assert PaperSizeLibrary.Letter == PaperSizeLibrary.paper_sizes["Letter"]
    assert PaperSizeLibrary.LetterR == PaperSizeLibrary.paper_sizes["LetterR"]


@pytest.mark.parametrize(
    "paper_size_name,expected_value", [
        ["4x6", PaperSizeLibrary.paper_sizes["4x6"]],
        ["11x17", PaperSizeLibrary.paper_sizes["11x17"]],
        ["A2", PaperSizeLibrary.paper_sizes["A2"]],
        ["A3", PaperSizeLibrary.paper_sizes["A3"]],
        ["A4", PaperSizeLibrary.paper_sizes["A4"]],
        ["A4R", PaperSizeLibrary.paper_sizes["A4R"]],
        ["Legal", PaperSizeLibrary.paper_sizes["Legal"]],
        ["Letter", PaperSizeLibrary.paper_sizes["Letter"]],
        ["LetterR", PaperSizeLibrary.paper_sizes["LetterR"]],
    ]
)
def test_get_paper_size_is_working_okay(paper_size_name, expected_value):
    """PaperSizeLibrary.get_paper_size() returns PaperSize with name."""
    assert expected_value == PaperSizeLibrary.get_paper_size(paper_size_name)
