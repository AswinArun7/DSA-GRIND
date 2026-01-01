x=input("Enter the Sentence:")
vowels='aeiouAEIOU'
count=0
for i in x:
    if i in vowels:
        count+=1

print(count)