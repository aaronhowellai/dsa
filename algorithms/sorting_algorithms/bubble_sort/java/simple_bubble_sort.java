/*
Implement a simple O(n²) bubble sort algorithm in java to compare language structures to each other.
"*/

// Bubble sort in Java

import java.util.Arrays;

class SimpleBubbleSort {

    // perform the bubble sort 
    static void bubbleSort(int arr[]) {
        int n = arr.length;

        // loop to access each array element
        for (int i = 0; i < n - 1; i++)

            // loop to compare each adjacent element in the array 
            for (int j = 0; j < n - i - 1; j++)

                // compare two adjacent adjacent elements
                if (arr[j] > arr[j + 1]) {

                    // swap if elements meet the target condition

                    // basic reassignment design 
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
    }

    public static void main(String args[]) {

        int[] data = {456, 41, 2, 67, 43, 4, 25, 8};

        // print unsorted array first
        System.out.println(System.lineSeparator());
        System.out.println("Unsorted array:");
        System.out.println(Arrays.toString(data));
        System.out.println(System.lineSeparator());
        
        // call method using class name
        SimpleBubbleSort.bubbleSort(data); 
        System.out.println("Sorted array:");
        System.out.println(Arrays.toString(data));
        System.out.println(System.lineSeparator());
    }
}