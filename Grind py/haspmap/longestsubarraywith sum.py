nums = [1, 2, 3, 1, 1, 1]
k=3
prefix_sum = 0
max_length = 0
seen={}
for i in range(len(nums)):
    prefix_sum+=nums[i]

    if prefix_sum==k:
        max_length=i+1

    if prefix_sum-k  in seen:
        max_length=max(max_length,i-seen[prefix_sum-k])

    if prefix_sum  not in seen:
        seen[prefix_sum]=i

print(max_length)        

# Two pointer approach - Sliding Window

# nums = [1, 2, 3, 1, 1, 1]
# k = 3

# left = 0
# sum = 0
# max_length = 0

# for right in range(len(nums)):
#     sum += nums[right]

#     while sum > k and left <= right:
#         sum -= nums[left]
#         left += 1

#     if sum == k:
#         max_length = max(max_length, right - left + 1)

# print(max_length)
