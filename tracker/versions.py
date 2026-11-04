"""API version negotiation. Legacy: distutils.version.LooseVersion (removed 3.12)."""
from distutils.version import LooseVersion


def supports(client_version, minimum="2.1"):
    return LooseVersion(client_version) >= LooseVersion(minimum)


def newest(versions):
    if not versions:
        return None
    return max(versions, key=LooseVersion)
