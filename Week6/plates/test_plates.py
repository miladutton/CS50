import plates
from plates import is_valid

def test_first_two():
    assert is_valid("MGFCHK") == True
    assert is_valid("90") == False
    assert is_valid("C9VCH") == False
    assert is_valid("5") == False

def test_length():
    assert is_valid("V") == False
    assert is_valid("BVVAKG66") == False

def test_number_position():
    assert is_valid("VCA6C") == False

def test_zero():
    assert is_valid("VKAG07") == False

def test_punctuation():
    assert is_valid("VC KH5") == False
    assert is_valid("VC.H5") == False
    assert is_valid("VC?KH5") == False
