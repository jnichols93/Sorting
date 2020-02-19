# TO-DO: complete the heap sort function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if len(arrA) == 0 or len(arrB) == 0:
            return merged_arr[:i] + arrA + arrB
        if arrA[0] > arrB[0]:
            merged_arr[i] = arrB.pop(0)
        else:
            merged_arr[i] = arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    l = len(arr)
    if l > 1:
        new_arr = l // 2
        leftarr = arr[:new_arr]
        rightarr = arr[new_arr:]
        arrA = merge_sort(leftarr)
        arrB = merge_sort(rightarr)
        arr = merge(arrA, arrB)
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below named after tim sort ((hybrid) insertion sort + )
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     # splitting
#     for i in range(0, len(arr), RUN):
#         arr[i]

#     return arr

# radix/bucket sort
# https://www.geeksforgeeks.org/radix-sort/
# A function to do counting sort of arr[] according to
# the digit represented by exp.
# def countingSort(arr, exp1):
#     n = len(arr)
#     # The output array elements that will have sorted arr
#     output = [0] * (n)
#     # initialize count array as 0
#     count = [0] * (10)
#     # Store count of occurrences in count[]
#     for i in range(0, n):
#         index = (arr[i]/exp1)
#         count[ (index)%10 ] += 1
#     # Change count[i] so that count[i] now contains actual
#     #  position of this digit in output array
#     for i in range(1,10):
#         count[i] += count[i-1]
#     # Build the output array
#     i = n-1
#     while i>=0:
#         index = (arr[i]/exp1)
#         output[ count[ (index)%10 ] - 1] = arr[i]
#         count[ (index)%10 ] -= 1
#         i -= 1
#     # Copying the output array to arr[],
#     # so that arr now contains sorted numbers
#     i = 0
#     for i in range(0,len(arr)):
#         arr[i] = output[i]

# def radixSort( arr ):
# # find max number to know number of digits
#     max1 = max(arr)
#     exp = 1
#     while max1/exp > 0:
#         countingSort(arr, exp)
#         exp *= 10

# arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
# radixSort(arr)

# for i in range(len(arr)):
#     print(arr[i]),
