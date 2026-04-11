// Implement Bubble Sort in C++ 

#include <iostream>

using namespace std;

// perform bubble sort
void bubbleSort(int arr[], int n) {

    // loop for accessing each array element
    for (int step = 0; step < n - 1; ++step) {

        // loop to compare array elements
        for (int i = 0; i < n - step - 1; ++i) {

            // compare two adjacent elements
            if (arr[i] > arr[i + 1]) {

                // swap elements if they meet the target condition 
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }
}

// print array 
void printArray(int arr[], int size) {

    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

int main() {
    int data[] = {456, 41, 2, 67, 43, 4, 25, 8};

    // find array's length 
    int size = sizeof(data) / sizeof(data[0]);

    // print the unsorted array
    cout << "\n";
    cout << "Unsorted array:\n";
    printArray(data,size);
    cout << "\n";

    // call the bubble sort function
    bubbleSort(data, size);

    // print the sorted array
    cout << "Sorted array:\n";
    printArray(data, size);
    cout << "\n";

    return 0;
}