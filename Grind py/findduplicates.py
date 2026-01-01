n=list(map(int,input("Enter the nos:").split()))
seen=set()
d=set()
for i in n:
    if i in seen:
        d.add(i)
    else:
        seen.add(i)
print(list(d))            