from numb3rs import validate

def test_validate_numbers():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("275.275.275.275") == False
    assert validate("1.2.3.275") == False
    assert validate("275.1.2.3") == False


def test_validate_incorrect_format():
    assert validate("cat.dog.pig.horse") == False
    assert validate("1.1.1.1.1") == False
    assert validate("1") == False
