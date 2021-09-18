"""
In a list of words, there is ONE (word) that consists of first letters for the rest of the words in the list.
Find the word that matches the criteria described above and re-print the list (minus the abbrivation word)
in format described below

--------example 1--++
5
Best
Brilliant
Excellent
Super
Terrific

out

B: Brilliant
E: Excellent
S: Super
T: Terrific

------------test 2--

8
Amazing
Clever
Entertainting
Exceptional
Happy
Remarkable
Teacher
Tremendous

out

T: Tremendous
E: Entertainting
A: Amazing
C: Clever
H: Happy
E: Exceptional
R: Remarkable

------------test3

7
Adorable
Energetic
Faboulous
Father
Happy
Reliable
Talented

out

F: Faboulous
A: Adorable
T: Talented
H: Happy
E: Energetic
R: Reliable

-----------test4

7
Enjoy
Entertain
Indulge
Read
Relax
Retire
Travel

R: Read
E: Enjoy
T: Travel
I: Indulge
R: Relax
E: Entertain

"""


def check_word(i, all_words):
    if sorted(all_words[i].upper()) == sorted([x[0] for index, x in enumerate(all_words) if not index == i]):
        return True
    else:
        return False


n = int(input())
all_words = []
for i in range(n):
    word = input()
    all_words.append(word)

for i in range(len(all_words)):
    if check_word(i, all_words):
        for char in all_words[i]:
            for j in range(len(all_words)):
                if char.upper() == all_words[j][0] and not j == i:
                    print(f'{char}: {all_words[j]}')
                    break
        break
