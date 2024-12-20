def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1

arr = [2,3,4,10,40]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)
print(result)