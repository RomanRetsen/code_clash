'''
The card that wins the trick
def winning_card(cards, trump=None):
Playing cards are again represented as tuples of (rank,suit) as in the cardproblems.py
lecture example program. In trick taking games such as whist or bridge, four players each play
one card from their hand to the trick, committing to their play in clockwise order starting from the
player who plays irst into the trick. The winner of the trick is determined by the following rules:
1. If one or more cards of the trump suit have been played to the trick, the trick is won by the
highest ranking trump card, regardless of the other cards played.
2. If no trump cards have been played to the trick, the trick is won by the highest card of the
suit of the irst card played to the trick. Cards of any other suits, regardless of their rank, are
powerless to win that trick.
3. Ace is the highest card in each suit.
Note that the order in which the cards are played to the trick greatly affects the outcome of that
trick, since the irst card played in the trick determines which suits have the potential to win the
trick in the irst place. Return the winning card for the list of cards played to the trick.
cards trump Expected result

three spades
ace diamonds
jack spades
eight spades

output
jack, spades

-----------------------test2


ace diamonds
ace hearts
ace spades
two clubs

output

two, clubs

-----------------

two clubs
ace diamonds
ace hearts
ace spades

output

('two', 'clubs')
'''
def winning_card(cards, trump=None):
    r = []
    if trump:
        for card in cards:
            if card[1] == trump:
                r.append((1, card[0], card[1]))
            else:
                r.append((0, card[0], card[1]))
    else:
        trump = cards[0][1]
        for card in cards:
            if card[1] == trump:
                r.append((1, card[0], card[1]))
            else:
                r.append((0, card[0], card[1]))
    return max((r), key=lambda x:(x[0], ranks[x[1]]))[1:]

ranks = {
    "two": 1, "three":2, "four": 3, "five": 4, "six": 5, "seven": 6,
    "eight": 7, "nine": 8, "ten": 9, "jack": 10, "queen": 11, "king": 12, "ace": 12
         }
suits = ("spades", "diamonds", "hearts", "clubs")

input_list = []
for _ in range(4):
    input_list.append(tuple(input().split()))
trump = input()
if trump in suits:
    print(winning_card(input_list, trump=trump))
else:
    print(winning_card(input_list, trump=None))