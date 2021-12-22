from collections import namedtuple


Point = namedtuple("MyPoint", "x y")
my_list = []
with open("test_file") as f:
    my_list = [Point._make(x.strip().split()) for x in f.readlines()]
    for p in my_list:
        print(getattr(p, "x"))


