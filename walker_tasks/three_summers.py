import math
# function is working but it's O(n**3) that's why its too slow in "range list" case

def three_summers(items, goal):
    start = 0
    while items[start] <= math.floor(goal // 3):
        inner_goal = goal - items[start]
        inner_start = start + 1
        while items[inner_start] <= math.floor(inner_goal // 2):
            final_goal = goal - items[start] - items[inner_start]
            final_start = inner_start + 1
            while items[final_start] <= final_goal:
                if items[final_start] == final_goal:
                    return True
                elif final_start + 1 < len(items):
                    final_start += 1
                else:
                    break
            if inner_start + 2 < len(items):
                inner_start += 1
            else:
                break
        if start + 3 < len(items):
            start += 1
        else:
            return False
    else:
        return False

# items = [10, 11, 16, 18, 19]
# items = [10, 11, 16, 18, 19]
# items = [1,2,3]
items = [10, 11, 16, 18, 19]
print(three_summers(items, 40))