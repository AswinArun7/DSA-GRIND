nums=[-2,1,-3,4,-1,2,1,-5,4]
# mx=float('-Inf')
# for i in range(len(nums)):
#     curr_sum=0
#     for j in range(i,len(nums)):
#         curr_sum+=nums[j]
#         mx=max(mx,curr_sum)

# kadane's Algorithm 1way->>>

# mx=float('-Inf')
# curr_sum=0
# for i in nums:
#     curr_sum+=i
#     mx=max(mx,curr_sum)
#     if curr_sum<0:
#         curr_sum=0


# kadane's Algorithm another way->>

mx=float('-Inf')
curr_sum=0
for i in nums:
    curr_sum=max(i,curr_sum+i)
    mx=max(mx,curr_sum)







print(mx)        