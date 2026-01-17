from temp_convert import celsius_to_fahrenheit

def test_zero():
    assert celsius_to_fahrenheit(0) == 32

def test_positive():
    assert celsius_to_fahrenheit(25) == 77

def test_negative():
    assert celsius_to_fahrenheit(-40) == -40
