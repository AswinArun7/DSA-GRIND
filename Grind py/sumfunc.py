def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
num=int(input("Enter:"))  

if num<1:
    print("Enter valid")
else:    
    r=sum(num)  
    print(r)