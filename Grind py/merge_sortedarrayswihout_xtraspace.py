nums1=[1,3,5,7]
nums2=[0,2,6,8,9]
m=len(nums1)
n=len(nums2)

# Without extra space
l,r=m-1,0
while l>=0 and r<n:
    if nums1[l]>nums2[r]:
        nums1[l],nums2[r]=nums2[r],nums1[l]
        l-=1
        r+=1
    else:
        break    
nums1.sort()
nums2.sort()        

# Take extra space (not allowed as per question)
# l,r=0,0
# nums3=[]
# while l<m and r<n:
#     if nums1[l]<=nums2[r]:
#         nums3.append(nums1[l])
#         l+=1
#     else:
#         nums3.append(nums2[r])
#         r+=1
    

# while l<m:
#     nums3.append(nums1[l])
#     l+=1

# while r<n:
#     nums3.append(nums2[r])
#     r+=1

# for i in range(len(nums3)):
#     if i<m:
#         nums1[i]=nums3[i]
#     else:
#         nums2[i-m]=nums3[i]



print(nums1)
print(nums2)        