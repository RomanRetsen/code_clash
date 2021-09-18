my_string = "Taras Grigorovuch Shevchenko"

mark = 0
while not (the_index := my_string.find("y", mark)) == -1:
    print(my_string[the_index:the_index+2])
    mark =the_index + 1