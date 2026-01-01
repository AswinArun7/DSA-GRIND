x=set(map(int,input("Enter set 1:").split()))
y=set(map(int,input("Enter set 2:").split()))
z=set(map(int,input("Enter set 3:").split()))

c=x & y & z

print(c)

#two pointer method for intersection of sorted arrays
# def intersectionSorted(arr1, arr2):
    # i = j = 0
    # res = []

    # while i < len(arr1) and j < len(arr2):
    #     if arr1[i] < arr2[j]:
    #         i += 1
    #     elif arr1[i] > arr2[j]:
    #         j += 1
    #     else:
    #         # equal elements
    #         if not res or res[-1] != arr1[i]:
    #             res.append(arr1[i])
    #         i += 1
    #         j += 1

    # return res

    
 
