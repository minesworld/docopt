from docopt import separated_args, merged_args, Skip, Overwrite, Collect, enlist_args


d1 = { 'x': 'a' }
d2 = { 'x': 'b' }

print("d1 =", d1)
print("d2 =", d2)
print()
print("merged_args(d1, d2, mode=Skip) :", merged_args(d1, d2, mode=Skip))
print("merged_args(d1, d2, mode=Overwrite) :", merged_args(d1, d2, mode=Overwrite))
print("merged_args(d1, d2, mode=Collect) :", merged_args(d1, d2, mode=Collect))

print()
print()

d = { 'x': [ '1', '2'], 'y' : [ 's -p 10 x' ], 'z' : None }
print ("d =", d)
print()
print("enlist_args(d, 'x', 'y', 'z') :", enlist_args(d, 'x', 'y', 'z'))
print("enlist_args(d, 'x', 'y', 'z', separator='-') :", enlist_args(d, 'x', 'y', 'z', separator='-'))
