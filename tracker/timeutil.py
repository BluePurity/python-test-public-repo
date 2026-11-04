"""Timestamps. Legacy: datetime.utcnow() (deprecated 3.12). Callers expect naive UTC."""
import datetime


def now():
    return datetime.datetime.utcnow()


def eta_hours(dispatched, transit_hours=48):
    if dispatched.tzinfo is not None:
        raise ValueError("dispatched must be naive UTC")
    remaining = dispatched + datetime.timedelta(hours=transit_hours) - datetime.datetime.utcnow()
    return max(0, int(remaining.total_seconds() // 3600))
