nums=[3,-2,5,-1,4,-3]
p=[]
n=[]
for i in nums:
    if i>0:
        p.append(i)
    else:
        n.append(i)
    i,j=0,0
    k=0
# while k<len(nums):
#     nums[k]=p[i]
#     i+=1
#     k+=1
#     nums[k]=n[j]
#     j+=1  
#     k+=1

for i in range(len(p)):
    nums[2*i]=p[i]
    nums[2*i+1]=n[i]

print(nums)