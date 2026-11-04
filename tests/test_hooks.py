from tracker.hooks import hook_signature, wants_context


def on_event(event, context=None, *extra, **opts):
    return event


def test_hook_signature():
    assert hook_signature(on_event) == {"args": ["event", "context"], "varargs": "extra",
                                        "keywords": "opts", "defaults": [None]}
    assert wants_context(on_event) and not wants_context(lambda e: e)
