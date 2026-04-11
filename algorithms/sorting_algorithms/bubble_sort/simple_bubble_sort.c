// Bubble sort in C

#include <stdio.h>

// perform the bubble sort
void bubbleSort(int arr[], int n) {

    // loop to access each array element
    for (int step = 0; step < n - 1; ++step) {

        // loop to compare each adjacent element in the array
        for (int i = 0; i < n - step - 1; ++i) {

            // compare two adjacent elements 
            if (arr[i] > arr[i + 1]) {

                // swap if elements meet the target condition
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }
}

// print sorted array
void printArray(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

}

int main() {
    int data[] = {456, 41, 2, 67, 43, 4, 25, 8};

    // find the array's length
    int size = sizeof(data) / sizeof(data[0]);

    // print unsorted array
    printf("\nUnsorted array:");
    printf("\n");
    printArray(data, size);
    printf("\n");

    // run the data through the algorithm
    bubbleSort(data, size);

    // print the sorted array
    printf("Sorted array:\n");
    printArray(data,size);
    printf("\n");

    fflush(stdout);
    return 0;
}

