def even(n):
    c=0
    for i in range(1,n):
        if i%2==0:
            c+=1
    return c
num=int(input("Enter:"))
r=even(num)
print(r) 
