from twttr import shorten


def test_Uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("WHAT'S YOUR NAME?") == "WHT'S YR NM?"
    assert shorten("CS50") == "CS50"


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("what's your name?") == "wht's yr nm?"
    assert shorten("cs50") == "cs50"


def test_MIX():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Wht's yr nm?") == "Wht's yr nm?"
    assert shorten("Cs50") == "Cs50"
