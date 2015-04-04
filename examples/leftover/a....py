from docopt import docopt

__doc__ = """extra-usage-example
Usage:
  extra-usage-example <a> [<b>...]
  extra-usage-example (-h|--help)
"""


# NOTE: this works also when [<b>...] is something like "a b -d -f d"

args = docopt(__doc__, usage=__usage__, leftover="<b>")

print(args)
