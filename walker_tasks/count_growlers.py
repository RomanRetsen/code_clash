'''
Count growlers
def count_growlers(animals):
Let the strings 'cat' and 'dog' denote that kind of animal facing left, and 'tac' and 'god'
denote that same kind of animal facing right. Since in this day and age this whole setup sounds like
some kind of a meme anyway, let us somewhat unrealistically assume that each individual animal,
regardless of its own species, growls if it sees strictly more dogs than cats to the direction that the
animal is facing. Given a list of such animals, return the count of how many of these animals are
growling. In the examples listed below, the growling animals have been highlighted in green.
animals Expected result
['cat', 'dog'] 0
['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 2
'god']
['dog', 'cat', 'dog', 'god', 'dog', 'god', 'dog', 11
'god', 'dog', 'dog', 'god', 'god', 'cat', 'dog',
'god', 'cat', 'tac']
['god', 'tac', 'tac', 'tac', 'tac', 'dog', 'dog', 0
'tac', 'cat', 'dog', 'god', 'cat', 'dog', 'cat',
'cat', 'tac']
'''

# animals = ['cat', 'dog'] # 0
animals = ['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 'god'] # 2
# animals = ['dog', 'cat', 'dog', 'god', 'dog', 'god', 'dog', 'god', \
#             'dog', 'dog', 'god', 'god', 'cat', 'dog', 'god', 'cat', 'tac'] # 11
# animals = ['god', 'tac', 'tac', 'tac', 'tac', 'dog', 'dog', 'tac', \
#             'cat', 'dog', 'god', 'cat', 'dog', 'cat', 'cat', 'tac'] #0

def count_growlers(animals):
    the_dict = {"cat":0, "dog":0, "tac":0, "god":0}
    growling_count = 0

    for animal in animals:
        if (animal == "cat" or animal == "dog") and \
                the_dict["cat"] + the_dict["tac"] < the_dict["dog"] + the_dict["god"]:
            growling_count +=1
        the_dict[animal] +=1

    the_dict = {"cat":0, "dog":0, "tac":0, "god":0}

    for animal in animals[::-1]:
        if (animal == "tac" or animal == "god") and \
                the_dict["cat"] + the_dict["tac"] < the_dict["dog"] + the_dict["god"]:
            growling_count +=1
        the_dict[animal] +=1

    return growling_count

print(count_growlers(animals))