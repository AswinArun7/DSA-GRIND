def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
arr=list(map(int, input().split()))
insertionsort(arr)
print(*arr)