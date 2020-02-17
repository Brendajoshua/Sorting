# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        #loop through elements on right-hand-side of current index and find the smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j     

        # TO-DO: swap
        #swap the element at the current index with the smallest element found in above loop
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        swaps = 0
        #Loop through array
        for i in range(len(arr)):
            #compare each element to its neighbour
            if i > 0 and arr[i] < arr[i - 1]:
                #If elements in wrong position (relative to each other) swp them
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swaps += 1
        #if no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1
        if swaps == 0:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr