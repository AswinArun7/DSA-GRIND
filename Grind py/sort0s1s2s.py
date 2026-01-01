nums=[2,0,2,1,1,0]
low,mid,high=0,0,len(nums)-1
while mid<=high:
    if nums[mid]==0:
        nums[low],nums[mid]=nums[mid],nums[low]
        low+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    else:
        nums[high],nums[mid]=nums[mid],nums[high]
        high-=1        
        

# c0,c1,c2=0,0,0
# for i in range(len(nums)):
#     if nums[i]==0:
#         c0+=1
#     elif nums[i]==1:
#         c1+=1
#     else:
#         c2+=1
# for j in range(c0):
#     nums[j]=0
# for k in range(c0,c0+c1):
#     nums[k]=1
# for l in range(c0+c1,len(nums)):
#     nums[l]=2                        

print(nums)        