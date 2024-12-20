import time
import random

def longest_inc_sublist(input_list):
    length_array = [1 for _ in range(len(input_list))]
    for i in range(len(input_list)):
        for y in range(i):
            if input_list[y] < input_list[i]:
                length_array[i] = max(length_array[i], length_array[y] + 1)
    return max(length_array)

def longest_inc_sublist2(input_list):
    l_length = len(input_list)
    hops_list = [{1:[input_list[x]]} for x in range(l_length)]
    print(hops_list)
    for i in range(l_length):
        for y in range(i, l_length):
            if input_list[y] > input_list[i]:
                if max(hops_list[y].keys()) < (max(hops_list[i].keys()) + 1):
                    hops_list[y][max(hops_list[i].keys()) + 1] = hops_list[i][max(hops_list[i])].copy() + [input_list[y]]
    print([(max(x), x[max(x)]) for x in hops_list])
    return max([max(x) for x in hops_list])

def longest_inc_relatives(input_list):
    l_length = len(input_list)
    max_length = 1
    start_mark = max_start_mark = 0
    end_mark = max_end_mark =  0
    current = input_list[0]
    for i in range(1, l_length):
        if input_list[i] > current:
            end_mark = i
            if end_mark - start_mark + 1 > max_length:
                max_length = end_mark - start_mark + 1
                max_start_mark = start_mark
                max_end_mark = end_mark
        else:
            start_mark = i
            end_mark = i
        current = input_list[i]
    print(f'max_length {max_length}; start_mark {max_start_mark}; end_mark {max_end_mark}')


if __name__ == "__main__":
    # test_list = [6, 2, 5, 1, 7, 4, 8, 3, 9]
    # test_list = [random.randint(1,1000) for _ in range(1000)]
    test_list = [399, 119, 194, 231, 339, 52, 48, 847, 412, 488, 900, 400, 405, 410, 411, 999]
    print(test_list)
    t0 = time.time()
    print(longest_inc_sublist(test_list))
    t1 = time.time()
    print(f"1-st method time: {t1-t0}")
    print(longest_inc_sublist2(test_list))
    t2 = time.time()
    print(f"2-nd method time: {t2-t1}")
    longest_inc_relatives(test_list)