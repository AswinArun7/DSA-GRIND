n=list(map(int,input("Enter:").split()))
x=len(n)
y=len(set(n))
if x==y:
    print(False)
else:
    print(True)    