#include <bits/stdc++.h>
using namespace std;
void mergesort(vector<int>&arr){
    if(arr.size()>1){
        int mid= arr.size()/2;
        vector<int> left(arr.begin(), arr.begin() + mid);
        vector<int> right(arr.begin() + mid, arr.end());
        mergesort(left);
        mergesort(right);
        int i = 0, j = 0, k = 0;
        while(i < left.size() && j < right.size()){
            if(left[i] < right[j]){
                arr[k] = left[i];
                i++;
            }
            else{
                arr[k] = right[j];
                j++;
            }
            k++;
        }
        while(i < left.size()){
            arr[k] = left[i];
            i++;
            k++;
        }
        while(j < right.size()){
            arr[k] = right[j];
            j++;
            k++;
        }
    }

}
int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    mergesort(arr);
    for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
}