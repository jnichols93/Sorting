# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j



        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
# Counting sort is a sorting algorithm that sorts the 
# elements of an array by counting the number of occurrences of each unique element in the array. 
# The count is stored in an auxiliary array and the sorting is done by mapping the count as an 
# index of the auxiliary array.
def count_sort( arr, maximum=-1 ):

    return arr