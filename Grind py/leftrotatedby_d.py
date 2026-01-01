arr = [1, 2, 3, 4, 5, 6, 7]
n=len(arr)
d=int(input("Enter number of rotations: "))
d=d%n
temp = []
for i in range(d):
    temp.append(arr[i])

for i in range(d,len(arr)):
    arr[i-d] = arr[i]

j=0
for i in range(n-d,n):
    arr[i] = temp[j]
    j += 1
print(*arr)

# EASY PY METHOD
# n=len(arr)
# d=int(input("Enter number of rotations: ")) 
# d=d%n
# arr=arr[d:]+arr[:d]
# print(*arr)

# most used left  rotate method reverse
# arr[:d]=reversed(arr[:d])
# arr[d:]=reversed(arr[d:])
# arr.reverse()
# print(*arr)