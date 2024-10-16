'''
Create an algorithm for processing tasks in the list.
There are randomly generated 2 lists of tasks, in which number represent
priority (the lower the number the higher is priority)
Also besides pre-existence tasks, there is a way when new task must be added to the list.
In the sequence of operation only two possible type:
- "add <number>" (add new task with priority. Or simply number must be added to the list)
- "pop" (take high priority task from the list; display the priority values; delete those task from the list)
Sequence of operations are read from file "heap_test_adon"

EXAMPLE :
Currently list is 317 573 13 271 306 572 991 890 141 15
Operations: add 555
Currently list is 317 573 13 271 306 572 991 890 141 15 555
Operations: pop
Popped 2 smallest element is 13 and 15
Currently list is 141 271 306 317 555 572 573 890 991
Operations: pop
Popped 2 smallest element is 141 and 271
Currently list is 306 317 555 572 573 890 991
Operations: add 1
Currently list is 306 317 555 572 573 890 991 1
Operations: add 1000000000
Currently list is 306 317 555 572 573 890 991 1 1000000000
Operations: add 500000
Currently list is 306 317 555 572 573 890 991 1 1000000000 500000
Operations: pop
Popped 2 smallest element is 1 and 306
'''

from time import time
import heapq
from random import randint


# list_for_list = [randint(1, 1000000000) for _  in range(10)]
list_for_list = [randint(1, 1000) for _  in range(10)]
list_for_heap = list_for_list[:]

mark_forlist1 = time()
# code hear
with open("heap_test_addon") as file:
    for line in file:
        operation_data = line.strip().split()
        if len(operation_data) == 2 and operation_data[0] == "add":
            list_for_list.append(int(operation_data[1]))
        elif len(operation_data) == 1 and operation_data[0] == "pop":
            list_for_list.sort()
            elem1, elem2 = list_for_list[:2]
            del list_for_list[:2]
            print(f"Popped 2 smallest element is {elem1} and {elem2}")
mark_forlist2 = time()
print(f"Time taken for list functionality {mark_forlist2 - mark_forlist1}")


mark_forheap1 = time()
heapq.heapify(list_for_heap)
with open("heap_test_addon") as file:
    for line in file:
        operation_data = line.strip().split()
        if len(operation_data) == 2 and operation_data[0] == "add":
            heapq.heappush(list_for_heap, int(operation_data[1]))
        elif len(operation_data) == 1 and operation_data[0] == "pop":
            elem_to_pop = heapq.heappop(list_for_heap)
            elem_to_pop2 = heapq.heappop(list_for_heap)
            print(f"Popped element is {elem_to_pop} and {elem_to_pop2}")
mark_forheap2 = time()
print(f"Time taken for heap functionality {mark_forheap2 - mark_forheap1}")
