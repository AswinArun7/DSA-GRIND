nums=[0,1,2,3,5]
# for i in range(len(nums)+1):
#     if i not in nums:
#         break
# return i


# n=len(nums)
# res=n
# for i in range(n):
#     res=res^i
#     res=res^nums[i]
# return res    

n=len(nums)
r=[0]*(n+1)
for i in range(n):
    r[nums[i]]=1
for j in range(n+1):
    if r[j]==0:
        print(j)        
        break  

# n = len(nums)
# expected = n * (n + 1) // 2
# return expected - sum(nums)

