'''
Optimal crag score
def optimal_crag_score(rolls):
An earlier problem asked you to compute the best possible score for a single roll in the dice game of
crag. In this problem, the game is played for multiple rolls, again aided with the same gift of perfect
foresight as in the previous “Lords of Midnight” problem. Given the entire sequence of rolls, this
function should return the highest possible score that can be achieved with those rolls under the
constraint that the same category cannot be used more than once, as is dictated by the rules of
the actual game of crag the same way as in the more famous dice game of Yahtzee.
The greedy algorithm “sort the rolls in the descending order of their maximum possible individual
score, and then use each roll for its highest scoring remaining category” does not work here, since
several rolls might it in the same category, and yet are not equally good choices with respect to the
remaining categories. Therefore, you need to process the list of rolls recursively, each level of
recursion assigning some still unused category to the current roll. For each such category,
recursively compute the best possible way to assign unused categories to the remaining rolls. The
best category for the current roll is then the one that maximizes the sum of the value for the current
roll and this recursively computed solution for the remaining rolls.
rolls Expected result
To speed up this recursion, you can keep track of the best solution that you have found so far. When
the current branch of the recursive search has a chance of beating that best solution, you can treat
the current branch as having a solution, as there is no point wasting perfectly good processor cycles
computing the exact value of something that cannot affect the inal answer.
[(1, 6, 6), (2, 5, 6), (4, 5, 6), (2, 3, 5)] 101
[(3, 1, 2), (1, 4, 2)] 24
[(5, 1, 1), (3, 5, 2), (2, 3, 2), (4, 3, 6),
(6, 4, 6), (4, 5, 2), (6, 4, 5)] 74
[(3, 1, 2), (1, 4, 2), (5, 2, 3), (5, 5, 3),
(2, 6, 3), (1, 1, 1), (5, 2, 5)] 118
[(1, 5, 1), (5, 5, 6), (3, 2, 4), (4, 6, 1),
(4, 4, 1), (3, 2, 4), (3, 4, 5), (1, 2, 2)] 33
'''

from itertools import product
from collections import deque

def generate_all_categories():
    all_categories = {(1, 50): [0, set()], (2, 26): [0, set()], (3, 25): [0, set()], \
                      (4, 20):[0, set()], (5, 20):[0, set()], (6, 20):[0, set()], (7, 20): [0, set()], \
                      (8, 18): [0, set()], (9, 12): [0, set()], (10, 6): [0, set()], \
                      (11, 15): [0,set()], (12, 10): [0,set()], (13, 5): [0,set()], \
                      (14, 12): [0,set()], (15, 8): [0,set()], (16, 4): [0,set()], \
                      (17, 9): [0,set()], (18, 6): [0,set()], (19, 3): [0,set()], \
                      (20, 6): [0,set()], (21, 4): [0,set()], (22, 2): [0,set()], \
                      (23, 3): [0,set()], (24, 2): [0,set()], (25, 1): [0,set()]
                      }
    for comb in product([1,2,3,4,5,6], repeat=3):
        sorted_comb = tuple(sorted(comb))
        if sum(comb) == 13:
            if len(set(comb)) == 2:
                all_categories[(1,50)][1].add(sorted_comb)
            all_categories[(2, 26)][1].add(sorted_comb)
        if len(set(comb)) == 1:
                all_categories[(3, 25)][1].add(sorted_comb)
        if sorted_comb == (1,2,3):
            all_categories[(4, 20)][1].add(sorted_comb)
        if sorted_comb == (4,5,6):
            all_categories[(5, 20)][1].add(sorted_comb)
        if sorted_comb == (1,3,5):
            all_categories[(6, 20)][1].add(sorted_comb)
        if sorted_comb == (2,4,6):
            all_categories[(7, 20)][1].add(sorted_comb)
        if sorted_comb.count(6) == 3:
            all_categories[(8, 18)][1].add(sorted_comb)
        elif sorted_comb.count(6) == 2:
            all_categories[(9, 12)][1].add(sorted_comb)
        elif sorted_comb.count(6) == 1:
            all_categories[(10, 6)][1].add(sorted_comb)
        if sorted_comb.count(5) == 3:
            all_categories[(11, 15)][1].add(sorted_comb)
        elif sorted_comb.count(5) == 2:
            all_categories[(12, 10)][1].add(sorted_comb)
        elif sorted_comb.count(5) == 1:
            all_categories[(13, 5)][1].add(sorted_comb)
        if sorted_comb.count(4) == 3:
            all_categories[(14, 12)][1].add(sorted_comb)
        elif sorted_comb.count(4) == 2:
            all_categories[(15, 8)][1].add(sorted_comb)
        elif sorted_comb.count(4) == 1:
            all_categories[(16, 4)][1].add(sorted_comb)
        if sorted_comb.count(3) == 3:
            all_categories[(17, 9)][1].add(sorted_comb)
        elif sorted_comb.count(3) == 2:
            all_categories[(18, 6)][1].add(sorted_comb)
        elif sorted_comb.count(3) == 1:
            all_categories[(19, 3)][1].add(sorted_comb)
        if sorted_comb.count(2) == 3:
            all_categories[(20, 6)][1].add(sorted_comb)
        elif sorted_comb.count(2) == 2:
            all_categories[(21, 4)][1].add(sorted_comb)
        elif sorted_comb.count(2) == 1:
            all_categories[(22, 2)][1].add(sorted_comb)
        if sorted_comb.count(1) == 3:
            all_categories[(23, 3)][1].add(sorted_comb)
        elif sorted_comb.count(1) == 2:
            all_categories[(24, 2)][1].add(sorted_comb)
        elif sorted_comb.count(1) == 1:
            all_categories[(25, 1)][1].add(sorted_comb)

    return all_categories


def crag_score(dice, category_card):
    sorted_dice = tuple(sorted(dice))
    for category_result, category_combinations \
            in sorted([(x,y) for x,y in category_card.items() if y[0] == 0], key=lambda x:x[0][1], reverse=True):
        if sorted_dice in category_combinations[1]:
            # category_card[category_result][0] == 1
            return category_result[1]
    else:
        return 0

def find_best_score(rolls, category_card, score):
    print(rolls)
    if len(rolls) == 0:
        return score
    current = tuple(sorted(rolls.popleft()))
    round_max = -1
    the_key = None
    print(category_card)
    for category_result, category_combinations \
            in sorted([(x, y) for x, y in category_card.items() if y[0] == 0], key=lambda x: x[0][1], reverse=True):
        if current in category_combinations[1]:
            to_change = round_max
            round_max = max(round_max, find_best_score(rolls, category_card, score + category_result[1]))
            if round_max > to_change:
                the_key = category_result
    print(f"the key {the_key}")
    category_card[the_key][0] = 1
    print(f"in {category_card}")
    return round_max

def score_backup(rolls, category_card, score):
    print(rolls)
    if len(rolls) == 0:
        return 0
        # return crag_score(rolls[0], category_card)
    current = tuple(sorted(rolls.popleft()))
    round_max = score
    for category_result, category_combinations \
            in sorted([(x, y) for x, y in category_card.items() if y[0] == 0], key=lambda x: x[0][1], reverse=True):
        round_max = max(round_max, find_best_score(rolls, category_card, score ))
        if current in category_combinations[1] and score + category_result[1] > round_max:
            category_card[category_result][0] = 1
            round_max = score + category_result[1]
    # return round_max + find_best_score(rolls, category_card, score + round_max)
    return round_max

def optimal_crag_score(rolls):
    category_card = generate_all_categories()
    rolls_like_deque = deque(rolls)
    return find_best_score(rolls_like_deque, category_card, 0)

# rolls = [(5, 1, 1), (3, 5, 2), (2, 3, 2), (4, 3, 6), \
#          (6, 4, 6), (4, 5, 2), (6, 4, 5)]
# rolls = [(3, 1, 2), (1, 4, 2), (5, 2, 3), (5, 5, 3), \
#          (2, 6, 3), (1, 1, 1), (5, 2, 5)]
# rolls = [(1, 5, 1), (5, 5, 6), (3, 2, 4), (4, 6, 1), \
#          (4, 4, 1), (3, 2, 4), (3, 4, 5), (1, 2, 2)]
# rolls = [(1, 6, 6), (2, 5, 6), (4, 5, 6), (2, 3, 5)]
# rolls = [(3, 1, 2), (1, 4, 2)]
# rolls = [(3, 1, 2)]
rolls = [ (1, 6, 6), (3, 5, 5)]

print(optimal_crag_score(rolls))








