import twttr
from twttr import shorten

def test_cap():
    assert shorten("HELLO WORLD") == "HLL WRLD"
def test_lower():
    assert shorten("hello world") == "hll wrld"
def test_numbers():
    assert shorten("He110 W0r1d") == "H110 W0r1d"
def test_punctuation():
    assert shorten("Hello, World") == "Hll, Wrld"
