"""
We need to perform a few operations on the list of words in input.txt.
We need to know the numbers of Uniquer Words, The lenght of the longest words and the lenght of the longest palindrome.

The answer is going to be

UniqueWords * (LenghtLongestWords - LenghLongestPalindrome)

"""

the_list = []
the_set = {}
palindrom_largest = 0
general_largest = 0

def is_pal2(input_word):
    if input_word == input_word[::-1]:
        return True
    return False

with open("med2_input.txt", "r") as f:
    while not (read_line := f.readline().strip()) == "":
        the_list.append(read_line)
        if is_pal2(read_line) and len(read_line) > palindrom_largest:
            palindrom_largest = len(read_line)
        if len(read_line) > general_largest:
            general_largest = len(read_line)

print(len(set(the_list)) * (int(general_largest) - int(palindrom_largest)))

