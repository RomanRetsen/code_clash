"""
Translate the text to the Ubbi Dubbi language.

Rules:
Ubbi Dubbi works by adding "ub" before each vowel sound ('a', 'e', 'i', 'o', 'u') in a syllable.
But, if there are two (or more) consecutive vowel sounds, the "ub" comes only before the first vowel.
Input
Line 1: A string input.
Output
Line 1: The result translated to the Ubbi Dubbi language.
Constraints
0 ≤ input string length ≤ 1024
All answers are in lowercase.
Example
Input

hello world

Output

hubellubo wuborld

---------------------------
we wish you a marry christmas and a happy new year
output
wube wubish yubou uba mubarry chrubistmubas uband uba hubappy nubew yubear

-----------------
harry potter and the prisoner of azkaban
output

hubarry pubottuber uband thube prubisubonuber ubof ubazkubabuban
-----------------------
lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
output
luborubem ubipsubum dubolubor subit ubamubet, cubonsubectubetubur ubadubipubisubicubing ubelubit, subed dubo ubeiusmubod tubempubor ubincubidubidubunt ubut lubabuborube ubet duboluborube mubagnuba ubalubiqubua.
"""

import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

_input = input()
pattern = r'([aueoy]+)'

print(re.sub(r'([aueoy]+)', 'ub\\1', _input))
