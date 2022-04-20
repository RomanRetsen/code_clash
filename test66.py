def three_summers(items, goal):
    for i in range(len(items)):
        print(f"i = {i}")
        x = items[i]
        start = i+1
        end = len(items) - 1
        newGoal = goal - x
        while start < end:
            two_summers = items[start] + items[end]
            if two_summers == newGoal:
                print(f"start {start}; end {end}")
                return True
            elif two_summers < newGoal:
                start += 1
            else:
                end -= 1
    return False


def three_summers_mine(items, goal):
    print(items)
    i = 0
    l = len(items) - 3
    while i <=l and items[i] * 3 <= goal:
        j = i + 1
        end_j = len(items) - 2
        new_goal = goal - items[i]
        while j <= end_j and items[j] * 2 <= new_goal:
            k = j + 1
            end_k = len(items) - 1
            final_goal = new_goal - items[j]
            while k <= end_k and items[k] <= final_goal:
                print(f"trying {items[k]}")
                if items[k] == final_goal:
                    return True
                k += 1
            j += 1
        i += 1
    return False


# in_list = [1,2,3]
# goal = 6
in_list = [2, 3, 5, 10, 16, 30, 54, 64, 70, 72, 115, 200, 318, 424, 571, 749, 789, 1035, 1132, 1153, 1212, 1345, 1682, 1908, 2390, 2503, 2564, 3131, 3331, 3616, 3728, 4160, 5103, 5918, 6192, 7015, 7217, 7232, 8463, 9707, 10674, 11055, 11590, 12780, 14157, 14321, 14372, 14667, 15333, 15892, 18205, 20261, 20757, 21898, 22773, 24717, 26989, 28060, 30665, 32009, 33781, 37152, 38477, 40040, 43808, 44660, 47337, 48067, 51620, 52417, 55664, 57538, 58345, 59965, 61787, 66384, 66685, 71504, 74937, 78327, 80892, 82198, 86844, 92538, 98073, 100263, 104893, 107588, 112072, 119005, 119435, 125664, 133376, 139378, 143511, 149859, 152627, 159887, 162510, 169724, 172753, 179974, 185586, 192351, 200078, 206773, 210988, 220611, 226043, 234908, 241378, 248360, 256681, 257459, 258060, 258986, 262029, 275480, 287378, 293319, 296975, 307200, 307861, 317090, 327996, 336986, 351964, 362302, 371780, 379167, 388458, 395010, 407602, 407717, 411823, 419968, 432774, 441948, 448783, 457348, 460668, 463095, 480393, 493196, 509479, 513051, 517224, 527498, 543628, 562340, 564886, 583588, 601437, 621316, 625641, 633336, 636281, 652229, 672238, 694724, 705516, 708745, 734594, 736603, 738354, 743295, 768382, 786559, 800285, 803535, 820630, 847748]
goal = 260117
print(three_summers_mine(in_list, goal))