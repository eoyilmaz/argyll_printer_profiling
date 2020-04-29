# -*- coding: utf-8 -*-


def test_initializing_without_any_arguments():
    """testing if the class ICCGenerator initializes correctly
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # check default values
    assert icc_gen.printer_brand == "Canon"
    assert icc_gen.printer_model == "iX6850"
    assert icc_gen.paper_brand == "Kodak"
    assert icc_gen.paper_model == "UPPP"
    assert icc_gen.paper_finish == "Glossy"
    assert icc_gen.paper_size == "A4"
    assert icc_gen.ink_brand == "CanonInk"
    assert icc_gen.use_high_density_mode is True
    assert icc_gen.number_of_pages == 1
    assert icc_gen.copyright_info == ""


def test_printer_brand_argument_is_skipped():
    """testing if the default value is used when the printer_brand argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.printer_brand == 'Canon'


def test_printer_brand_argument_is_none():
    """testing if printer_brand argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(printer_brand=None)

    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not NoneType"


def test_printer_brand_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the printer_brand
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_brand = None

    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not NoneType"


def test_printer_brand_argument_is_not_a_string():
    """testing if a TypeError will be raised if the printer_brand argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(printer_brand=312)

    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not int"


def test_printer_brand_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the printer_brand attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_brand = 443

    assert str(cm.value) == "ICCGenerator.printer_brand should be a str, not int"


def test_printer_brand_argument_is_working_properly():
    """testing if the printer_brand argument value is properly passed to the
    printer_brand attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'Epson'
    icc_gen = ICCGenerator(printer_brand=test_value)
    assert icc_gen.printer_brand == test_value


def test_printer_brand_attribute_is_working_properly():
    """testing if the printer_brand attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'Epson'
    icc_gen = ICCGenerator()
    assert icc_gen.printer_brand != test_value
    icc_gen.printer_brand = test_value
    assert icc_gen.printer_brand == test_value


def test_printer_model_argument_is_skipped():
    """testing if the default value is used when the printer_model argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.printer_model == 'iX6850'


def test_printer_model_argument_is_none():
    """testing if printer_model argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(printer_model=None)

    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not NoneType"


def test_printer_model_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the printer_model
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_model = None

    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not NoneType"


def test_printer_model_argument_is_not_a_string():
    """testing if a TypeError will be raised if the printer_model argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(printer_model=312)

    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not int"


def test_printer_model_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the printer_model attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.printer_model = 443

    assert str(cm.value) == "ICCGenerator.printer_model should be a str, not int"


def test_printer_model_argument_is_working_properly():
    """testing if the printer_model argument value is properly passed to the
    printer_model attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'iP7250'
    icc_gen = ICCGenerator(printer_model=test_value)
    assert icc_gen.printer_model == test_value


def test_printer_model_attribute_is_working_properly():
    """testing if the printer_model attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'iP7250'
    icc_gen = ICCGenerator()
    assert icc_gen.printer_model != test_value
    icc_gen.printer_model = test_value
    assert icc_gen.printer_model == test_value


def test_paper_brand_argument_is_skipped():
    """testing if the default value is used when the paper_brand argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.paper_brand == 'Kodak'


def test_paper_brand_argument_is_none():
    """testing if paper_brand argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_brand=None)

    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not NoneType"


def test_paper_brand_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the paper_brand
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_brand = None

    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not NoneType"


def test_paper_brand_argument_is_not_a_string():
    """testing if a TypeError will be raised if the paper_brand argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_brand=312)

    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not int"


def test_paper_brand_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the paper_brand attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_brand = 443

    assert str(cm.value) == "ICCGenerator.paper_brand should be a str, not int"


def test_paper_brand_argument_is_working_properly():
    """testing if the paper_brand argument value is properly passed to the
    paper_brand attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'Hahnemuhle'
    icc_gen = ICCGenerator(paper_brand=test_value)
    assert icc_gen.paper_brand == test_value


def test_paper_brand_attribute_is_working_properly():
    """testing if the paper_brand attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'Hahnemuhle'
    icc_gen = ICCGenerator()
    assert icc_gen.paper_brand != test_value
    icc_gen.paper_brand = test_value
    assert icc_gen.paper_brand == test_value


def test_paper_model_argument_is_skipped():
    """testing if the default value is used when the paper_model argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.paper_model == 'UPPP'


def test_paper_model_argument_is_none():
    """testing if paper_model argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_model=None)

    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not NoneType"


def test_paper_model_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the paper_model
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_model = None

    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not NoneType"


def test_paper_model_argument_is_not_a_string():
    """testing if a TypeError will be raised if the paper_model argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_model=312)

    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not int"


def test_paper_model_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the paper_model attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_model = 443

    assert str(cm.value) == "ICCGenerator.paper_model should be a str, not int"


def test_paper_model_argument_is_working_properly():
    """testing if the paper_model argument value is properly passed to the
    paper_model attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'FineArt'
    icc_gen = ICCGenerator(paper_model=test_value)
    assert icc_gen.paper_model == test_value


def test_paper_model_attribute_is_working_properly():
    """testing if the paper_model attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'FineArt'
    icc_gen = ICCGenerator()
    assert icc_gen.paper_model != test_value
    icc_gen.paper_model = test_value
    assert icc_gen.paper_model == test_value


def test_paper_finish_argument_is_skipped():
    """testing if the default value is used when the paper_finish argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.paper_finish == 'Glossy'


def test_paper_finish_argument_is_none():
    """testing if paper_finish argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_finish=None)

    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not NoneType"


def test_paper_finish_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the paper_finish
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_finish = None

    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not NoneType"


def test_paper_finish_argument_is_not_a_string():
    """testing if a TypeError will be raised if the paper_finish argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_finish=312)

    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not int"


def test_paper_finish_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the paper_finish attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_finish = 443

    assert str(cm.value) == "ICCGenerator.paper_finish should be a str, not int"


def test_paper_finish_argument_is_working_properly():
    """testing if the paper_finish argument value is properly passed to the
    paper_finish attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'Silk'
    icc_gen = ICCGenerator(paper_finish=test_value)
    assert icc_gen.paper_finish == test_value


def test_paper_finish_attribute_is_working_properly():
    """testing if the paper_finish attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'Silk'
    icc_gen = ICCGenerator()
    assert icc_gen.paper_finish != test_value
    icc_gen.paper_finish = test_value
    assert icc_gen.paper_finish == test_value


def test_ink_brand_argument_is_skipped():
    """testing if the default value is used when the ink_brand argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.ink_brand == 'CanonInk'


def test_ink_brand_argument_is_none():
    """testing if ink_brand argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(ink_brand=None)

    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not NoneType"


def test_ink_brand_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the ink_brand
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.ink_brand = None

    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not NoneType"


def test_ink_brand_argument_is_not_a_string():
    """testing if a TypeError will be raised if the ink_brand argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(ink_brand=312)

    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not int"


def test_ink_brand_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the ink_brand attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.ink_brand = 443

    assert str(cm.value) == "ICCGenerator.ink_brand should be a str, not int"


def test_ink_brand_argument_is_working_properly():
    """testing if the ink_brand argument value is properly passed to the
    ink_brand attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'PhotoInk'
    icc_gen = ICCGenerator(ink_brand=test_value)
    assert icc_gen.ink_brand == test_value


def test_ink_brand_attribute_is_working_properly():
    """testing if the ink_brand attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'PhotoInk'
    icc_gen = ICCGenerator()
    assert icc_gen.ink_brand != test_value
    icc_gen.ink_brand = test_value
    assert icc_gen.ink_brand == test_value


def test_paper_size_argument_is_skipped():
    """testing if the default value is used when the paper_size argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.paper_size == 'A4'


def test_paper_size_argument_is_none():
    """testing if paper_size argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_size=None)

    assert str(cm.value) == "ICCGenerator.paper_size should be a str, not NoneType"


def test_paper_size_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the paper_size
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_size = None

    assert str(cm.value) == "ICCGenerator.paper_size should be a str, not NoneType"


def test_paper_size_argument_is_not_a_string():
    """testing if a TypeError will be raised if the paper_size argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(paper_size=312)

    assert str(cm.value) == "ICCGenerator.paper_size should be a str, not int"


def test_paper_size_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the paper_size attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.paper_size = 443

    assert str(cm.value) == "ICCGenerator.paper_size should be a str, not int"


def test_paper_size_argument_value_is_not_one_of_the_enum_values():
    """testing if a ValueError will be raised if the paper_size argument is not
    one of the enum values
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(ValueError) as cm:
        icc_gen = ICCGenerator(paper_size='A2')

    assert str(cm.value) == \
        "ICCGenerator.paper_size should be one of ['A3', 'A4'], not A2"


def test_paper_size_attribute_value_is_not_one_of_the_enum_values():
    """testing if a ValueError will be raised if the paper_size attribute is
    set to a value other than on of the enum values
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    import pytest
    with pytest.raises(ValueError) as cm:
        icc_gen.paper_size = 'A2'

    assert str(cm.value) == \
        "ICCGenerator.paper_size should be one of ['A3', 'A4'], not A2"


def test_paper_size_argument_is_working_properly():
    """testing if the paper_size argument value is properly passed to the
    paper_size attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'A3'
    icc_gen = ICCGenerator(paper_size=test_value)
    assert icc_gen.paper_size == test_value


def test_paper_size_attribute_is_working_properly():
    """testing if the paper_size attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'A3'
    icc_gen = ICCGenerator()
    assert icc_gen.paper_size != test_value
    icc_gen.paper_size = test_value
    assert icc_gen.paper_size == test_value


def test_number_of_pages_argument_is_skipped():
    """testing if the default value is used when the number_of_pages argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.number_of_pages == 1


def test_number_of_pages_argument_is_none():
    """testing if number_of_pages argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(number_of_pages=None)

    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not NoneType"


def test_number_of_pages_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the number_of_pages
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.number_of_pages = None

    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not NoneType"


def test_number_of_pages_argument_is_not_a_string():
    """testing if a TypeError will be raised if the number_of_pages argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(number_of_pages='312')

    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not str"


def test_number_of_pages_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the number_of_pages attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.number_of_pages = '443'

    assert str(cm.value) == "ICCGenerator.number_of_pages should be a int, not str"


def test_number_of_pages_argument_is_working_properly():
    """testing if the number_of_pages argument value is properly passed to the
    number_of_pages attribute
    """
    from icc_generator import ICCGenerator
    test_value = 10
    icc_gen = ICCGenerator(number_of_pages=test_value)
    assert icc_gen.number_of_pages == test_value


def test_number_of_pages_attribute_is_working_properly():
    """testing if the number_of_pages attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 10
    icc_gen = ICCGenerator()
    assert icc_gen.number_of_pages != test_value
    icc_gen.number_of_pages = test_value
    assert icc_gen.number_of_pages == test_value


def test_copyright_info_argument_is_skipped():
    """testing if the default value is used when the copyright_info argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.copyright_info == ""


def test_copyright_info_argument_is_none():
    """testing if copyright_info argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(copyright_info=None)

    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not NoneType"


def test_copyright_info_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the copyright_info
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.copyright_info = None

    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not NoneType"


def test_copyright_info_argument_is_not_a_string():
    """testing if a TypeError will be raised if the copyright_info argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(copyright_info=312)

    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not int"


def test_copyright_info_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the copyright_info attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.copyright_info = 443

    assert str(cm.value) == "ICCGenerator.copyright_info should be a str, not int"


def test_copyright_info_argument_is_working_properly():
    """testing if the copyright_info argument value is properly passed to the
    copyright_info attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'Erkan Ozgur Yilmaz'
    icc_gen = ICCGenerator(copyright_info=test_value)
    assert icc_gen.copyright_info == test_value


def test_copyright_info_attribute_is_working_properly():
    """testing if the copyright_info attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'Erkan Ozgur Yilmaz'
    icc_gen = ICCGenerator()
    assert icc_gen.copyright_info != test_value
    icc_gen.copyright_info = test_value
    assert icc_gen.copyright_info == test_value


def test_use_high_density_mode_argument_is_skipped():
    """testing if the default value is used when the use_high_density_mode
    argument is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.use_high_density_mode is True


def test_use_high_density_mode_argument_is_none():
    """testing if use_high_density_mode argument is set to None will raise an
    TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(use_high_density_mode=None)

    assert str(cm.value) == "ICCGenerator.use_high_density_mode should be a bool (True or False), not NoneType"


def test_use_high_density_mode_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the use_high_density_mode
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.use_high_density_mode = None

    assert str(cm.value) == "ICCGenerator.use_high_density_mode should be a bool (True or False), not NoneType"


def test_use_high_density_mode_argument_is_not_a_bool():
    """testing if a TypeError will be raised if the use_high_density_mode argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(use_high_density_mode=312)

    assert str(cm.value) == "ICCGenerator.use_high_density_mode should be a bool (True or False), not int"


def test_use_high_density_mode_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the use_high_density_mode attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.use_high_density_mode = 443

    assert str(cm.value) == "ICCGenerator.use_high_density_mode should be a bool (True or False), not int"


def test_use_high_density_mode_argument_is_working_properly():
    """testing if the use_high_density_mode argument value is properly passed to the
    use_high_density_mode attribute
    """
    from icc_generator import ICCGenerator
    test_value = False
    icc_gen = ICCGenerator(use_high_density_mode=test_value)
    assert icc_gen.use_high_density_mode == test_value


def test_use_high_density_mode_attribute_is_working_properly():
    """testing if the use_high_density_mode attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = False
    icc_gen = ICCGenerator()
    assert icc_gen.use_high_density_mode != test_value
    icc_gen.use_high_density_mode = test_value
    assert icc_gen.use_high_density_mode == test_value


def test_initializing_non_default_values():
    """testing if the class ICCGenerator initializes non default values
    correctly
    """
    from icc_generator import ICCGenerator
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%m")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_name = "Canon_iX6850_Kodak_UPPP_Glossy_A4_CanonInk_%s_%s" % (
        date_str, time_str
    )
    assert icc_gen.profile_name == profile_name


def test_paper_sizes():
    """testing if default page sizes are working properly
    """
    from icc_generator import ICCGenerator
    assert ICCGenerator.A3 == "A3"
    assert ICCGenerator.A4 == "A4"

    icc_gen = ICCGenerator()
    assert icc_gen.A3 == "A3"
    assert icc_gen.A4 == "A4"


def test_per_page_patch_count_is_updated_properly():
    """testing if the per_page_patch_count is properly updated with the paper
    size and use_high_density_mode attribute values
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # Set the paper size to A4
    icc_gen.paper_size = icc_gen.A4
    icc_gen.use_high_density_mode = False
    assert icc_gen.per_page_patch_count == 210

    icc_gen.use_high_density_mode = True
    assert icc_gen.per_page_patch_count == 600

    # Set the paper size to A3
    icc_gen.paper_size = icc_gen.A3
    icc_gen.use_high_density_mode = False
    assert icc_gen.per_page_patch_count == 460

    icc_gen.use_high_density_mode = True
    assert icc_gen.per_page_patch_count == 1260


def test_patch_count_is_read_only():
    """testing if the patch_count is a read only property
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    import pytest
    with pytest.raises(AttributeError) as cm:
        icc_gen.patch_count = 120

    # assert str(cm.value) == 'Patch count can not be set. Please update paper_size, ' \
    #                  'use_high_density_mode and page_count'


def test_patch_count_is_updating_properly():
    """testing if the patch_count is updating properly with changing values of
    page_size, page_count and use_high_density_mode attributes
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # Paper Size:A4
    # Use High Density Mode: False
    icc_gen.paper_size = icc_gen.A4
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
    assert icc_gen.patch_count == 600

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 1200

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 1800

    # Paper Size:A3
    # Use High Density Mode: False
    icc_gen.paper_size = icc_gen.A3
    icc_gen.use_high_density_mode = False

    # 1 Page
    icc_gen.number_of_pages = 1
    assert icc_gen.patch_count == 460

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 920

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 1380

    # Use High Density Mode: True
    icc_gen.use_high_density_mode = True

    # 1 Page
    icc_gen.number_of_pages = 1
    assert icc_gen.patch_count == 1260

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 2520

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 3780


def test_profile_name_template_default_value():
    """testing if the profile_name_template default value is correct
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    assert icc_gen.profile_name_template == \
        "{printer_brand}_{printer_model}_{paper_brand}_" \
        "{paper_model}_{paper_finish}_{paper_size}_{ink_brand}_" \
        "{profile_date}_{profile_time}"


def test_profile_name_default_value_is_properly_calculated():
    """testing if profile_name default value is properly calculated
    """
    from icc_generator import ICCGenerator
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%m")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_name = "Canon_iX6850_Kodak_UPPP_Glossy_A4_CanonInk_%s_%s" % (
        date_str, time_str
    )
    assert icc_gen.profile_name == profile_name


def test_profile_name_is_working_properly():
    """testing if the profile_name attribute is working properly
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # the profile_name could be updated in any ways the user wanted
    test_value = 'This is a valid profile name (but a bad one)'
    icc_gen.profile_name = test_value
    assert icc_gen.profile_name == test_value


def test_generate_targets():
    """testing if generate_targets is working properly
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = icc_gen.A4
    icc_gen.generate_targets()

    import os
    assert os.path.exists(
        os.path.join(icc_gen.output_path, icc_gen.profile_name, '.ti1')
    )
    assert os.path.exists(
        os.path.join(icc_gen.output_path, icc_gen.profile_name, '.ti2')
    )

    assert os.path.exists(
        os.path.join(icc_gen.output_path, icc_gen.profile_name, '_01.tif')
    )


def test_print_charts():
    """testing if the print_charts is working properly
    """
    # This is hard to test
    # We need a container that we can install GIMP and GutenPrint when needed
    # and uninstall when it
    raise NotImplementedError("Test is not implemented yet")


def test_read_charts():
    """testing if the read_charts method is working properly
    """
    # again this is hard to test
    # we can check if the chartread process is started etc.
    # and there should be a .ti3 file afterwards
    raise NotImplementedError("Test is not implemented yet")


def test_generate_profile():
    """testing if the generate_profile method is working properly
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    # again we need some pre build data so when the generate_profile has
    # run we can check if the ICC Profile is generated
    raise NotImplementedError("Test is not implemented yet")


def test_install_profile():
    """testing if the install_profile method is working properly
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    # this is easy
    # just check if ICC file is copied to the correct folder
    raise NotImplementedError("Test is not implemented yet")
