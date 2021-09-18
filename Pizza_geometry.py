"""
John is opening a new restaurant called Pizza Galore. For his restaurant, he needs to order some custom-made pizza trays from Diamond Corp to carry the pizza boxes. John needs some help in figuring out the correct size for the pizza trays. The thing is Diamond Corp only manufactures square trays, and they need to know the length s in order to process an order. All pizza boxes are squares of side b and they are not allowed to be stacked on top of each other.
If John has to carry n pizza boxes of side b, what is the length s of the tray?

For example, a 16x16 tray (s=16 inches) can only carry 1 pizza box of size 16x16, while a 32x32 tray can fit up to 4, and a 48x48 up to 9.
Input
Line 1: An integer n for the number of pizzas
Line 2: A integer b that defines the length of side of each pizza box
Output
An integer s for the length of the side of the square tray
Constraints
0 < n <= 1*10^13
0 < r <= 1*10^12
0 < s <= 1*10^17
Example
Input

1
8

Output

8

---------------
2
8

16
---------------
3
2

4
_______________
4
2

4
___________
12
49


196
--------------------
570
120

2880

--------------
9879777
9999

31436856
----------------------
126781000230
84251512000

29998930368768000
-------------------------

"""
import math

n = int(input())
b = int(input())

print(b * int(math.ceil(n**0.5)))