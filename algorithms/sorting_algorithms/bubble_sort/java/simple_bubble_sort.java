/*
Implement a simple O(n²) bubble sort algorithm in java to compare language structures to each other.
"*/

// Bubble sort in Java

import java.util.Arrays;

class SimpleBubbleSort {

    // perform the bubble sort 
    static void bubbleSort(int array[]) {
        int n = array.length;

        // loop to access each array element
        for (int i = 0; i < n - 1; i++)

            // loop to compare each adjacent element in the array 
            for (int j = 0; j < n - i - 1; j++)

                // compare two adjacent adjacent elements
                if (array[j] > array[j + 1]) {

                    // swap if elements meet the target condition
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
    }

    public static void main(String args[]) {

        int[] data = {456, 41, 2, 67, 43, 4, 25, 8};

        // print unsorted array first
        System.out.println(System.lineSeparator());
        System.out.println("My unsorted array:");
        System.out.println(Arrays.toString(data));
        System.out.println(System.lineSeparator());
        
        // call method using class name
        SimpleBubbleSort.bubbleSort(data); 
        System.out.println("Sorted array:");
        System.out.println(Arrays.toString(data));
        System.out.println(System.lineSeparator());
    }
}