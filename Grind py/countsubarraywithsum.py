nums=[1,2,3]
k=3
prefixsum=0
count=0
seen={0:1}
for i in range(len(nums)):
    prefixsum+=nums[i]
    if prefixsum-k in seen:
        count+=seen[prefixsum-k]
    seen[prefixsum]=seen.get(prefixsum,0)+1
print(count)    