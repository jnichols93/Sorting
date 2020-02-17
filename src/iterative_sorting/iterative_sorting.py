# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range (cur_index, len(arr)): #comparision loop: starts as i +1 (index of range) and ends at length of array 
            if arr[smallest_index] > arr[j]:
                smallest_index = j


        # TO-DO: swap
        if arr[smallest_index] > arr[j]:
                smallest_index = j




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr