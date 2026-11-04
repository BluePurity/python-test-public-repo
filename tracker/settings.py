"""Settings. Legacy: SafeConfigParser/readfp (removed 3.12) and distutils.strtobool (removed 3.12)."""
import io
from configparser import ConfigParser

DEFAULTS = {"carrier": "royal-mail", "express": "no", "max_parcels": "20"}


def _strtobool(val):
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    if val in ("n", "no", "f", "false", "off", "0"):
        return 0
    raise ValueError("invalid truth value %r" % (val,))


def parse(text):
    parser = ConfigParser()
    parser.read_file(io.StringIO(text))
    out = dict(DEFAULTS)
    if parser.has_section("tracker"):
        out.update(dict(parser.items("tracker")))
    out["express"] = bool(_strtobool(out["express"]))
    out["max_parcels"] = int(out["max_parcels"])
    return out
