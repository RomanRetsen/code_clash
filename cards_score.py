"""
The goal of the coder is to know the score of the hand,
either by getting three cards of the same rank (like 8s or Jacks)
or the same suit (like hearts(H) or spades(S)).

The value of your hand is calculated by adding up the total of your cards in any one suit
(and yes this is max value for just one of your suits).
Regular cards are worth their number, face cards (J, Q, K) are worth 10,
and Aces are worth 11, but remember, only one of your suits counts!
You can also make a hand of three cards with the same rank,
like 8-8-8 or J-J-J. "This is worth 30.5 points unless it is A-A-A, which is worth 32.

Take this example:
S8 S10 CA
Score values for each suit:
Spades: 8+10 = 18
Clubs: 11
Hearts and Diamonds: 0
Max of 18 S, 11 C, 0 H, 0 D is 18
So score is 18 here.

Take another one:
SJ S10 SA
Score values for each suit:
Spades: 10 (from the J) + 10 + 11 (from the A) = 31
Hearts and Diamonds and Clubs: 0
Max of 31 S, 11 C, 0 H, 0 D is 31
So score is 31 here.30.5
Input
First 3 lines: The cards shown (type first, then the number)
Output
The score of the hand
Constraints
Cards are of these suits: H-hearts, C-clubs, S-spades, and D-diamonds
Numbers are: 7, 8, 9, 10, J, Q, K, A
Example
Input

CA
D9
H8

Output

11


____test2___________

SJ
SQ
S8

28

_________test3______
DJ
CJ
HJ

30.5

____________test4_____----
DA
DK
DQ

31

__test5_________________


HA
CA
SA

32
__________test6
S10
C10
H10


30.5

"""

by_suit = {"C":[], "H":[], "S":[], "D":[]}
by_rank = {"7":[], "8":[], "9":[], "10":[], "J":[], "Q":[], "K":[], "A":[]}
f = lambda x:11 if x == "A" else 10 if x in "KJQ" else int(x)
by_rank_list = map(lambda x: 32 if x[0] == "A" and len(x[1]) == 3 else 30.5 if len(x[1]) == 3 else 0,
                   by_rank.items())
for i in range(3):
    card = input()
    by_suit[card[0]].append(f(card[1]))
    by_rank[card[1:]].append(card[0])
rank_max = max(by_rank_list)
suit_max = max([sum(x[1]) for x in by_suit.items()])
print(max(rank_max, suit_max))
