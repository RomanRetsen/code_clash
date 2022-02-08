# the_list = ['cat', 'dog'] # 0
# the_list = ['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 'god'] # 2
the_list = ['dog', 'cat', 'dog', 'god', 'dog', 'god', 'dog', 'god', \
            'dog', 'dog', 'god', 'god', 'cat', 'dog', 'god', 'cat', 'tac'] # 11
# the_list = ['god', 'tac', 'tac', 'tac', 'tac', 'dog', 'dog', 'tac', \
#             'cat', 'dog', 'god', 'cat', 'dog', 'cat', 'cat', 'tac'] #0

the_dict = {"cat":0, "dog":0, "tac":0, "god":0}
growling_count = 0

for animal in the_list:
    if (animal == "cat" or animal == "dog") and \
            the_dict["cat"] + the_dict["tac"] < the_dict["dog"] + the_dict["god"]:
        growling_count +=1
    the_dict[animal] +=1

the_dict = {"cat":0, "dog":0, "tac":0, "god":0}

for animal in the_list[::-1]:
    if (animal == "tac" or animal == "god") and \
            the_dict["cat"] + the_dict["tac"] < the_dict["dog"] + the_dict["god"]:
        growling_count +=1
    the_dict[animal] +=1

print(growling_count)