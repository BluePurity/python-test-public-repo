"""API version negotiation. Legacy: distutils.version.LooseVersion (removed 3.12)."""
import re

_COMPONENT_RE = re.compile(r"(\d+ | [a-z]+ | \.)", re.VERBOSE)


def _version_key(v):
    if not v:
        raise AttributeError("'LooseVersion' object has no attribute 'version'")
    components = [x for x in _COMPONENT_RE.split(v) if x and x != "."]
    for i, obj in enumerate(components):
        try:
            components[i] = int(obj)
        except ValueError:
            pass
    return components


def supports(client_version, minimum="2.1"):
    return _version_key(client_version) >= _version_key(minimum)


def newest(versions):
    if not versions:
        return None
    return max(versions, key=_version_key)
