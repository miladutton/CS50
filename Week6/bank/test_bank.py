import bank
from bank import value

def test_hello_lower():
    assert value("Hello world") == 0
def test_h():
    assert value("Hi world") == 20
def test_not_h():
    assert value("world") == 100
