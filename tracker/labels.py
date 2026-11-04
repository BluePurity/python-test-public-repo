"""Label and command formatting. Legacy: locale.format (removed 3.12), pipes.quote (removed 3.13)."""
import locale
import pipes


def weight_label(kg):
    return locale.format("%.1f", kg) + " kg"


def price_label(amount):
    return "GBP " + locale.format("%.2f", amount, grouping=True)


def print_command(printer, label_file):
    return "lp -d %s %s" % (pipes.quote(printer), pipes.quote(label_file))
