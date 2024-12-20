from time import time
from random import randint


def best_sublist0(input_list):
    my_max = 0
    x_max = 0
    y_max = 0
    for i in range(0, len(my_list)):
        for y in range(i, len(my_list)+1):
            sum = 0
            for k in range(i, y):
                sum += input_list[k]
            if sum > my_max:
                x_max = i
                y_max = y-1
                my_max = sum
    print(my_max)
    return (x_max, y_max)

def best_sublist(input_list):
    my_max = 0
    x_max = 0
    y_max = 0
    for i in range(0, len(my_list)):
        for y in range(i, len(my_list)+1):
            #3-d loop created by slicing making this algorithm 0n**3
            slice_sum = sum(my_list[i:y])
            if slice_sum > my_max:
                x_max = i
                y_max = y-1
                my_max = slice_sum
    print(my_max)
    return (x_max, y_max)

def best_sublist2(input_list):
    my_max = 0
    x_max = 0
    y_max = 0
    for i in range(len(input_list)):
        sum = 0
        for y in range(i, len(input_list)):
            sum += input_list[y]
            if sum > my_max:
                x_max = i
                y_max = y
                my_max = sum
    print(my_max)
    return (x_max, y_max)

def best_sublist3(input_list):
    my_max = -1000
    x_max = 0
    x_new_max_potencial = 0
    y_max = 0
    sum = 0
    for i in range(len(input_list)):
        if input_list[i] >= sum + input_list[i]:
            # print(f'input_sublist {input_list[i]}')
            # print(f'sum+sublist {sum + input_list[i]}')
            sum = input_list[i]
            x_new_max_potencial = i
        else:
            sum += input_list[i]

        if sum > my_max:
            x_max = x_new_max_potencial
            my_max = sum
            y_max = i

    print(f'my_max {my_max}')
    return (x_max,y_max)


#similar and simple than best_sublist3. 0 is min value
def best_sublist4(a, size):
    max_so_far = -1000
    max_ending_here = 0
    x_max = 0
    x_new_max_potencial = 0
    y_max = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            x_max = x_new_max_potencial
            y_max = i
            max_so_far = max_ending_here

        if max_ending_here < 0:
            x_new_max_potencial = i + 1
            max_ending_here = 0
    print(max_so_far)
    return (x_max, y_max)

if __name__ == "__main__":
    # my_list = [-1, -5, -1, 2, 4, -3, 4, -2, 5, -5, 2, -6, -1, -5, -1, 2, 4, -3, -4, 5, 2, -5, 2, -6]
    my_list = [3, 2, -9, 5, 2, -9, 1, -8, 3, -10, 1, -10, 5, 3, 2, -3, -8, 4, 4, -7, 1, -5, 3, -6, 0, -10, -8, -4, -8, 2, -1, 2, -4, -6, 4, -5, -3, 2, -5, -3, 3, 4, -7, -6, 3, -3, -8, -6, 3, 5, 5, -10, 0, 0, -9, -8, -3, -2, -1, -1, -5, 5, -5, -9, -7, -6, -2, -3, -4, -10, 1, -10, -7, -9, 0, 2, 3, -10, -8, -2, -8, -5, -5, -7, 1, 1, -8, -4, 0, -2, -9, 2, -5, -5, -1, -6, -9, 5, 5, -1]

    # my_list = [-2, -4, 1, 3, -6, -2, -5, -2]
    # my_list = [randint(-10, 5) for _ in range(100)]
    print(my_list)
    t00 = time()
    x_max, y_max = best_sublist0(my_list)
    t0 = time()
    print(f'x= {x_max}; y= {y_max} Time: {t0-t00}')
    x_max, y_max = best_sublist(my_list)
    t1 = time()
    print(f'x= {x_max}; y= {y_max} Time: {t1-t0}')
    x_max, y_max = best_sublist2(my_list)
    t2 = time()
    print(f'x= {x_max}; y= {y_max} Time: {t2-t1}')
    x_max, y_max = best_sublist3(my_list)
    t3 = time()
    print(f'x= {x_max}; y= {y_max} Time: {t3-t2}')
    x_max, y_max = best_sublist4(my_list, len(my_list))
    t4 = time()
    print(f'x= {x_max}; y= {y_max} Time: {t4-t3}')
