from docopt import docopt, separated_args, merged_args, Skip, Overwrite, Collect

__doc__ = """extra-usage-example
Usage:
  extra-usage-example internal <c> [<d>...]
  extra-usage-example <a> [<b>...]
  extra-usage-example (-h|--help)
"""

__usage__ = """extra-usage-example
Usage:
  extra-usage-example <a> [<b>...] -- <c> [<d>...]
  extra-usage-example (-h|--help)
"""

args = docopt(__doc__, usage=__usage__)

print("before workaround:", args)
print()

args, oargs = separated_args(args, "<b>")
if oargs:
    args = merged_args(args, docopt(__doc__, argv=[ "internal" ] + oargs, usage=__usage__))

print("after workaround:", args)

