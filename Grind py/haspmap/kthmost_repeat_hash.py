nums=[1,2,2,3,3,3,4,4]
k=2
freq={}
for i in nums:
    freq[i]=freq.get(i,0)+1
sorted_items=sorted(freq.items(), key= lambda x: x[1], reverse=True)

if k<=len(sorted_items):
    print(sorted_items[k-1][0])
else:
    print("k is larger than the number of unique elements")    