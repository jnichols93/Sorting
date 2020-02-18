# TO-DO: Complete the selection_sort() function below selection sort moves the smallest value to the left 1 by 1 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        #j represents our comparative integer
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j



        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below bubble sort floats the larger numbers to the right
def bubble_sort( arr ):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            # comparing two items next to each other 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
# Counting sort is a sorting algorithm that sorts the 
# elements of an array by counting the number of occurrences of each unique element in the array. 
# The count is stored in an auxiliary array and the sorting is done by mapping the count as an 
# index of the auxiliary array.
# def count_sort( arr, maximum=-1 ):
# # Count the number of times each value appears.
# # counts[0] stores the number of 0's in the input
# # counts[4] stores the number of 4's in the input etc.
#     counts = [0] * (maximum + 1)
#     for i in arr:
#         counts[i] += 1
    
#     num_i_before = 0
#     for i, count in enumerate(counts):
#         counts[i] = num_i_before
#         num_i_before += count
    
#     sorted_list = [None] * len(arr)

#     for i in arr:
#         sorted_list[ counts[i] ] = i
#         counts[i]+=1
#     return sorted_list