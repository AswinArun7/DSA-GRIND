#include <bits/stdc++.h>
using namespace std;
int partition(vector<int>&arr, int low, int high){
    int pivot=arr[low];
    int i=low+1;
    for (int j=low+1;j<high+1;j++){
        if (arr[j]<pivot){
            swap(arr[i],arr[j]);
            i++;
        }
    }    
    swap(arr[low],arr[i-1]);
    return i-1;
    
}
void quicksort(vector<int>&arr, int low, int high){
    if (low < high){
        int pivot=partition(arr, low, high);
        quicksort(arr, low, pivot - 1);
        quicksort(arr, pivot + 1, high);
    }
}
int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    quicksort(arr, 0, arr.size() - 1);
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
}