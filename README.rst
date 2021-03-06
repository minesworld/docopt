Goal of this fork:

- Fix the broken (as of 0.6.2)  "--" separator usages like

    test <a> [<b>...] -- <c> [<d>...]

    test <a> (-- <c> [<d>...])...

    test [--opt1] <a> -- [--opt2] <b>

    test [--opt1] <a> -- [--opt1] <a>


- Fix the broken (as of 0.6.2) last repeating argument usage like

    test <a> [<b>...]

  which failed when called as

    test a b -b

Solution:

- added usage parameter to docopt function. If given this string will be presented to the user instead of
  the doc string.

- added separated_args() and merged_args() functions to ease coding the workaround

- added docopt leftover optional argument specifing the key into which all non parsable leftover arguments
  should be collected into.


Implementation to get "test <a> [<b>...] -- <c> [<d>...]" working:

.. code:: python
  __doc__ = """test
  Usage:
    test <a> [<b>...] -- <c> [<d>...]
  """

- Build a new __usage__ string by splitting each command which use the "--" separator into two commands.

  One which includes all parameters up to "--" separator. If the argument before the separator was not repeatable
  make it repeatable by adding "...".
  An additional which uses an internal non-optional argument and the rest of the original arguments after
  the separator.

  Move the new internal command before other existing command as it might have the same syntax.

.. code:: python
  __doc__ = """test
  Usage:
    test <a> [<b>...] -- <c> [<d>...]
  """

  __usage__ = """test
  Usage:
    test internal <c> [<d>...]
    test <a> [<b>...]
  """

- Call docopt() with the new usage parameter

.. code:: python
  args = docopt.docopt(__doc__, usage=__usage__)

- process the additional arguments by calling docopt again but this time use the internal non-optional argument.

.. code:: python
  args, sargs = docopt.separated_args(args, "<b>")
  if sargs:
      args = docopt.merged_args(args, docopt.docopt(__doc__, argv=[ "internal" ] + sargs, usage=__usage__))

- It is possible to repeat this in case multiple separators are needed. By leaving the docopt function "as is"
  everybody is free to implement the logic to collect the arguments after the separator. Some might want to
  put the resulting dict into a "--" key of the first pass or even a list of dicts when multiple separators are
  in use...


Attention to detail and different implementations:

- Take a look at all source files within examples/separator-workarounds folder.


Thanks:

- To Vladimir Keleshev for the original idea and project.
- The Python community in general.
