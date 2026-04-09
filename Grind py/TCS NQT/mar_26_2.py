# Minimum Adjacent Swaps to Convert One Array to Another

# def max_swaps(S,X):                   => time complexity O(n^2) and space complexity O(1)
#     swaps=0
#     n=len(S)
#     for i in range(n):
#         if S[i] != X[i]:
#             j=i+1

#             while j<n and S[j]!=X[i]:
#                 j+=1

#             while j>i:
#                 S[j],S[j-1]=S[j-1],S[j]
#                 j-=1
#                 swaps+=1
#     return swaps                

# S=list(map(int, input().split()))
# X=list(map(int, input().split()))
# print(max_swaps(S,X))



# BETTER SOLUTION

def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort_count(arr[:mid])
    right, inv_right = merge_sort_count(arr[mid:])

    merged = []
    i = j = inv_split = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_split += len(left) - i   # 🔥 KEY LINE
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged, inv_left + inv_right + inv_split


def min_adjacent_swaps(S, X):
    pos = {value: i for i, value in enumerate(X)}
    arr = [pos[x] for x in S]

    _, swaps = merge_sort_count(arr)
    return swaps