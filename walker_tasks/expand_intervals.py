'''
Expand positive integer intervals

def expand_intervals(intervals):
An interval of consecutive positive integers can be succinctly described as a string that contains its
irst and last value, inclusive, separated by a minus sign. (This problem is intentionally restricted to
positive integers so that there will be no ambiguity between the minus sign character used as a
separator and an actual unary minus sign tacked in front of a digit sequence.) For example, the
interval that contains the integers 5, 6, 7, 8, 9 can be more concisely described as '5-9'. Multiple
intervals can be described together by separating their descriptions with commas. A singleton
interval with only one value is given as that value.
Given a string of such comma-separated intervals, guaranteed to be in sorted ascending order
and never overlap or be contiguous with each other, this function should create and return the list
that contains all the integers contained inside these intervals. In solving this problem, the same as
any other problems, it is always better to not have to reinvent the wheel, but irst check out whether
the string objects offer any useful methods that make your job easier.
'''
def expand_intervals(intervals):
    return_list = []
    # if len(return_list) == 0:
    #     return return_list
    for iterval in intervals.split(","):
        if not iterval.find("-") == -1:
            start, end = [int(x) for x in iterval.split("-")]
            return_list.extend(range(start, end + 1))
        elif iterval:
            return_list.append(int(iterval))
    return return_list

# str_to_process = '4-6,10-12,16' # [4, 5, 6, 10, 11, 12, 16]
str_to_process = '1,3-9,12-14,9999' # [1, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 9999]
# str_to_process = '4-5' # [4,5]
# str_to_process = '' # []
# str_to_process = '4-5' # [4,5]
# str_to_process = '42' # [42]
print(expand_intervals(str_to_process))