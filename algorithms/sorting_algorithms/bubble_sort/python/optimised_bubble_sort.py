"""
This script exists to demonstrate an optimised implementation of the Bubble Sorting algorithm.
"""

def bubbleSort(arr):

    # loop through each element in the array
    n = len(arr)
    for i in range(n):

        # keep track of swapping
        swapped = False

        # loop to compare array elements

        for j in range(0, n-i-1):

            # compare two adjacent elements
            if arr[j] > arr[j+1]:

                # tuple assignment to swap positions
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # update swapped status
                swapped = True

        # no swapping means the array is already sorted and no further comparison is needed
        if not swapped:
            break

data = [456,41,2,67,43,4,25,8]

# print unsorted data
print(f"\nUnsorted data: {data}\n")

# print sorted data by first calling the algorithm
bubbleSort(data)
print(f"Sorted data: {data}\n")