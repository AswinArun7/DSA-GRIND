nums=[3,3,4,2,4,4,2,4,4]
seen={}
for i in nums:
    seen[i] = seen.get(i, 0) + 1              
    if seen[i] > len(nums) // 2:
        print(i)
        break

# for i in nums:
#     if i in seen:
#         seen[i]+=1
#         if seen[i]>len(nums)//2:
#             print(i)
#             break
#     else:
#         seen[i]=1


# Moore's Voting Algorithm
# candidate=None
# count=0
# for i in nums:
#     if count==0:
#         candidate=i
#     if i==candidate:
#         count+=1
#     else:
#         count-=1

# if nums.count(candidate)>len(nums)//2:
#     print(candidate)