from collections import deque

class Queue:
    def __init__(self, x):
        self.the_q = deque(maxlen=x)

    def is_empty(self):
        return True if len(self.the_q) == 0 else False

    def sizeof(self):
        return len(self.the_q)

    def enqueue(self, element):
        self.the_q.appendleft(element)

    def dequeue(self):
        return self.the_q.pop()

    def move_along(self, n):
        self.the_q.rotate(n)

    def __repr__(self):
        return "->".join([str(x) for x in self.the_q])

def hot_potato(name_list, num):
    sim_queue = Queue(len(name_list))
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.sizeof() > 1:
        sim_queue.move_along(num)
        # for i in range(num):
        #     sim_queue.enqueue(sim_queue.dequeue())
        #     print(sim_queue)
        sim_queue.dequeue()

    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
