from seasons import add_text

def test_words():
    assert add_text("12062880") == "Twelve million, sixty-two thousand, eight hundred eighty minutes"
    assert add_text("12326400") == "Twelve million, three hundred twenty-six thousand, four hundred minutes"
