from docopt import docopt, separated_args, merged_args

__doc__ = """extra-usage-example
Usage:
  extra-usage-example internal [--opt2] <b>
  extra-usage-example [--opt1] <a>...
  extra-usage-example (-h|--help)
"""

__usage__ = """extra-usage-example
Usage:
  extra-usage-example [--opt1] <a> -- [--opt2] <b>
  extra-usage-example (-h|--help)
"""

args = docopt(__doc__, usage=__usage__)

print("before workaround:", args)
print()

args, oargs = separated_args(args, "<a>")
if oargs:
    args = merged_args(args, docopt(__doc__, argv=[ "internal" ] + oargs, usage=__usage__))

print("after workaround:", args)

