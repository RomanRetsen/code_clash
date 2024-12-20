'''

Line 1 : The number of movies in the list
N next lines : A string with the title of the movie and his rating
Output
List of movies titles rated >= 6/10
Constraints
If two movies have the same rating, you need to range them in the same order of the original list.
Example
Input

3
Destination finale 2 (6.2/10)
The Fighting Temptations (5.6/10)
Le monde de Nemo (8.1/10)

Output

Le monde de Nemo
Destination finale 2

-------------------------test2
7
Elfe (6.9/10)
Un duplex pour 3 (5.9/10)
Dreamcatcher, l'attrape-reves (5.5/10)
Dickie Roberts: Ex-enfant star (5.6/10)
Lune de miel en enfer (5.4/10)
Dark Blue (6.6/10)
Daredevil (5.3/10)

output

Elfe
Dark Blue

--------------------------test3
2
Ecole paternelle (5.6/10)
Lady Chance (7/10)

output

Lady Chance

--------------------test4
5
Self Control (6/10)
2 Fast 2 Furious  (5.9/10)
30 minutes maximum (6/10)
The Simpsons (The movie) (7.3/10)
Destination: Graceland (6/10)

output

The Simpsons (The movie)
Self Control
30 minutes maximum
Destination: Graceland

'''

n = int(input())
r = []
for i in range(n):
    movie,_, rating = input().rpartition(" ")
    if (the_rating := float(rating.strip("()").split("/")[0])) >= 6:
        r.append((movie, the_rating))

print(*[x[0]  for x in sorted(r, key=lambda x:x[1], reverse=True)], sep="\n")