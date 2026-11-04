"""Event hooks. Legacy: inspect.getargspec (removed 3.11)."""
import inspect


def hook_signature(fn):
    spec = inspect.getargspec(fn)
    return {"args": spec.args, "varargs": spec.varargs, "keywords": spec.keywords,
            "defaults": list(spec.defaults or ())}


def wants_context(fn):
    return "context" in inspect.getargspec(fn).args
