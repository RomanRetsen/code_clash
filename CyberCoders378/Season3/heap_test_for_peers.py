'''
Create an algorithm for processing tasks in the list.
There are randomly generated 2 identical lists of tasks,
in which number represent the priority
(the lower the number the higher is priority).
We'll use two list in order to compare 2 different data structures
used in solving the same problem.
1-st list must be used to solve the problem with a help of list functions (sort, min, max  or slicing).
2-d list is used to solve the problem with a help of heap structure (and it's already solved)

Besides pre-existed tasks, there is a way when new task must be added to the list.
In the sequence of operations, there are only two possible types:
- "add <priority>" (add new task with "priority".)
- "pop <number>" (take <number> of high priority tasks from the list; display the priority values;
    delete those task from the list which effectevly marking it solved)
Sequence of operations are read from file "heap_test_addon"

EXAMPLE :
Currently list is 317 573 13 271 306 572 991 890 141 15
Operations: add 555
Currently list is 317 573 13 271 306 572 991 890 141 15 555
Operations: pop 2
Popped 2 smallest element is 13 and 15
Currently list is 141 271 306 317 555 572 573 890 991
Operations: pop 2
Popped 2 smallest element is 141 and 271
Currently list is 306 317 555 572 573 890 991
Operations: add 1
Currently list is 306 317 555 572 573 890 991 1
Operations: add 1000000000
Currently list is 306 317 555 572 573 890 991 1 1000000000
Operations: add 500000
Currently list is 306 317 555 572 573 890 991 1 1000000000 500000
Operations: pop 2
Popped 2 smallest element is 1 and 306

Both blocks of code (one that must be written by you and the one that already written)
are enclosed in the timing marks in order to measure efficiency of the code.

'''

from time import time
import heapq
from random import randint


# 10 mils of random tasks must be used for final test
# But list of 10 can be used to quick test
# list_for_list = [randint(1, 1000) for _  in range(10)]
list_for_list = [randint(1, 1000000000) for _  in range(10000000)]
# creating 2-d list with deep copy
list_for_heap = list_for_list[:]

mark_forlist1 = time()
# your code here !!!!!!!!!!

mark_forlist2 = time()
print(f"Time taken for list functionality {mark_forlist2 - mark_forlist1}")


mark_forheap1 = time()
heapq.heapify(list_for_heap)
with open("heap_test_addon") as file:
    for line in file:
        operation_data = line.strip().split()
        if len(operation_data) == 2 and operation_data[0] == "add":
            heapq.heappush(list_for_heap, int(operation_data[1]))
        elif len(operation_data) == 2 and operation_data[0] == "pop":
            number_to_pop = int(operation_data[1])
            print(f"Popping {number_to_pop} numbers")
            if number_to_pop <= len(list_for_heap):
                temp = []
                for _ in range(number_to_pop):
                    elem_to_pop = heapq.heappop(list_for_heap)
                    print(f"Popped element is {elem_to_pop}")
            else:
                print(f"There are not enough tasks left to pull {number_to_pop}")
mark_forheap2 = time()
print(f"Time taken for heap functionality {mark_forheap2 - mark_forheap1}")
