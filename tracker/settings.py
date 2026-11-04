"""Settings. Legacy: SafeConfigParser/readfp (removed 3.12) and distutils.strtobool (removed 3.12)."""
import io
from configparser import SafeConfigParser
from distutils.util import strtobool

DEFAULTS = {"carrier": "royal-mail", "express": "no", "max_parcels": "20"}


def parse(text):
    parser = SafeConfigParser()
    parser.readfp(io.StringIO(text))
    out = dict(DEFAULTS)
    if parser.has_section("tracker"):
        out.update(dict(parser.items("tracker")))
    out["express"] = bool(strtobool(out["express"]))
    out["max_parcels"] = int(out["max_parcels"])
    return out
