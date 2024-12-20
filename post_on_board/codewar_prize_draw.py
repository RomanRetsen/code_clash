'''
To participate in a prize draw each one gives his/her firstname.

Each letter of a firstname has a value which is its rank in the English alphabet. A and a have rank 1, B and b rank 2 and so on.

The length of the firstname is added to the sum of these ranks hence a number som.

An array of random weights is linked to the firstnames and each som is multiplied by its corresponding weight to get what they call a winning number.
Example:

names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
weights: [1, 4, 4, 5, 2, 1]

PauL -> som = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54
The *weight* associated with PauL is 2 so PauL's *winning number* is 54 * 2 = 108.

Now one can sort the firstnames in decreasing order of the winning numbers. When two people have the same winning number sort them alphabetically by their firstnames.
Task:

    parameters: st a string of firstnames, we an array of weights, n a rank

    return: the firstname of the participant whose rank is n (ranks are numbered from 1)

Example:

names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
weights: [1, 4, 4, 5, 2, 1]
n: 4

The function should return: "PauL"

Notes:

    The weight array is at least as long as the number of names, it may be longer.

    If st is empty return "No participants".

    If n is greater than the number of participants then return "Not enough participants".

    See Examples Test Cases for more examples.

'''
import string

def calc_val(name, mult):
    l = len(name)
    char_vals = \
        [
            (ord(x) - 64) if x in string.ascii_uppercase else (ord(x) - 96) \
                if x in string.ascii_lowercase else 0 for x in name
         ]
    # multy -1 in order to implement proper priority sorting with 2 conditions
    return (l + sum(char_vals)) * mult * -1

def rank(st, we, n):
    st_list = [(calc_val(x, y), x) for x,y in zip(st.split(","), we)]

    if len(st) == 0:
        return 'No participants'
    elif len(st_list) < n:
        return 'Not enough participants'
    else:
        return sorted(st_list)[n-1][1]

print(rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1,3,5,5,3,6], 2))
# output Matthew

print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))
# output Benjamin

print(rank("Lagon,Lily", [1, 5], 2))
# output Lagon

print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))
# output Not enough participants

print(rank("", [4, 2, 1, 4, 3, 1, 2], 6))
# output No participants
