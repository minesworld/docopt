from docopt import docopt, separated_args, merged_args

__doc__ = """extra-usage-example
Usage:
  extra-usage-example internal [--opt1] <a>
  extra-usage-example [--opt1] <a>...
  extra-usage-example (-h|--help)
"""

__usage__ = """extra-usage-example
Usage:
  extra-usage-example [--opt1] <a> -- [--opt1] <a>
  extra-usage-example (-h|--help)
"""

for x in (1, 2):

    args = docopt(__doc__, usage=__usage__)

    print("before workaround", x, ":", args)
    print()

    # the end-user __usage__ has <a> as a non-repeating argument
    # but the workaround __doc__ must use <a> as a repeating argument
    # by using unlist=True the args dict will contain a scalar value as specified by __usage__

    # as [--opt1] <a> is used a second time after the "--" separator we have to collect the results
    # a simply way is to put the result items into a list of dicts which can be accessed by the separator as key
    # to do this use the collect keyword passing a list of keys specifying the items to move into a dict per call

    args, oargs = separated_args(args, "<a>", unlist=True, collect=["--opt1", "<a>"])

    if x:
        args = merged_args(args, docopt(__doc__, argv=[ "internal" ] + oargs, usage=__usage__))

        # make sure the "--opt1" "<a>" items are moved into a dict within the separators list
        # unlist needed here as the parser got "confused" and args["<a>"] is a list...

        args, oargs = separated_args(args, "<a>", unlist=True, collect=["--opt1", "<a>"])

    else:

        # now use a different strategy: use the only possible usage so the parser doesn't get confused
        # args["<a>"] is a str and unlist is not needed...

        args = merged_args(args, docopt("usage: t [--opt1] <a>", argv=oargs, usage=__usage__))
        args, oargs = separated_args(args, "<a>", collect=["--opt1", "<a>"])

    print("after workaround", x, ":", args)

