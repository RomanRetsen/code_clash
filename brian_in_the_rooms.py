import string


x = y=-1
stop_search = False
h = int(input())
w = int(input())

around_list = []
previous_record = ""
for i in range(h):
    mapline = input()
    col = mapline.find("B")
    if not x == -1 and not y == -1 and not stop_search:
        around_list.append(mapline[y])
        stop_search = True
    if not col == -1:
        x = i
        y = col
        if x > 0:
            around_list.append(previous_record[y])
        if col > 0:
            around_list.append(mapline[col - 1])
        if col < len(mapline)-1:
            around_list.append(mapline[col + 1])
    previous_record = mapline

result = set([x for x in around_list if x in string.ascii_letters])
if len(result) == 1:
    where_is_b = result.pop()
    if where_is_b == "L":
        print("BRIAN IS IN THE LIVING ROOM")
    elif where_is_b == "T":
        print("BRIAN IS IN THE BATHROOM")
    elif where_is_b == "K":
        print("BRIAN IS IN THE KITCHEN")
    elif where_is_b == "E":
        print("BRIAN IS IN THE BEDROOM")
    elif where_is_b == "C":
        print("BRIAN IS IN THE CORRIDOR")
