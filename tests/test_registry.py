import pytest

from tracker.registry import Registry, by_status, total_weight


def test_registry_normalises_keys_and_validates():
    r = Registry()
    r["ab1"] = {"weight": 2}
    assert list(r) == ["AB1"] and len(r) == 1
    with pytest.raises(TypeError):
        r["x"] = [1, 2]


def test_total_weight_and_status():
    s = [{"id": "b", "weight": "1.5", "status": "new"}, {"id": "a", "weight": 2, "status": "new"}]
    assert total_weight(s) == 3.5
    assert by_status(s, "new") == ["a", "b"]
