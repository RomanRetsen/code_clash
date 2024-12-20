import random


def countingSort(arr):

    max_length = len(str(max(arr)))

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    for power in range(max_length):
        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (arr[i] / 10 ** power)
            count[int(index % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array

        print(count)
        for i in range(1, 10):
            count[i] += count[i - 1]
        print(count)

            # Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i] / 10 ** power)
            output[count[int(index % 10)] - 1] = arr[i]
            count[int(index % 10)] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

unsorted_list = [random.randint(1,1000) for _ in range(20)]
print(unsorted_list)
countingSort(unsorted_list)
print(unsorted_list)