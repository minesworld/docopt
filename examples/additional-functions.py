from docopt import separated_args, merged_args, Skip, Overwrite, Collect


d1 = { 'x': 'a' }
d2 = { 'x': 'b' }

print("d1 =", d1)
print("d2 =", d2)
print()
print("merged_args(d1, d2, mode=Skip) :", merged_args(d1, d2, mode=Skip))
print("merged_args(d1, d2, mode=Overwrite) :", merged_args(d1, d2, mode=Overwrite))
print("merged_args(d1, d2, mode=Collect) :", merged_args(d1, d2, mode=Collect))
