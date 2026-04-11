// Implement Simple Bubble Sort algorithm in Go with tuple assignment design

package main

import (
	"fmt"
)

// perform the bubble sort
func bubbleSort(arr []int) {
	n := len(arr)

	// loop to access each element in the array
	for i := 0; i < n-1; i++ {

		// loop to compare each adjacent element in the array
		for j := 0; j < n-1; j++ {

			// compare two adjacent elements with tuple assignment
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
}

func main() {
	data := []int{456, 41, 2, 67, 43, 4, 25, 8}

	// print the unsorted array
	fmt.Println()
	fmt.Println("Unsorted array:")
	fmt.Println(data)
	fmt.Println()

	// print the sorted data
	bubbleSort(data)
	fmt.Println("Sorted array:")
	fmt.Println(data)
	fmt.Println()
}
