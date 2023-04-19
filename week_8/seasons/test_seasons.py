from seasons import validate,calc_minutes
from datetime import date

def test_seasons1():
    assert validate("1999-01-01") == date(1999, 1, 1)
    assert validate("2022-12-31") == date(2022, 12, 31)
    assert validate("2005-06-15") == date(2005, 6, 15)


