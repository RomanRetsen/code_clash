"""
Lords of Midnight
def midnight(dice):
Midnight is a dice game where the player initially rolls six dice, and must decide which dice to keep
and which to re-roll to maximize his inal score. However, all your hard work with the previous
problems has now mysteriously rewarded you with the gift of perfect foresight (as some wily
Frenchman might say, you might unknowingly be a descendant of Madame de Th bes) that allows
you to foresee what pip values each individual die will produce in its entire sequence of future rolls,
expressed as a sequence such as [2, 5, 5, 1, 6, 3]. Aided with this foresight, your task is to
return the maximum total score that could be achieved with the given dice rolls.
The argument dice is a list whose each element is a sequence of the pip values that particular die
will produce when rolled. (Since this game will necessarily end after at most six rolls, this given
future sequence needs to be only six elements long.) Note that the rules require you to keep at least
one die in each roll, which is why the trivial algorithm “First choose the two dice you use to get the 1
and 4, and add up the maximum pip values for the four remaining dice” does not work, as
demonstrated by the irst row of the following table. DUCY?
"""
from itertools import product

def not_skipped(the_combination):
    the_steps = sorted([step_index[0] for step_index in the_combination])
    current = the_steps[0]
    if not current == 0:
        return False
    for i in range(1, len(the_steps), 1):
        if the_steps[i] - current > 1:
            return False
        else:
            current = the_steps[i]
    else:
        return True

def midnight(inlist):
    enriched_list = [[(index, y) for index, y in enumerate(x)] for x in inlist]
    the_max = 0
    for comb in product(*enriched_list):
        if 1 in (x[1] for x in comb) \
                and 4 in (x[1] for x in comb) \
                and sum([x[1] for x in comb])-1-4 > the_max \
                and not_skipped(comb):
            the_max = sum([x[1] for x in comb])- 1 - 4
    return the_max

the_list = [[3, 4, 6, 6, 6, 2], [3, 2, 6, 2, 3, 3], [2, 2, 2, 2, 2, 3],
            [6, 1, 4, 2, 2, 2], [2, 2, 2, 3, 2, 3], [2, 3, 3, 3, 3, 2]] # 14
# the_list = [[2, 6, 2, 1, 3, 3], [2, 2, 2, 2, 2, 3], [2, 2, 4, 3, 6, 6],
#             [4, 5, 6, 3, 2, 5], [2, 4, 2, 6, 5, 3], [2, 2, 2, 2, 2, 3]] # 17
# the_list = [[2, 3, 5, 3, 2, 2], [1, 3, 2, 3, 6, 4], [3, 2, 3, 3, 3, 5],
#             [3, 6, 4, 6, 2, 3], [2, 3, 3, 2, 3, 2], [3, 5, 3, 5, 1, 2]] # 17
# the_list = [[2, 6, 2, 5, 2, 5], [5, 3, 3, 2, 5, 3], [2, 2, 2, 2, 5, 2],
#             [3, 6, 3, 2, 2, 5], [6, 2, 2, 6, 3, 2], [2, 2, 3, 2, 2, 2]] # 0
print(midnight(the_list))