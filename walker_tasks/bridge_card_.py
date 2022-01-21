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
    return max(r, key=lambda x:(x[0], ranks[r[1]]))



ranks = {"two": 1,"three":2, "four": 3,"five": 4, "six": 5, "seven": 6,
         "eight": 7, "nine": 8, "ten": 9, "jack": 10, "queen": 11, "king": 12, "ace": 12}
suits = {"spades", "diamonds", "hearts", "clubs"}

input_list = []
for _ in range(4):
    input_list.append(tuple(input().split()))
print(f"input_list {input_list}" )
print(winning_card(input_list))