# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #initialize array indexes
    i_A = 0
    i_B = 0

    #for the length of the merged array
    for i in range(elements):
        #if an index lies beyond the bounds of the array,
        #we've reached the end, so add element from the other
        if len(arrA) <= i_A:
            #add element to the merged array and shift index
            merged_arr[i] = arrB[i_B]
            i_B += 1
        elif len(arrB) <= i_B:
            merged_arr[i] = arrA[i_A]
            i_A += 1
        #compare the two smallest unmerged values
        elif arrB[i_B] < arrA[i_A]:
            #if the right is smaller
            merged_arr[i] = arrB[i_B]
            i_B += 1
        else:
            #if the left is smaller than or equal to the right
            merged_arr[i] = arrA[i_A]
            i_A += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if array contains one element, it is sorted
    if len(arr) <= 1:
        return arr
    #if array contains more than one element, split in half and
    #sort each half, then merge together
    else:
        mid = len(arr) // 2
        arr_left = arr[:mid]
        arr_right = arr[mid:]
    return merge(merge_sort(arr_left), merge_sort(arr_right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
