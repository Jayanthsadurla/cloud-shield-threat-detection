#include <iostream>
using namespace std;

int binary_search(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    int arr[1000]; 
    cout << "Enter sorted array elements separated by space: ";
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    int target;
    cout << "Enter the target value: ";
    cin >> target;
    int index = binary_search(arr, n, target);
    cout << "Index: " << Index << endl;
    return 0;
}
