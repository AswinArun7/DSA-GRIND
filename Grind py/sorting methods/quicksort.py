def quicksort(arr,low,high):
    if low < high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    for j in range(low+1,high+1):
        if arr[j]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[low],arr[i-1]=arr[i-1],arr[low]    
    return i-1    

arr=[5,3,8,4,2,7,1,6]
quicksort(arr,0,len(arr)-1)
print(*arr)            
  