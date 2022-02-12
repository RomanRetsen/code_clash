'''
Fail while daring greatly
def josephus(n, k):
The ancient world of swords and sandals “🎶 when men were made of iron and their ships were
made of wood 🎶 ” could occasionally also be an entertainingly violent place, at least according to
popular historical docudramas such as “300”, “Spartacus” and “Rome”. During one particularly
memorable incident, a group of zealots (yes, Lana, literally) found themselves surrounded by
overwhelming Roman forces. To avoid capture and arduous death by cruci ixion, in their righteous
zeal these men committed themselves to mass suicide in a way that ensured each man’s unwavering
commitment to this shared fate. They arranged themselves in a circle, and used lots to choose a step
size k. Then repeatedly count k men ahead, kill him and remove his corpse from this grim circle.
Being normal people instead of computer scientists, this deadly game of eeny-meeny-miney-moe is
one-based, and continues until the last man standing falls on his own sword to complete the circle.
Josephus would very much prefer to be this last man, since he has other ideas of surviving. Help him
survive with a function that, given n and k, returns the list of the execution order so that these men
know which places let them be the survivors who get to walk away from this grim circle. A cute
mathematical solution instantly determines the survivor for k = 2. Unfortunately k can get
arbitrarily large, even far exceeding the current number of men... if only to brie ly excite us cold and
timid souls, hollow men without chests, the rictus of our black lips gaped in grimace that sneers at
the strong men who once stumbled. (If only to lighten up this hammy lament, note the feline
generalization of this problem that practically begs to be turned into an adorable viral video.)
Expected result
4 1 [1, 2, 3, 4]

4 2 [2, 4, 3, 1]

10 3 [3, 6, 9, 2, 7, 1, 8, 5, 10, 4]

8 7 [7, 6, 8, 2, 5, 1, 3, 4]

30 4 [4, 8, 12, 16, 20, 24, 28, 2, 7, 13, 18, 23,
29, 5, 11, 19, 26, 3, 14, 22, 1, 15, 27, 10,
30, 21, 17, 25, 9, 6]

10 10**100 [10, 1, 9, 5, 2, 8, 7, 3, 6, 4]
'''

from collections import deque

def josephus(n, k):
    return_sequence = []
    # zealot_circle = deque(range(1, n + 1), maxlen=n)
    zealot_circle = list(range(1, n + 1))
    for i in range(n):
        killed = (k - 1) % len(zealot_circle)
        return_sequence.append(zealot_circle[killed])
        left_side = zealot_circle[killed + 1:]
        right_side = zealot_circle[:killed]
        zealot_circle = left_side + right_side
    return return_sequence

# n = 30
# k = 4
# n = 4
# k = 2
n = 10
k = 10 ** 100
print(josephus(n, k))
