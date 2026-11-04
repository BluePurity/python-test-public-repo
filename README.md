# python-test-public-repo — shipment-tracker

A small **legacy Python 3.9** service used as a public test target for the Solara
refactor/validation agents (upgrade target: Python 3.12).

It intentionally uses standard-library APIs that were removed or deprecated after 3.9:
`collections.MutableMapping`, `configparser.SafeConfigParser` / `readfp`, `distutils`,
`datetime.utcnow`, `locale.format`, `pipes.quote`, `@asyncio.coroutine`, `inspect.getargspec`.

```bash
python3.9 -m pip install pytest
python3.9 -m pytest        # all tests pass on 3.9; collection fails on 3.12
```
No third-party runtime dependencies.
