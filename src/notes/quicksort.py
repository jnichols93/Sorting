
# [5 9 3 7 2 8 1 6]

# [3 2 1][5][9 7 8 6]

# [2 1][3][][5][7 8 6][9][]

# [1][2][3][4][5][6][7][8][9]

# decide on the base case
# base case is []
# find the pivot point

# partition our data to the left and right of our pivot
#  left -> smaller than pivot, right -> larger than pivot
# What if they're the same size as the pivot? just pick one? >=

# Repeat, Recurse,

my_list = [5, 9, 3, 7, 2, 8, 1, 6]

def partition(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: #handling > or =
            right.append(item)
    return left, pivot, right

def quicksort(data):
    #base case
    if data == []:
        return data
    
    left, pivot, right = partition(data)

    return quicksort(left)+ [pivot] + quicksort(right)

print(quicksort(my_list))

# print(5 in my_list)
# in =
# for item in my_list:
#         if item == n:
#                return True
#         else:
#                 return False
