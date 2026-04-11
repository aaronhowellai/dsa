"""
This script exists to demonstrate another python simple O(n²) implementation of a Bubble Sorting algorithm.
"""

def bubblesort(arr):

    # loop to access each array element 
    for i in range(len(arr)):

        # loop to compare the array elements
        for j in range(0, len(arr) - i - 1):
            
            # compare two adjacent elements in ascending order
            if arr[j] > arr[j+1]: 

                # reassignment method
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

# create unsorted array
data = [456, 41, 2, 67, 43, 4, 25, 8]

# print unsorted array 
print(f"\nMy unsorted array: {data}!\n")

# print sorted array
print(f"Sorted array {bubblesort(data)}!\n")
                