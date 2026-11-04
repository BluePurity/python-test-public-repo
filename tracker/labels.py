"""Label and command formatting. Legacy: locale.format (removed 3.12), pipes.quote (removed 3.13)."""
import locale
import shlex


def weight_label(kg):
    return locale.format_string("%.1f", kg) + " kg"


def price_label(amount):
    return "GBP " + locale.format_string("%.2f", amount, grouping=True)


def print_command(printer, label_file):
    return "lp -d %s %s" % (shlex.quote(printer), shlex.quote(label_file))
