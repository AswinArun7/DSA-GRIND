n=input("Enter the sentence:").split()
x=[]
for i in n:
    rev=i[::-1]
    x.append(rev)
y=" ".join(x)
print(y)    
