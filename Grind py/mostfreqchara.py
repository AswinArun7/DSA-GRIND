n=input("Enter the str:")
max_c=0
chr=""
for i in n:
    count=n.count(i)
    if count>max_c:
        max_c=count
        chr=i
print(chr)        