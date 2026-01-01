s=list(input("Enter the str:"))
seen=[]
for i in s:
    if i in seen:
        print(i)
        break
    seen.append(i)
else:
    print("no repeat")
