from tracker.labels import price_label, print_command, weight_label


def test_labels():
    assert weight_label(2.25) == "2.2 kg"
    assert price_label(1234.5) == "GBP 1234.50"
    assert print_command("office 1", "a b.pdf") == "lp -d 'office 1' 'a b.pdf'"
