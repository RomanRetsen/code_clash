"""
You must determine which of the input list are Hamming Numbers.

Hamming numbers are those integers whose only prime factors are 2, 3 and 5.

Smooth, eh?
Input
Line 1: the number N of integers
Next N lines: an integer I
Output
N lines: HAMMING or OTHER
Constraints
N ≤ 20
I < 2⁵³
Example
Input

10
1
2
3
4
5
6
7
8
9
10

Output

HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
OTHER
HAMMING
HAMMING
HAMMING

-----------------
15
600
640
675
729
768
810
900
972
1024
1125
1200
1250
1296
1440
1500

HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
------------------------------
15
630
650
732
760
806
872
966
1001
1092
1160
1216
1290
1400
1460
1539

OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
OTHER
_____________
20
8916100448256000
8905786697765618
8978233254014990
8883664392439636
8967378984372715
8906044184985600
8815968460800000
8839938372534426
8887458428319767
8847360000000000
8957952000000000
8898925781250000
8968066875000000
8926168066560000
8857350000000000
8981943434664571
8855835700998201
8910737505679793
8825923015031250
8983733062992534

HAMMING
OTHER
OTHER
OTHER
OTHER
HAMMING
HAMMING
OTHER
OTHER
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
HAMMING
OTHER
OTHER
OTHER
HAMMING
OTHER
"""

"""
def is_humming(n):
    prime_allowed = [2,3,5]
    while not n == 1:
        for pr in prime_allowed:
            if n % pr == 0:
                n //= pr
                break
        else:
            return False
    return True

n = int(input())
for i in range(n):
    i = int(input())
    if is_humming(i):
        print("HAMMING")
    else:
        print("OTHER")
"""
x=[*open(0)]
for i in x[1:]:
 z=int(i)
 for j in [2,3,5]*100:
  if z%j==0:z/=j
 if z<=1:print('HAMMING')
 else:print('OTHER')