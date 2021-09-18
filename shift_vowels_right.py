import collections

#shift vowels 1 index to the right. The word is cyclic, meaning If vowels is the last character,
# it should get index 0 and become first charter

line = input()
my_deq = collections.deque(line)

skip = False
for i in range(len(my_deq)):
    if skip:
        skip = False
        continue
    elif my_deq[i].upper() in ['A', 'E', 'I', 'O', 'U'] and i == len(my_deq)-1:
        my_deq.appendleft(my_deq.pop())
    elif my_deq[i].upper() in ['A', 'E', 'I', 'O', 'U']:
        # C style swap
        # temp = my_deq[i+1]
        # my_deq[i+1] = my_deq[i]
        # my_deq[i] = temp
        #
        #python style swap
        my_deq[i], my_deq[i+1] = my_deq[i+1], my_deq[i]
        skip = True
print(''.join(my_deq))

# input : CODINGAME
# output :ECDONIGMA