from docopt import docopt, separated_args, merged_args, Skip, Overwrite, Collect

__doc__ = """extra-usage-example
Usage:
  extra-usage-example internal <c> [<d>...]
  extra-usage-example <a> [<b>...]
"""


__usage__ = """extra-usage-example
Usage:
  extra-usage-example <a> [<b>...] -- <c> [<d>...]
"""



args = docopt(__doc__, usage=__usage__)

print("unprocessed:", args)

args, oargs = separated_args(args, "<b>")
if oargs:
    args = merged_args(args, docopt(__doc__, argv=[ "internal" ] + oargs, usage=__usage__))

print("processed:", args)

print()

d1 = { 'x': 'a' }
d2 = { 'x': 'b' }

print(d1, d2)
print("Skip:", merged_args(d1, d2, mode=Skip))
print("Overwrite:", merged_args(d1, d2, mode=Overwrite))
print("Collect:", merged_args(d1, d2, mode=Collect))