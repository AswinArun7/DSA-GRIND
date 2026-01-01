nums=[-2,1,-3,4,-1,2,1,-5,4]
mx=float('-Inf')
curr_sum=0
start=0
for i in range(len(nums)):
    
    curr_sum+=nums[i]
    if curr_sum>mx:
        mx=curr_sum
        ans_start=start
        ans_end=i
    if curr_sum<0:
        curr_sum=0
        start=i+1

print(nums[ans_start:ans_end+1])        