def countv(n):
    c=0
    vow="aeiouAEIOU"
    for i in n:
        if i in vow:
            c+=1
    return c
text=input("Enter:")
r=countv(text)
print(r)        

    