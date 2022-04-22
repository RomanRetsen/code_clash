'''
A chess board is a square of 8x8 cells, with rows marked by numbers (1-8) and columns marked by letters (a-h). A cell is identified by a pair of letter and number (e.g. f1, c4).


   _______________
8 |_|#|_|#|_|#|_|#|
7 |#|_|#|_|#|_|#|_|
6 |_|#|_|#|_|#|_|#|
5 |#|_|#|_|#|_|#|_|
4 |_|#|_|#|_|#|_|#|
3 |#|_|#|_|#|_|#|_|
2 |_|#|_|#|_|#|_|#|
1 |#|_|#|_|#|_|#|_|
   a b c d e f g h



A queen can attack an opponent located in any cells horizontally, vertically and diagonally from queen's position.

Given the positions of the queen and the opponent print the distance (opponent is how many cells away from the Queen) between them if the queen can attack otherwise print CANNOT ATTACK.

Example

Queen position: b4
Opponent position: e1

In this case Queen can attack the opponent and opponent is 3 cells away from the Queen.

Note: The distance is also called Chebyshev distance.
https://en.wikipedia.org/wiki/Chebyshev_distance
Input
Queen and opponent positions separated by space.
Output
Print distance if queen can attack otherwise print CANNOT ATTACK.
Constraints
Example
Input

c5 c8

Output

3

------------test2


a5 d7

CANNOT ATTACK

-------------test3


b4 g4

5
--------------test4


g8 a3

CANNOT ATTACK
--------------test5


b4 e1

3
-------------test6


g3 d6

3

'''
queen, you = input().split()

letters = {x:y for x, y in zip("abcdefgh", range(8))}
board = [[0 for _ in range(8)] for _ in range(8)]

for i in range(8):
    board[i][letters[queen[0]]] = 1
for i in range(7, -1, -1):
    board[8 - int(queen[1])][i] = 1
for i in range(letters[queen[0]] - 1, -1, -1):
    diag = 8 - int(queen[1])
    adj = letters[queen[0]] - i
    if diag - adj >= 0 and diag - adj <= 7:
        board[diag - adj][i] = 1
    if diag + adj >= 0 and diag + adj <= 7:
        board[diag + adj][i] = 1
for i in range(letters[queen[0]] + 1, 8):
    diag = 8 - int(queen[1])
    adj = letters[queen[0]] - i
    if diag - adj >= 0 and diag - adj <= 7:
        board[diag - adj][i] = 1
    if diag + adj >= 0 and diag + adj <= 7:
        board[diag + adj][i] = 1

if board[8 - int(you[1])][letters[you[0]]] == 1:
    print(max(
        abs(int(you[1]) - int(queen[1])), \
            + abs(letters[you[0]] - letters[queen[0]])))
else:
    print("CANNOT ATTACK")