# Imagine we could fold a piece of paper infinite times. How wonderful would it be to build anything with just paper! In our case, we will build a thick block of paper. How creative of us!
#
# Given a single piece of paper having a thickness of T m, we need to find out how many times we need to fold it in half to build a block of height H m.
#
# Basically, by folding a piece of paper in half, we make it higher, eg. when you fold a paper of thickness 0.004 m, it becomes 0.008 m high.
#
# We also need to reach a certain width W, because a very thin block would be unusable for anything!
# When we fold only in one axis, length of our paper will remain unchanged, but width will be halved with each fold, eg. when you fold paper of width 1 m, it becomes 0.5 m wide.
#
# You also need to calculate how wide our sheet of paper has to be to reach a certain width after folding (the starting width).
#
# The goal here is to compute the number of folds required, and the required width of the unfolded piece of paper.
#
# Imagine what we could use that block for... A bridge, a house, anything your imagination desires!
# Input
# Space separated values: T H W
#
# T - thickness of used sheet of paper (floating)
# H - minimum desired height (int)
# W - desired width (int)
# Output
# In separate lines write the following integer results:
#
# fold_count - how many times we need to fold the paper to achieve desired block height
# starting_width - how wide this sheet of paper has to be to achieve desired width
# Constraints
# 0 < T < 1
# 0 < H ≤ 500
# 0 < W ≤ 200
# 0.004 100 12
#
# 15
# 393216
#

def folds(initial, final, counter):
    if initial < final:
        counter += 1
        return folds(initial*2, final, counter)
    return counter

inputs = input().split()
t = float(inputs[0])
h = int(inputs[1])
w = int(inputs[2])


result = folds(t, h, 0)
print(f'{result} {12*(2**result)}')
