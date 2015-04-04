from docopt import docopt, separated_args, merged_args

__doc__ = """extra-usage-example
Usage:
  extra-usage-example internal <b> [<c>...]
  extra-usage-example <a>...
  extra-usage-example (-h|--help)
"""

__usage__ = """extra-usage-example
Usage:
  extra-usage-example <a> (-- <b> [<c>...])...
  extra-usage-example (-h|--help)
"""

args = docopt(__doc__, usage=__usage__)

print("before workaround:", args)
print()

# the end-user __usage__ has <a> as a non-repeating argument
# but the workaround __doc__ must use <a> as a repeating argument
# by using unlist=True the args dict will contain a scalar value as specified by __usage__

args, oargs = separated_args(args, "<a>", unlist=True)


# as (<b> [<c>...])... is repeatable we have to collect the results
# a simply way is to put the result items into a list of dicts which can be accessed by the separator as key
# to do this use the collect keyword passing a list of keys specifying the items to move into a dict per call

if oargs:
    args = merged_args(args, docopt(__doc__, argv=[ "internal" ] + oargs, usage=__usage__))

    while True:
        args, oargs = separated_args(args, "<c>", collect=["<b>", "<c>"])
        if not oargs:
            break
        args = merged_args(args, docopt(__doc__, argv=[ "internal" ] + oargs, usage=__usage__))

else:

    # handle special case where only <a> might be given
    # remove "<b>":None, "<c>":[] from args dict by "collecting" them into an empty list as the separators value
    # this way the args dict always contain a list as the separators value

    args, oargs = separated_args(args, "<c>",  collect=["<b>", "<c>"])


print("after workaround:", args)

