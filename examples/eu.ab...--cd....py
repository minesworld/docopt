from docopt import docopt

__doc__ = """extra-usage-example
Usage:
  extra-usage-example internal <c> [<d>...]
  extra-usage-example <a> [<b>...]
"""


__usage__ = """extra-usage-example
Usage:
  extra-usage-example <a> [<b>...] -- <c> [<d>...]
"""


def separated_args(args, key, separator="--"):
    args = dict(args)

    if None is args[key] or not separator in args[key]:
        return args, []

    index = args[key].index(separator)
    args[key], optionalargs = args[key][:index], args[key][index + 1:]

    return args, optionalargs


Skip=1
Overwrite=2
Collect=3

def merged_args(args, optargs, mode=Skip):
    args = dict(args)

    for key in optargs.keys():
        if None is optargs[key]:
            continue
        if args[key]:
            if Skip == mode:
                continue
            elif Overwrite == mode:
                args[key] = optargs[key]
            elif Collect == mode:
                if not isinstance(args[key], list):
                    args[key] = [ args[key], optargs[key] ]
                else:
                    args[key] = args[key].append(optargs[key])
        else:
            args[key] = optargs[key]

    return args


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