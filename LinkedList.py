import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

class UnsortedList:
    def __init__(self):
        self.head = None
        self.current_size = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        new_item = Node(item)
        new_item.set_next(self.head)
        self.head = new_item
        self.current_size += 1

    def size(self):
        return self.current_size

    def is_in(self, item):
        found = False
        e = self.head
        while not e is None and not found:
            if e.get_data() == item:
                found = True
            else:
                e = e.get_next()
        return found

    def remove(self, item):
        found = False
        previous = None
        e = self.head
        while not e is None:
            if e.get_data() == item:
                found = True
                self.current_size -= 1
                if previous:
                    previous.set_next(e.get_next())
                    e = None
                    print(f"Ref count of e {sys.getrefcount(e)}")
                    e = previous
                else:
                    self.head = e.get_next()
                    e = None
                    print(f"Ref count of e {sys.getrefcount(e)}")
                    e = self.head
            else:
                previous = e
                e = e.get_next()
        return found

    def __repr__(self):
        if self.size() > 0:
            r = []
            e = self.head
            r.append(f"(: {e.get_data()} :)")
            e = e.get_next()
            while not e == None:
                r.append(e.get_data())
                e = e.get_next()
            return " --> ".join([str(x) for x in r])
        else:
            return "Unordered list is empty"



mylist = UnsortedList()
mylist.add(31)
mylist.add(77)
mylist.remove(77)
mylist.remove(31)
print(mylist.is_empty())
print(mylist)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
# print(f"list size {mylist.size()}")
# print(mylist.is_in(54))
# print(mylist)
# mylist.remove(31)
# print(mylist)
# print(f"new size {mylist.size()}")
#

