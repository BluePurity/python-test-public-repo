"""Shipment registry. Legacy: subclasses collections.MutableMapping (removed in 3.10)."""
import collections
import collections.abc


class Registry(collections.abc.MutableMapping):
    def __init__(self):
        self._items = {}

    def __getitem__(self, key):
        return self._items[key]

    def __setitem__(self, key, value):
        if not isinstance(value, collections.abc.Mapping):
            raise TypeError("shipment must be a mapping")
        self._items[str(key).upper()] = dict(value)

    def __delitem__(self, key):
        del self._items[key]

    def __iter__(self):
        return iter(sorted(self._items))

    def __len__(self):
        return len(self._items)


def total_weight(shipments):
    if not isinstance(shipments, collections.abc.Iterable):
        raise TypeError("shipments must be iterable")
    return round(sum(float(s.get("weight", 0)) for s in shipments), 3)


def by_status(shipments, status):
    return sorted(s["id"] for s in shipments if s.get("status") == status)
