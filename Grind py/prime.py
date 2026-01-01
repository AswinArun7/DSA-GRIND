n=int(input("Enter the number:"))
if n==1:
    print("Neither Prime nor Composite")
else:
    for i in range(2,n-1):
        if n%i==0:
            print("Composite")
            break
    else:
        print("Prime")    

