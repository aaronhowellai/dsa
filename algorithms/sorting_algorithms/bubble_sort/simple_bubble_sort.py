"""
This script exists to demonstrate a simple implementation of a Bubble Sorting algorithm.
"""

def bubble_sort(arr):

    # set a simple reusable variable to represent the full length of the array
    n = len(arr)

    # go through all elements with respect to zero indexing
    for i in range(0,n-1):

        # go through all array elements, minus the ones already sorted
        for j in range(0, n-i-1):
            
            # swap the next number with the current number if it is greater than it, by a value of 1 (int)
            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

# implement the script
nArray = [456, 41,2,67,43,4,25,8]

# print the unsorted array
print(f"\nMy unsorted array: {nArray}!\n")

# print the sorted array, that implemented the algorithm
print(f"Sorted array: {bubble_sort(nArray)}!\n")

        