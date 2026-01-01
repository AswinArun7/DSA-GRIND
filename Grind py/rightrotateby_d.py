arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = int(input("Enter number of rotations: "))
d = d % n
# arr = arr[-d:] + arr[:-d]  or arr[:]= arr[-d:] + arr[:-d]  arr[:]->modifies the original array
# print(*arr)

# WITHOUT EASY PY METHOD most used ROTATE method UUSING REVERSE
arr.reverse()
arr[:d] = reversed(arr[:d])
arr[d:] = reversed(arr[d:])
print(*arr)