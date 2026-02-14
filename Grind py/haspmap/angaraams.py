s=input("Enter the str:").lower().split()

# if sorted(s[0])==sorted(s[1]):
#     print(True)
# else :
#     print(False)

# efficient approach
def anagram(s):
    if len(s[0])!=len(s[1]):
        return False
    
    count={}
    for i in s[0]:
        count[i]=count.get(i,0)+1
    for i in s[1]:
        if i not in count or count[i]==0:
            return False
            break
        count[i]-=1
    return True    

anagram(s)
print(anagram(s))


