#include <bits/stdc++.h>
using namespace std;
void insertionsort(vector<int>&arr){
        int j;
        for(int i=1;i<arr.size();i++){
            j=i;
            while(j>0 && arr[j]<arr[j-1]){
                swap(arr[j],arr[j-1]);
                j--;
            }
        }
}


int main(){
    int n;
    cin>>n;
    vector<int>arr(n);
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    insertionsort(arr);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}