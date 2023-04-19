from numb3rs import validate

def test_validate_1():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2.cat.1") == False
    assert validate("1.cat.2.1") == False
    assert validate("1.2.2.cat") == False
    assert validate("cat") == False
    assert validate("1.1.1.1") == True
    assert validate("cat") == False
    assert validate("1.230.1000.0") == False
    assert validate("1.300.500.700") == False


