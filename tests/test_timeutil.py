import datetime

from tracker.timeutil import eta_hours, now


def test_now_is_naive():
    assert now().tzinfo is None


def test_eta():
    assert eta_hours(now() - datetime.timedelta(hours=100)) == 0
    assert 46 <= eta_hours(now()) <= 48
