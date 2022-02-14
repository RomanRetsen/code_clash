'''
All your fractions are belong to base
def group_and_skip(n, out, ins):
A pile of n identical coins lies on the table. Each move consists of three stages. First, the coins in the
remaining pile are arranged into groups of exactly out coins per group, where out is a positive
integer greater than one. Second, the n%out leftover coins that did not make a complete group of
out elements are taken aside and recorded. Third, from each complete group of out coins taken
out, exactly ins coins are collected to together create the new single pile, the rest of the coins again
put aside for good.
Repeat this three-stage move until the entire pile becomes empty, which must eventually happen
whenever out>ins. Return a list of how many coins were taken aside in each move.
n out ins Expected result
123456789 10 1 [9, 8, 7, 6, 5, 4, 3, 2, 1]
987654321 1000 1 [321, 654, 987]
255 2 1 [1, 1, 1, 1, 1, 1, 1, 1]
81 5 3 [1, 3, 2, 0, 4, 3]
10**9 13 3 [12, 1, 2, 0, 7, 9, 8, 11, 6, 8, 10, 5,
8, 3]
As you can see in the irst three rows, this method produces the digits of the nonnegative integer n
in base out in reverse order. So this entire setup turned out to be a cleverly disguised algorithm to
construct the representation of integer n in base out. However, an improvement over the standard
base conversion algorithm is that this version works not only for integer bases, but allows any
fraction out/ins that satis ies out>ins and gcd(out,ins)==1 to be used as a base! For
example, the famous integer 42 would be written as 323122 in base 4/3.
Yes, fractional bases are an actual thing. Take a deep breath to think about the implications
(hopefully something higher than winning a bar bet), and then imagine trying to do real world basic
arithmetic in such a system. That certainly would have been some "New Math" for the frustrated
parents in the swinging sixties for whom balancing their chequebooks in the familiar base ten was
already an exasperating ordeal!
'''
def group_and_skip(n, out, ins):
    return_list = []
    while (leftover := (n // out ) * ins) > ins:
        return_list.append(n % out)
        n = leftover
    else:
        return_list.append(n % out)
        if not leftover == 0:
            return_list.append(leftover)
    return return_list


n = 255
out = 2
ins = 1
# n = 987654321
# out = 1000
# ins = 1
print(group_and_skip(n, out, ins))