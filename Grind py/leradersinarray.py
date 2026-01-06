nums=[10,22,12,3,0,6]
max=float('-inf')
l=[]
for i in range(len(nums)-1,-1,-1):
    if nums[i]>max:
        max=nums[i]
        l.append(nums[i])
print(l[::-1])