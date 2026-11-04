"""Event hooks. Legacy: inspect.getargspec (removed 3.11)."""
import inspect


def hook_signature(fn):
    spec = inspect.getfullargspec(fn)
    return {"args": spec.args, "varargs": spec.varargs, "keywords": spec.varkw,
            "defaults": list(spec.defaults or ())}


def wants_context(fn):
    return "context" in inspect.getfullargspec(fn).args
