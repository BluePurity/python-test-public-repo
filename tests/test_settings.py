import pytest

from tracker.settings import parse


def test_defaults():
    assert parse("") == {"carrier": "royal-mail", "express": False, "max_parcels": 20}


def test_overrides():
    s = parse("[tracker]\nexpress = yes\nmax_parcels = 5\n")
    assert s["express"] is True and s["max_parcels"] == 5


def test_invalid_flag():
    with pytest.raises(ValueError):
        parse("[tracker]\nexpress = maybe\n")
