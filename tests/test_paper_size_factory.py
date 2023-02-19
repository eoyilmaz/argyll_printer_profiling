# -*- coding: utf-8 -*-
"""Tests for the PaperSizeFactory class."""

import pytest

from icc_generator.api import PaperSizeFactory, PaperSize


def test_paper_size_factory_ment_to_be_used_as_a_storage():
    """Instantiating PaperSizeFactory raise RuntimeError."""
    with pytest.raises(RuntimeError) as cm:
        PaperSizeFactory()

    assert (
        str(cm.value) ==
        "PaperSizeFactory is meant to be used as a storage class. "
        "Do not instantiate it."
    )


def test_paper_size_factory_data():
    """PaperSizeFactory contains predefined PaperSizes."""
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
        assert paper_name in PaperSizeFactory.paper_sizes
        assert paper_size == PaperSizeFactory.paper_sizes[paper_name]
