def addbinarynos(a,b):
    
    carry=0
    i,j=len(a)-1,len(b)-1
    r=[]
    while i>=0 or j>=0 or carry:
        sum=carry
        if i>=0:
            sum+=int(a[i])
            i-=1
        if j>=0:
            sum+=int(b[j])
            j-=1
        carry=sum//2
        r.append(str(sum%2))
    return ''.join(r[::-1])

a=input("Enter the first binary number:")
b=input("Enter the second binary number:")
print(addbinarynos(a,b))
        


