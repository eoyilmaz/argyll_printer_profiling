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


def test_precondition_profile_path_argument_is_skipped():
    """testing if the default value is used when the precondition_profile_path argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.precondition_profile_path == ""


def test_precondition_profile_path_argument_is_none():
    """testing if precondition_profile_path argument is set to None will raise an TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(precondition_profile_path=None)

    assert str(cm.value) == "ICCGenerator.precondition_profile_path should be a str, not NoneType"


def test_precondition_profile_path_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the precondition_profile_path
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.precondition_profile_path = None

    assert str(cm.value) == "ICCGenerator.precondition_profile_path should be a str, not NoneType"


def test_precondition_profile_path_argument_is_not_a_string():
    """testing if a TypeError will be raised if the precondition_profile_path argument
    value is not a string
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(precondition_profile_path=312)

    assert str(cm.value) == "ICCGenerator.precondition_profile_path should be a str, not int"


def test_precondition_profile_path_attribute_is_not_set_to_a_string():
    """testing if a TypeError will be raised when the precondition_profile_path attribute
    is set to a value other than a string
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.precondition_profile_path = 443

    assert str(cm.value) == "ICCGenerator.precondition_profile_path should be a str, not int"


def test_precondition_profile_path_argument_is_working_properly():
    """testing if the precondition_profile_path argument value is properly passed to the
    precondition_profile_path attribute
    """
    from icc_generator import ICCGenerator
    test_value = 'Epson'
    icc_gen = ICCGenerator(precondition_profile_path=test_value)
    assert icc_gen.precondition_profile_path == test_value


def test_precondition_profile_path_attribute_is_working_properly():
    """testing if the precondition_profile_path attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 'Epson'
    icc_gen = ICCGenerator()
    assert icc_gen.precondition_profile_path != test_value
    icc_gen.precondition_profile_path = test_value
    assert icc_gen.precondition_profile_path == test_value


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
    time_str = now.strftime("%H%M")
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
    assert icc_gen.per_page_patch_count == 672

    # Set the paper size to A3
    icc_gen.paper_size = icc_gen.A3
    icc_gen.use_high_density_mode = False
    assert icc_gen.per_page_patch_count == 445

    icc_gen.use_high_density_mode = True
    assert icc_gen.per_page_patch_count == 1392


def test_patch_count_is_read_only():
    """testing if the patch_count is a read only property
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    import pytest
    with pytest.raises(AttributeError) as cm:
        icc_gen.patch_count = 120


def test_gray_patch_count_argument_is_skipped():
    """testing if the default value is used when the gray_patch_count argument
    is skipped
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.gray_patch_count == 16


def test_gray_patch_count_argument_is_none():
    """testing if gray_patch_count argument is set to None will raise an
    TypeError
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(gray_patch_count=None)

    assert str(cm.value) == "ICCGenerator.gray_patch_count should be an int, " \
                            "not NoneType"


def test_gray_patch_count_attribute_is_set_to_none():
    """testing if an TypeError will be raised when the gray_patch_count
    attribute is set to None
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.gray_patch_count = None

    assert str(cm.value) == "ICCGenerator.gray_patch_count should be an int, " \
                            "not NoneType"


def test_gray_patch_count_argument_is_not_an_int():
    """testing if a TypeError will be raised if the gray_patch_count argument
    value is not an int
    """
    from icc_generator import ICCGenerator
    import pytest
    with pytest.raises(TypeError) as cm:
        icc_gen = ICCGenerator(gray_patch_count="312")

    assert str(cm.value) == "ICCGenerator.gray_patch_count should be an int, " \
                            "not str"


def test_gray_patch_count_attribute_is_not_set_to_an_int():
    """testing if a TypeError will be raised when the gray_patch_count
    attribute is set to a value other than an int
    """
    from icc_generator import ICCGenerator
    import pytest
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.gray_patch_count = "443"

    assert str(cm.value) == "ICCGenerator.gray_patch_count should be an int, " \
                            "not str"


def test_gray_patch_count_argument_is_working_properly():
    """testing if the gray_patch_count argument value is properly passed to the
    gray_patch_count attribute
    """
    from icc_generator import ICCGenerator
    test_value = 64
    icc_gen = ICCGenerator(gray_patch_count=test_value)
    assert icc_gen.gray_patch_count == test_value


def test_gray_patch_count_attribute_is_working_properly():
    """testing if the gray_patch_count attribute is working properly
    """
    from icc_generator import ICCGenerator
    test_value = 64
    icc_gen = ICCGenerator()
    assert icc_gen.gray_patch_count != test_value
    icc_gen.gray_patch_count = test_value
    assert icc_gen.gray_patch_count == test_value


def test_gray_patch_count_is_updated_properly():
    """testing if the gray_patch_count is properly updated with the paper
    size and use_high_density_mode attribute values
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # Set the paper size to A4
    icc_gen.paper_size = icc_gen.A4
    icc_gen.number_of_pages = 1
    assert icc_gen.gray_patch_count == 16

    icc_gen.number_of_pages = 2
    assert icc_gen.gray_patch_count == 16

    icc_gen.number_of_pages = 3
    assert icc_gen.gray_patch_count == 16

    icc_gen.number_of_pages = 4
    assert icc_gen.gray_patch_count == 16

    icc_gen.gray_patch_count = 25
    assert icc_gen.number_of_pages == 4
    assert icc_gen.gray_patch_count == 25


def test_gray_patch_count_is_not_read_only():
    """testing if the gray_patch_count is not a read only property
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    icc_gen.gray_patch_count = 120
    assert icc_gen.gray_patch_count == 120


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
    assert icc_gen.patch_count == 672

    # 2 Pages
    icc_gen.number_of_pages = 2
    assert icc_gen.patch_count == 1344

    # 3 Pages
    icc_gen.number_of_pages = 3
    assert icc_gen.patch_count == 2016

    # Paper Size:A3
    # Use High Density Mode: False
    icc_gen.paper_size = icc_gen.A3
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
    time_str = now.strftime("%H%M")
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


def test_profile_path_template_default_value():
    """testing if the profile_path_template default value is correct
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    assert icc_gen._profile_path_template == \
        "~/.cache/ICCGenerator/{printer_brand}_" \
        "{printer_model}/{profile_date}"


def test_profile_path_default_value_is_properly_calculated():
    """testing if profile_path default value is properly calculated
    """
    from icc_generator import ICCGenerator
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    assert icc_gen.profile_path == profile_path


def test_profile_path_is_read_only():
    """testing if the profile_path property is read only
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # the profile_path could be updated in any ways the user wanted
    import pytest
    with pytest.raises(AttributeError):
        icc_gen.profile_path = "some value"


def test_profile_absolute_path_is_properly_calculated():
    """testing if profile_absolute_path is properly calculated
    """
    from icc_generator import ICCGenerator
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    import os
    assert icc_gen.profile_absolute_path == os.path.expanduser(profile_path)


def test_profile_absolute_path_is_is_read_only():
    """testing if profile_absolute_path is properly calculated
    """
    from icc_generator import ICCGenerator
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    import os
    import pytest
    with pytest.raises(AttributeError) as cm:
        icc_gen.profile_absolute_path = os.path.expanduser(profile_path)

    assert str(cm.value) == "can't set attribute"


def test_profile_absolute_full_path_is_properly_calculated():
    """testing if profile_absolute_full_path is properly calculated
    """
    from icc_generator import ICCGenerator
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    import os
    assert icc_gen.profile_absolute_full_path == os.path.join(
        os.path.expandvars(os.path.expanduser(profile_path)),
        icc_gen.profile_name
    )


def test_profile_absolute_full_path_is_is_read_only():
    """testing if profile_absolute_full_path is properly calculated
    """
    from icc_generator import ICCGenerator
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    icc_gen = ICCGenerator()

    assert icc_gen.profile_date == date_str
    assert icc_gen.profile_time == time_str
    profile_path = "~/.cache/ICCGenerator/Canon_iX6850/%s" % date_str
    import os
    import pytest
    with pytest.raises(AttributeError) as cm:
        icc_gen.profile_absolute_full_path = os.path.expanduser(profile_path)

    assert str(cm.value) == "can't set attribute"


def test_generate_target_creates_the_output_folder(file_collector):
    """testing if generate_target will create the output folder
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = icc_gen.A4
    file_collector.append(icc_gen.profile_absolute_path)
    icc_gen.generate_target()
    import os
    assert os.path.exists(
        os.path.expanduser(
            os.path.join(icc_gen.output_path)
        )
    )


def test_generate_target_generates_ti_file(file_collector):
    """testing if generate_target will generate ti
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = icc_gen.A4
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()

    import os
    expected_path = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '.ti1')
        )
    )
    assert os.path.exists(expected_path)


def test_generate_tif_files_will_generate_tif_files_from_target_file(file_collector):
    """testing if generate_tif_files will generate tif file or files from target file
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = icc_gen.A4
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()

    # import time
    # time.sleep(20)

    import os
    profile_absolute_full_path = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '.tif')
        )
    )
    print("profile_absolute_full_path: %s" % profile_absolute_full_path)
    assert os.path.exists(profile_absolute_full_path)
    assert not os.path.exists(
        os.path.expanduser(
            os.path.join(
                icc_gen.profile_path,
                "%s%s" % (icc_gen.profile_name, '_02.tif')
            )
        )
    )


def test_generate_tif_files_will_generates_correct_amount_of_tif_files(file_collector):
    """testing if generate_tif_files correct amount of tif files file
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = icc_gen.A4
    # append the folder to the file_collector
    # so it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    import os
    assert os.path.exists(
        os.path.expanduser(
            os.path.join(
                icc_gen.profile_path,
                "%s%s" % (icc_gen.profile_name, '_01.tif')
            )
        )
    )
    assert os.path.exists(
        os.path.expanduser(
            os.path.join(
                icc_gen.profile_path,
                "%s%s" % (icc_gen.profile_name, '_02.tif')
            )
        )
    )


def test_generate_tif_files_will_fill_tif_files_attribute_single_page(file_collector):
    """testing if generate_tif_files will fill the tif_files list correctly
    when there is only one page
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 1
    icc_gen.paper_size = icc_gen.A4
    # append the folder to the file_collector
    # so it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    import os
    tif1 = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '.tif')
        )
    )

    assert icc_gen.tif_files[0] == tif1


def test_generate_tif_files_will_fill_tif_files_attribute_more_than_one_page(file_collector):
    """testing if generate_tif_files will fill the tif_files list correctly
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = icc_gen.A4
    # append the folder to the file_collector
    # so it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    import os
    tif1 = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '_01.tif')
        )
    )

    tif2 = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '_02.tif')
        )
    )

    assert icc_gen.tif_files[0] == tif1
    assert icc_gen.tif_files[1] == tif2


def test_generate_tif_files_will_clear_the_tif_files_list(file_collector):
    """testing if generate_tif_files will clear the tif_files list before
    running to prevent filling it over and over with previous runs
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = icc_gen.A4
    # append the folder to the file_collector
    # so it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    import os
    tif1 = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '_01.tif')
        )
    )

    tif2 = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '_02.tif')
        )
    )
    assert len(icc_gen.tif_files) == 2
    assert icc_gen.tif_files[0] == tif1
    assert icc_gen.tif_files[1] == tif2

    # change number of pages to 1
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()

    import os
    tif1 = os.path.expanduser(
        os.path.join(
            icc_gen.profile_path,
            "%s%s" % (icc_gen.profile_name, '.tif')
        )
    )

    assert len(icc_gen.tif_files) == 1
    assert icc_gen.tif_files[0] == tif1


def test_generate_tif_files_with_high_density_mode(file_collector, patch_run_external_process):
    """testing if generate_tif_files will use i1 Pro as the input device when
    the use_high_density_mode is set to False
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = icc_gen.A4
    # append the folder to the file_collector
    # so it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()
    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert any(['-ii1' in arg for arg in final_command])


def test_generate_tif_files_with_normal_density_mode(file_collector, patch_run_external_process):
    """testing if generate_tif_files will use ColorMunki as the input device
    when the use_high_density_mode is set to False
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()

    # There should be files under the temp folder
    # check them
    # set it to use only one A4 page
    icc_gen.number_of_pages = 2
    icc_gen.paper_size = icc_gen.A4
    icc_gen.use_high_density_mode = False
    # append the folder to the file_collector
    # so it is cleaned up after the test
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()
    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert any(['-iCM' in arg for arg in final_command])


def test_print_charts(file_collector, patch_run_external_process):
    """testing if the print_charts is working properly
    """
    # patch the run_external_process and check the command
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)

    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert 'gimp' in final_command[0]


def test_read_charts_calls_chartread_command(file_collector, patch_run_external_process):
    """testing if the read_charts method will call chartread
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts()

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert 'chartread' in final_command[0]


def test_read_charts_with_resume_set_to_True(file_collector, patch_run_external_process):
    """testing if the read_charts method with resume=True will call chartread
    with -r option
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts(resume=True)

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert 'chartread' in final_command[0]

    assert any(['-r' in arg for arg in final_command])


def test_read_charts_with_read_mode_set_to_1(file_collector, patch_run_external_process):
    """testing if the read_charts method with read_mode=1 will call chartread
    with -p and -P options
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    icc_gen.number_of_pages = 1
    file_collector.append(icc_gen.profile_path)
    icc_gen.generate_target()
    icc_gen.generate_tif()
    icc_gen.print_charts()
    icc_gen.read_charts(read_mode=1)

    # check the final call to the run_external_process
    final_command = patch_run_external_process[-1]
    assert 'chartread' in final_command[0]

    assert any(['-p' in arg for arg in final_command])
    assert any(['-P' in arg for arg in final_command])


def test_generate_profile_1(file_collector, patch_run_external_process):
    """testing if the generate_profile method is working properly
    """
    from icc_generator import ICCGenerator
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
    assert 'colprof' in final_command[0]

    assert any(['-v' in arg for arg in final_command])
    assert any(['-qh' in arg for arg in final_command])
    assert any(['-r0.5' in arg for arg in final_command])
    assert any(['-S' in arg for arg in final_command])
    assert any(['-cmt' in arg for arg in final_command])
    assert any(['-dpp' in arg for arg in final_command])
    assert any(['-D' in arg for arg in final_command])


def test_generate_profile_2(file_collector, patch_run_external_process):
    """testing if the generate_profile method is working properly
    """
    from icc_generator import ICCGenerator
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
    assert 'colprof' in final_command[0]

    assert any(['-CErkan Ozgur Yilmaz(c)2021' in arg for arg in final_command])


def test_check_profile(file_collector, patch_run_external_process):
    """testing if the check_profile method is working properly
    """
    from icc_generator import ICCGenerator
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
    assert 'profcheck' in final_command[0]

    assert any(["-k" in arg for arg in final_command])
    assert any(["-v2" in arg for arg in final_command])
    assert not any(["-s" in arg for arg in final_command])


def test_check_profile_with_sort(file_collector, patch_run_external_process):
    """testing if the check_profile method is working properly
    """
    from icc_generator import ICCGenerator
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
    icc_gen.check_profile(sort_by_dE=True)

    final_command = patch_run_external_process[-1]
    assert 'profcheck' in final_command[0]

    assert any(["-k" in arg for arg in final_command])
    assert any(["-v2" in arg for arg in final_command])
    assert any(["-s" in arg for arg in final_command])


def test_check_profile_with_correct_file_extension(file_collector, patch_run_external_process):
    """testing if the check_profile method is using the correct profile file extension, that is ICM on Windows and ICC
    on Linux
    """
    from icc_generator import ICCGenerator
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
    icc_gen.check_profile(sort_by_dE=True)

    final_command = patch_run_external_process[-1]
    assert 'profcheck' in final_command[0]

    import os
    if os.name == 'nt':
        assert any([".icm" in arg for arg in final_command])
        assert not any([".icc" in arg for arg in final_command])
    else:
        assert not any([".icm" in arg for arg in final_command])
        assert any([".icc" in arg for arg in final_command])


def test_install_profile_1(file_collector, patch_run_external_process):
    """testing if the install_profile method is working properly
    """
    import os
    from icc_generator import ICCGenerator
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
    os.makedirs(os.path.expandvars(os.path.expanduser(icc_gen.profile_path)), exist_ok=True)
    assert os.path.expandvars(os.path.expanduser(icc_gen.profile_path))
    with open(dummy_icc_profile_full_path, "w+") as f:
        f.write("dummy icc file!!!")
    assert os.path.exists(dummy_icc_profile_full_path)
    file_collector.append(dummy_icc_profile_full_path)

    icc_gen.install_profile()

    # this is easy
    # just check if ICC file is copied to the correct folder
    import os
    profile_install_path = None
    if os.name == 'nt':
        profile_install_path = os.path.expandvars('$WINDIR/System32spool/drivers/color/%s.icc' % icc_gen.profile_name)
    elif os.name == 'posix':
        profile_install_path = os.path.expandvars(
            os.path.expanduser(
                '~/.local/share/icc/%s.icc' % icc_gen.profile_name
            )
        )

    assert profile_install_path is not None
    file_collector.append(profile_install_path)
    assert os.path.exists(
        os.path.expandvars(
            profile_install_path
        )
    )


def test_install_profile_2(file_collector, patch_run_external_process):
    """testing if the install_profile will raise a RuntimeError if the ICC has not been generated yet
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    file_collector.append(icc_gen.profile_path)
    icc_gen.number_of_pages = 1
    icc_gen.copyright_info = "Erkan Ozgur Yilmaz(c)2021"
    file_collector.append(icc_gen.profile_path)

    import pytest
    with pytest.raises(RuntimeError) as cm:
        icc_gen.install_profile()

    assert str(cm.value) == "ICC file doesn't exist, please generate it first!"


def test_default_logger_is_created(file_collector):
    """testing if a default logger has been created
    """
    import logging
    from icc_generator import logger
    assert isinstance(logger, logging.Logger)


def test_default_log_level_is_warning(file_collector):
    """testing if the default log level is warning
    """
    import logging
    from icc_generator import logger
    assert logger.level == logging.WARNING


def test_output_path_for_windows(set_to_windows):
    """testing if the output_path variable is correctly set for Windows
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.output_path == '%WINDIR%/System32/spool/drivers/color/'


def test_output_path_for_linux(set_to_linux):
    """testing if the output_path variable is correctly set for Linux
    """
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    assert icc_gen.output_path == '~/.local/share/icc/'


def test_color_correct_image_printer_profile_path_is_skipped(file_collector, patch_run_external_process):
    """testing if the color_correct_image method will raise a ValueError if the printer_profile_path argument is skipped
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            input_image_path=input_image_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent
        )

    assert str(cm.value) == 'Please specify a proper printer_profile_path!'


def test_color_correct_image_printer_profile_path_is_none(file_collector, patch_run_external_process):
    """testing if the color_correct_image method will raise a TypeError when the printer_profile_path argument is None
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == 'Please specify a proper printer_profile_path!'


def test_color_correct_image_printer_profile_path_doesnt_exist(file_collector, patch_run_external_process):
    """testing if the color_correct_image method will raise a ValueError when the path shown with printer_profile_path
    argument value doesn't exist
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path = tempfile.mktemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "printer_profile_path doesn't exists: %s" % printer_profile_path


def test_color_correct_image_printer_profile_path_is_not_an_icc_or_icm_file(file_collector, patch_run_external_process):
    """testing if a ValueError will be raised when the printer_profile_path argument value is not to a path to an ICC or
    ICM file
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.not_an_icc_file')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "printer_profile_path should be a valid ICC/ICM file: %s" % printer_profile_path


def test_color_correct_image_input_image_path_is_skipped(file_collector, patch_run_external_process):
    """testing if the color_correct_image method will raise a ValueError if the input_image_path argument is skipped
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"
    with pytest.raises(TypeError) as cm:
        ICCGenerator.color_correct_image(
            printer_profile_path=printer_profile_path,
            output_image_path=output_image_path,
            image_profile=image_profile,
            intent=intent
        )

    assert str(cm.value) == 'Please specify a proper input_image_path!'


def test_color_correct_image_input_image_is_none(file_collector, patch_run_external_process):
    """testing if the color_correct_image method will raise a TypeError when the input_image argument is None
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == 'Please specify a proper input_image_path!'


def test_color_correct_image_input_image_doesnt_exist(file_collector, patch_run_external_process):
    """testing if the color_correct_image method will raise a ValueError when the path shown with input_image
    argument value doesn't exist
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path = tempfile.mktemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "input_image_path doesn't exists: %s" % input_image_path


def test_color_correct_image_input_image_path_is_not_an_jpg_or_tif_file(file_collector, patch_run_external_process):
    """testing if a TypeError will be raised when the input_image_path argument value is not to a path to a JPG or TIF
    file
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.bmp')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "input_image_path should be a valid JPG/TIF file: %s" % input_image_path


def test_color_correct_image_output_image_path_is_skipped(file_collector, patch_run_external_process_class_method_version):
    """testing if a proper output_image_path will be generated when the output_image_path argument is skipped
    """
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        image_profile=image_profile,
        intent=intent
    )

    import os
    input_image_name, input_image_ext = os.path.splitext(input_image_path)
    expected_path = "%s_corrected_1%s" % (input_image_name, input_image_ext)
    assert any(expected_path in arg for arg in patch_run_external_process_class_method_version[0])


def test_color_correct_image_output_image_path_is_none(file_collector, patch_run_external_process_class_method_version):
    """testing if a proper output_image_path will be generated when the output_image_path argument is None
    """
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        image_profile=image_profile,
        intent=intent
    )

    import os
    input_image_name, input_image_ext = os.path.splitext(input_image_path)
    expected_path = "%s_corrected_1%s" % (input_image_name, input_image_ext)
    assert any(expected_path in arg for arg in patch_run_external_process_class_method_version[0])


def test_color_correct_image_output_image_path_is_not_a_tif_file(file_collector):
    """testing if a ValueError will be raised when the output_image_path is not a tif file path
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.bmp')
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
            intent=intent
        )

    assert str(cm.value) == 'output_image_path should be a valid JPG/TIF file: %s' % output_image_path


def test_color_correct_image_intent_is_skipped(file_collector, patch_run_external_process_class_method_version):
    """testing if the default value will be used when the intent argument is skipped
    """
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
    )

    assert "-i" in patch_run_external_process_class_method_version[0]
    assert "r" in patch_run_external_process_class_method_version[0]


def test_color_correct_image_intent_is_none(file_collector, patch_run_external_process_class_method_version):
    """testing if the default value will be used when the intent argument is None
    """
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
        intent=None
    )

    assert "-i" in patch_run_external_process_class_method_version[0]
    assert "r" in patch_run_external_process_class_method_version[0]


def test_color_correct_image_intent_is_not_a_string(file_collector):
    """testing if a TypeError will be raised when the intent argument is not a string
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "intent should be a string, not int"


def test_color_correct_image_intent_is_not_correct_enum_value(file_collector):
    """testing if a TypeError will be raised when the intent argument is not one of p, r, s, a
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "intent should be one of p, r, s, a, not %s" % intent


def test_color_correct_image_intent_is_working_properly(file_collector, patch_run_external_process_class_method_version):
    """testing if the default value will be used when the intent argument is None
    """
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
        intent=intent
    )

    assert "-i" in patch_run_external_process_class_method_version[0]
    assert "r" in patch_run_external_process_class_method_version[0]


def test_color_correct_image_profile_is_none(file_collector, patch_run_external_process_class_method_version):
    """testing if the default value will be used when the image_profile argument is None
    """
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "AdobeRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=None,
        intent=intent
    )

    assert "-p" in patch_run_external_process_class_method_version[0]
    assert any(["AdobeRGB" in arg for arg in patch_run_external_process_class_method_version[0]])


def test_color_correct_image_image_profile_is_not_a_string(file_collector):
    """testing if a TypeError will be raised when the image_profile argument is not a string
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "image_profile should be one of sRGB or AdobeRGB, not 123123"


def test_color_correct_image_image_profile_is_not_correct_enum_value(file_collector):
    """testing if a TypeError will be raised when the image_profile argument is not one of AdobeRGB or sRGB
    """
    import pytest
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
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
            intent=intent
        )

    assert str(cm.value) == "image_profile should be one of sRGB or AdobeRGB, not %s" % image_profile


def test_color_correct_image_image_profile_is_working_properly(file_collector, patch_run_external_process_class_method_version):
    """testing if a TypeError will be raised when the image_profile argument is working properly
    """
    import tempfile
    from icc_generator import ICCGenerator
    printer_profile_path_handle, printer_profile_path = tempfile.mkstemp(suffix='.icc')
    input_image_path_handle, input_image_path = tempfile.mkstemp(suffix='.tif')
    output_image_path = tempfile.mktemp(suffix='.tif')
    file_collector.append(printer_profile_path)
    file_collector.append(input_image_path)
    image_profile = "sRGB"
    intent = "r"

    ICCGenerator.color_correct_image(
        printer_profile_path=printer_profile_path,
        input_image_path=input_image_path,
        output_image_path=output_image_path,
        image_profile=image_profile,
        intent=intent
    )

    print("patch_run_external_process[0]: %s" % patch_run_external_process_class_method_version[0])
    assert any("-p" in arg for arg in patch_run_external_process_class_method_version[0])
    assert any("sRGB" in arg for arg in patch_run_external_process_class_method_version[0])


def test_save_settings_path_is_skipped(file_collector):
    """testing if the profile_path will be used when the path argument value is skipped
    """
    import os
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    settings_file_path = os.path.join(icc_gen.profile_path, "%s.json" % icc_gen.profile_name)

    file_collector.append(settings_file_path)

    assert not os.path.exists(os.path.expanduser(settings_file_path))
    icc_gen.save_settings()
    assert os.path.exists(os.path.expanduser(settings_file_path))


def test_save_settings_path_is_none(file_collector):
    """testing if the profile_path will be used when the path argument value is None
    """
    import os
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    settings_file_path = os.path.join(icc_gen.profile_path, "%s.json" % icc_gen.profile_name)

    file_collector.append(settings_file_path)

    assert not os.path.exists(os.path.expanduser(settings_file_path))
    icc_gen.save_settings(path=None)
    assert os.path.exists(os.path.expanduser(settings_file_path))


def test_save_settings_path_is_not_a_string():
    """testing if a TypeError will be raised when the path argument value is not a string
    """
    import pytest
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.save_settings(1)

    assert str(cm.value) == 'Please specify a valid path'


def test_save_settings_is_working_properly(file_collector, patch_run_external_process):
    """testing if the save_settings function is working properly
    """
    from icc_generator import ICCGenerator
    import tempfile
    icc_gen = ICCGenerator()
    path = tempfile.mktemp()
    file_collector.append(path)
    icc_gen.save_settings(path)

    import os
    assert os.path.exists(path)

    # check file content
    import json
    with open(path, "r") as f:
        data = json.load(f)

    assert data is not None
    icc_gen.ink_brand = data["ink_brand"]
    icc_gen.paper_brand = data["paper_brand"]
    icc_gen.paper_finish = data["paper_finish"]
    icc_gen.paper_model = data["paper_model"]
    icc_gen.paper_size = data["paper_size"]
    icc_gen.printer_brand = data["printer_brand"]
    icc_gen.printer_model = data["printer_model"]
    icc_gen.profile_date = data["profile_date"]
    icc_gen.profile_time = data["profile_time"]


def test_load_settings_path_is_skipped():
    """testing if a RuntimeError will be raised when the path argument is skipped
    """
    import pytest
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.load_settings()

    assert str(cm.value) == "load_settings() missing 1 required positional argument: 'path'"


def test_load_settings_path_is_none():
    """testing if a RuntimeError will be raised when the path argument value is None
    """
    import pytest
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.load_settings(None)

    assert str(cm.value) == 'Please specify a valid path'


def test_load_settings_path_is_not_a_string():
    """testing if a TypeError will be raised when the path argument value is not a string
    """
    import pytest
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    with pytest.raises(TypeError) as cm:
        icc_gen.load_settings(123)

    assert str(cm.value) == 'Please specify a valid path'


def test_load_settings_path_does_not_exist():
    """testing if a RuntimeError will be raised when the path doesn't exist
    """
    import pytest
    from icc_generator import ICCGenerator
    icc_gen = ICCGenerator()
    with pytest.raises(RuntimeError) as cm:
        icc_gen.load_settings("Some random error")

    assert str(cm.value) == "File does not exist!: Some random error"


def test_load_settings_is_working_properly(file_collector):
    """testing if the load_settings function is working properly
    """
    from icc_generator import ICCGenerator
    import tempfile
    icc_gen = ICCGenerator()

    # set some values
    icc_gen.ink_brand = 'Epson673'
    icc_gen.paper_brand = 'Agfa'
    icc_gen.paper_finish = 'Glossy'
    icc_gen.paper_model = 'HGPIP'
    icc_gen.paper_size = 'A4'
    icc_gen.printer_brand = 'Epson'
    icc_gen.printer_model = 'L800'

    path = tempfile.mktemp()
    file_collector.append(path)
    icc_gen.save_settings(path)

    import os
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
