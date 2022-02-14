'''
Crack the crag
def crag_score(dice):
Crag is an old dice game similar to the more popular games of Yahtzee and Poker dice in style and
spirit, but with much simpler combinatorics of roll value calculation due to this game using only
three dice. Players repeatedly roll three dice and assign the resulting patterns to scoring categories
so that once some roll has been assigned to a category, that category is considered to have been
spent and cannot be used again for any future roll. These tactical choices between safety and risk-
taking give this game a more tactical lair on top of merely relying on the favours of Lady Luck for
rolling the bones. See the Wikipedia page for the scoring table used in this problem.
Given the list of pips of the three dice of the irst roll, this function should return the highest
possible score available when all categories of the scoring table are still available for you to
choose from, so that all that matters is maximizing this irst roll. Note that the examples on the
Wikipedia page show the score that some dice would score in that particular category, which is
not necessarily even close to the maximum score in principle attainable with that roll. For example,
the roll [1, 1, 1] used inef iciently in the category “Ones” would indeed score only three points,
whereas the same roll scores a whopping 25 points in the harder category “Three of a kind”. (The
problem “Optimal crag score” near the end of this collection has you distribute a slew of these rolls
into distinct categories to maximize the total score.)
This problem ought to be a straightforward exercise on if-else ladders combined with simple
sequence management. Your function should be swift and sure to return the correct answer for
every one of the 6 3 = 216 possible pip combinations. However, you will surely design your
conditional statements to handle entire equivalence classes of pip combinations in a single step, so
that your entire ladder consists of far fewer than 216 separate steps.
[1, 2, 3] 20
[4, 5, 1] 5
[3, 3, 3] 25
[4, 5, 4] 50
[1, 1, 1] 25
[1, 1, 2] 2
'''
from itertools import product

def generate_all_categories():
    all_categories = {(1, 50): set(), (2, 26): set(), (3, 25): set(), \
                      (4, 20):set(), (5, 20):set(), (6, 20):set(), (7, 20): set(), \
                      (8, 18): set(), (9, 12): set(), (10, 6): set(), \
                      (11, 15): set(), (12, 10): set(), (13, 5): set(), \
                      (14, 12): set(), (15, 8): set(), (16, 4): set(), \
                      (17, 9): set(), (18, 6): set(), (19, 3): set(), \
                      (20, 6): set(), (21, 4): set(), (22, 2): set(), \
                      (23, 3): set(), (24, 2): set(), (25, 1): set()
                      }
    for comb in product([1,2,3,4,5,6], repeat=3):
        sorted_comb = tuple(sorted(comb))
        if sum(comb) == 13:
            if len(set(comb)) == 2:
                all_categories[(1,50)].add(sorted_comb)
            all_categories[(2, 26)].add(sorted_comb)
        if len(set(comb)) == 1:
                all_categories[(3, 25)].add(sorted_comb)
        if sorted_comb == (1,2,3):
            all_categories[(4, 20)].add(sorted_comb)
        if sorted_comb == (4,5,6):
            all_categories[(5, 20)].add(sorted_comb)
        if sorted_comb == (1,3,5):
            all_categories[(6, 20)].add(sorted_comb)
        if sorted_comb == (2,4,6):
            all_categories[(7, 20)].add(sorted_comb)
        if sorted_comb.count(6) == 3:
            all_categories[(8, 18)].add(sorted_comb)
        elif sorted_comb.count(6) == 2:
            all_categories[(9, 12)].add(sorted_comb)
        elif sorted_comb.count(6) == 1:
            all_categories[(10, 6)].add(sorted_comb)
        if sorted_comb.count(5) == 3:
            all_categories[(11, 15)].add(sorted_comb)
        elif sorted_comb.count(5) == 2:
            all_categories[(12, 10)].add(sorted_comb)
        elif sorted_comb.count(5) == 1:
            all_categories[(13, 5)].add(sorted_comb)
        if sorted_comb.count(4) == 3:
            all_categories[(14, 12)].add(sorted_comb)
        elif sorted_comb.count(4) == 2:
            all_categories[(15, 8)].add(sorted_comb)
        elif sorted_comb.count(4) == 1:
            all_categories[(16, 4)].add(sorted_comb)
        if sorted_comb.count(3) == 3:
            all_categories[(17, 9)].add(sorted_comb)
        elif sorted_comb.count(3) == 2:
            all_categories[(18, 6)].add(sorted_comb)
        elif sorted_comb.count(3) == 1:
            all_categories[(19, 3)].add(sorted_comb)
        if sorted_comb.count(2) == 3:
            all_categories[(20, 6)].add(sorted_comb)
        elif sorted_comb.count(2) == 2:
            all_categories[(21, 4)].add(sorted_comb)
        elif sorted_comb.count(2) == 1:
            all_categories[(22, 2)].add(sorted_comb)
        if sorted_comb.count(1) == 3:
            all_categories[(23, 3)].add(sorted_comb)
        elif sorted_comb.count(1) == 2:
            all_categories[(24, 2)].add(sorted_comb)
        elif sorted_comb.count(1) == 1:
            all_categories[(25, 1)].add(sorted_comb)

    return all_categories


def crag_score(dice):
    sorted_dice = tuple(sorted(dice))
    for category_result, category_combinations \
            in sorted(generate_all_categories().items(), key=lambda x:x[0][1], reverse=True):
        if sorted_dice in category_combinations:
            return category_result[1]
    else:
        return 0


# the_combination = [1,2,3]
# the_combination = [4, 5, 1]
# the_combination = [3,3,3]
# the_combination = [4, 5, 4]
# the_combination = [1,1,1]
the_combination = [1,1,2]
print(crag_score(the_combination))






