from tracker.versions import newest, supports


def test_supports():
    assert supports("2.10") and supports("2.1") and not supports("1.9")


def test_newest():
    assert newest(["2.9", "2.10", "1.0"]) == "2.10" and newest([]) is None
