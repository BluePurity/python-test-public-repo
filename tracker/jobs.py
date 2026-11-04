"""Async status polling. Legacy: @asyncio.coroutine / yield from (removed 3.11)."""
import asyncio


async def poll(shipment_id):
    await asyncio.sleep(0)
    return {"id": shipment_id, "status": "in_transit" if shipment_id % 2 else "delivered"}


async def poll_all(ids):
    results = []
    for i in ids:
        r = await poll(i)
        results.append(r)
    return results


def run_poll(ids):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(poll_all(ids))
    finally:
        loop.close()
