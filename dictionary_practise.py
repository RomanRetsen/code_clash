"""
Your goal is to merge two dictionaries into one dictionary with two maximum values.
Dictionaries will be given line by line with their KeyValue pair, separated by a semicolon.
The output dictionary can have a single value linked to a key, which means the second value can be empty.

The display of the output dictionary content must be printed line by line, each line displaying a pair content as :
Key: Value1 and Value2
If the Value2 doesn't exist, then your program shouldn't print the " and Value2"

The display order of the printed pairs is the same order as pairs were read.
Input
Line 1: An integer N1, the number of pairs in the first dictionary
N1 lines: The first dictionary given line by line as a pair, separated by a semicolon
Next line: An integer N2, the number of pairs in the second dictionary
N2 lines: The second dictionary given line by line as a pair, separated by a semicolon
Output
The content of the output dictionary.
Constraints
0 < N1 < 33
0 < N2 < 33
0 < Word length < 129
Example
Input

3
First item;Cola
Second item;Bread
Third item;Chocolate
2
First item;Water
Third item;Sugar cane

Output

First item: Cola and Water
Second item: Bread
Third item: Chocolate and Sugar cane

------------test2

3
Un;One
Quatro;Four
Cinco;Five
2
Dos;Two
Tres;Three

out:

Un: One
Quatro: Four
Cinco: Five
Dos: Two
Tres: Three
----------------------test3


3
Cute;Cat
Fatal;Shark
Curious;Bird
3
Fatal;Bear
Cute;Hamster
Curious;Meerkat


out:

Cute: Cat and Hamster
Fatal: Shark and Bear
Curious: Bird and Meerkat

---------------test4

6
Cheddar;5
Salad;1
Pasta;2
Milk;2
Water;6
LED;3
6
Cheddar;$2.50
Salad;$1.29
Pasta;$0.99
Milk;$1.39
Water;$0.79
LED;$9.59

out:

Cheddar: 5 and $2.50
Salad: 1 and $1.29
Pasta: 2 and $0.99
Milk: 2 and $1.39
Water: 6 and $0.79
LED: 3 and $9.59

----------------test5

12
Action;Wonder Woman
Crime;Night Call
Drama;Twelve Years a Slave
Adventure;Avatar
Ninja;Elektra
Fantasy;Black Panther
Horror;The Conjuring 2
Romance;Midnight Sun
Musical;High School Musical
Mystery;The Game
Disaster;Cloverfield
Pirate;Pirates of the Caribbean
9
Thriller;Inception
Action;Deadpool
Horror;Get Out
Sports;Invictus
Terrorism;13 Hours
Disaster;San Andreas
Musical;Frozen
Western;The Good, the Bad and the Ugly
Romance;La La Land


out: 

Action: Wonder Woman and Deadpool
Crime: Night Call
Drama: Twelve Years a Slave
Adventure: Avatar
Ninja: Elektra
Fantasy: Black Panther
Horror: The Conjuring 2 and Get Out
Romance: Midnight Sun and La La Land
Musical: High School Musical and Frozen
Mystery: The Game
Disaster: Cloverfield and San Andreas
Pirate: Pirates of the Caribbean
Thriller: Inception
Sports: Invictus
Terrorism: 13 Hours
Western: The Good, the Bad and the Ugly


"""

r = {}
n1 = int(input())
for i in range(n1):
    k1,v1 = input().split(";")
    r[k1] = [v1] 
n2 = int(input())
for i in range(n2):
    k2, v2 = input().split(";")
    if k2 in r:
        r[k2].append(v2)
    else:
        r[k2] = [v2]

for k, v in r.items():
    print(f'{k}: {" and ".join(v)}')
