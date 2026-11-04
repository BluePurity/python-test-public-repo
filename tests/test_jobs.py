from tracker.jobs import run_poll


def test_run_poll():
    assert run_poll([1, 2]) == [{"id": 1, "status": "in_transit"}, {"id": 2, "status": "delivered"}]
