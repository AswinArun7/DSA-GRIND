n=input("Enter the sentence:").lower()
cln=""
for i in n:
    if i.isalnum():
        cln +=i
if cln == cln[::-1]:
    print(True)
else:
    print(False)        