words=input("Enter the words").split()
grouped={}
for i in words:
    fl=i[0]
    if fl in grouped:
        grouped[fl].append(i)
    else:
        grouped[fl]=[i]
print(grouped)