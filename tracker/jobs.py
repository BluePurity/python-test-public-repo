"""Async status polling. Legacy: @asyncio.coroutine / yield from (removed 3.11)."""
import asyncio


@asyncio.coroutine
def poll(shipment_id):
    yield from asyncio.sleep(0)
    return {"id": shipment_id, "status": "in_transit" if shipment_id % 2 else "delivered"}


@asyncio.coroutine
def poll_all(ids):
    results = []
    for i in ids:
        r = yield from poll(i)
        results.append(r)
    return results


def run_poll(ids):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(poll_all(ids))
    finally:
        loop.close()
