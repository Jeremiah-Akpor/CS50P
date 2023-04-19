from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True

def test_is_not_valid():
    assert is_valid("CS50P") == False
    assert is_valid("5CS50") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_is_not_valid2():
    assert is_valid("thispython") == False
    assert is_valid("11A111") == False
    assert is_valid("32") == False

if __name__ == "__main__":
    main()