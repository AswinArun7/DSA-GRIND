n=input("Enter the str:")
words=n.split()
f={}

for i in words:
    # if i in f:
    #     f[i]+=1
    # else:
    #     f[i]=1
    f[i]=f.get(i,0)+1
print(f)            

