
n = int(input())
server_state = 0
player_state = 0
server_score = 0
player_score = 0
game = {}
for i in range(n):
    score = input().rpartition("-")
    if score[1] == "-" and score[0].isdigit() and score[2].isdigit():
        current_round_server = int(score[0])
        current_round_player = int(score[2])
        if current_round_server != server_state:
            server_state = current_round_server
            server_score += 1
        if current_round_player != player_state:
            player_state = current_round_player
            player_score += 1
    elif score[1] == "-" and score[2] == 'in':
        server_state = 45
        server_score += 1
    elif score[1] == "-" and score[2] == 'out':
        player_state = 45
        player_score += 1
    elif score[2] == 'game':
        if server_state > player_state:
            server_score += 1
        else:
            player_score += 1
    elif score[2] == 'deuce':
        if server_state > player_state:
            player_state = 40
            server_state = 40
            player_score += 1
        else:
            server_state = 40
            player_state = 40
            server_score += 1

print(server_score, '-', player_score)


# Line 1: integer n for the number of points played
# Next n lines: current score of the game. It is either 0, 15,30 or 40 separated by a dash, or a text value of game, deuce, ad-in or ad-out
# Output
# The final points for each player, separated by a dash
# Constraints
# 4 <= n < 1000
#
#
#
#
# 4
# 15-0
# 30-0
# 40-0
# game
#
#
#
#
# 8
# 15-0
# 30-0
# 40-0
# 40-15
# 40-30
# deuce
# ad-in
# game
# 5-3
#
#
# 8
# 15-0
# 30-0
# 40-0
# 40-15
# 40-30
# deuce
# ad-out
# game
#
# 3-5
#
# 10
# 15-0
# 30-0
# 40-0
# 40-15
# 40-30
# deuce
# ad-out
# deuce
# ad-out
# game
#
# 3-5