from um import count

def test_um1():
    assert count("Um, thanks, um..") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("um?") == 1
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("hello, um, world") == 1