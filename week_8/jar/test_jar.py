from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
         Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(4)
    assert jar.size == 7
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"