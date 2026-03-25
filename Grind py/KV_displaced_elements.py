#FIND ALl the displaced elements in an array.
#An element is displaced if there is an element greater than it on the left,
#and an element smaller than it on the right.


# def displaced(arr):           complexity O(n^2)
#     d=[]
#     for i in range(1,len(arr)-1):
#         j=0;k=i+1
#         l,r=0,0
#         while j<i:
#             if arr[j]>arr[i]:
#                 l=1
#                 break
#             j+=1
#         while k<len(arr):
#             if arr[k]<arr[i]:
#                 r=1
#                 break
#             k+=1
#         if l==1 and r==1:
#             d.append(arr[i])
#     return d    


# optimized approach with complexity O(n)
def displaced(arr):
    n=len(arr)
    l_max=[0]*n
    r_min=[0]*n

    l_max[0]=arr[0]
    for i in range(1,n):
        l_max[i]=max(l_max[i-1],arr[i])

    r_min[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        r_min[i]=min(r_min[i+1],arr[i])

    d=[]
    for i in range(1,n-1):
        if l_max[i-1]>arr[i] and r_min[i+1]<arr[i]:
            d.append(arr[i])
    return d        

arr=[4,7,3,6,1,5]

r=displaced(arr)
print(r)