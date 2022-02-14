'''
Recamán's sequence
def recaman_item(n):
Compute and return the n:th term of the Recam n's sequence. See the linked de inition for this
sequence on Wolfram Mathworld.
Note how the de inition for the current element in this sequence depends on whether some
particular number can be found in the previously generated pre ix of the sequence. To allow your
function to execute in a sure and speedy fashion even for millions of elements, you should use a set
to keep track of which elements are already part of the pre ix of the sequence generated so far. This
way you can generate each element in constant time, instead of having to iterate through the entire
previously generated list the way some "Shlemiel" might approach this problem.
n Expected result
1 1
8 12
13 23
57 87
395743 258330
The previous version of this problem, simply called recaman in the very irst versions of this
problem collection, expected this function to return the entire sequence up to the n:th term. This
dates all the way back to the original automated tester script that computed only the checksum of
expected answers, but did not record or reveal the expected answers to aid students in their
debugging tasks. Since the expected_answers ile did not even exis
'''
def recaman_item(n):
    if n == 0:
        return 1
    recaman_seq = [1,]
    # power of set!!! if list is used to check existance with 'in' operator
    # code become quite inefficient
    check_set = {1,}
    for i in range(1, n):
        possible_new_value = recaman_seq[i-1] - (i + 1)
        if possible_new_value > 0 and not possible_new_value in check_set:
            recaman_seq.append(possible_new_value)
            check_set.add(possible_new_value)
        else:
            new_value = recaman_seq[i-1] + (i + 1)
            recaman_seq.append(new_value)
            check_set.add(new_value)
    return recaman_seq[-1]

n = 395743
print(recaman_item(n))