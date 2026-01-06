nums=[100,4,200,1,102,3,2,101]
nums.sort()
count=0
longest=1
ls=float('-inf')
for i in range(len(nums)):
    if nums[i]-1 ==ls:
        count+=1
        ls=nums[i]
    elif nums[i]-1 !=ls:
        count=1
        ls=nums[i]
    longest=max(longest,count)    
print(longest)     