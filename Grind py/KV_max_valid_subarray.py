def max_valid_subarray(arr,k):
    n=len(arr)
    max_len=0
    for i in range(n):
        for j in range(i,n):
            sub =arr[i:j+1]
            s=sum(sub)
            if s<k and not ap_sub(sub):
                max_len=max(max_len,len(sub))

    return max_len            

def ap_sub(sub):
    if len(sub)<2:
        return False  
    d=sub[1]-sub[0]
    for i in range(2,len(sub)):
        if sub[i]-sub[i-1]!=d:
            return False
    return True
#Optimized approach using sliding window and hashmap to track differences.O(n) time complexity.

# from collections import defaultdict
# def max_valid_subarray(arr, K):
#     left = 0
#     curr_sum = 0
#     max_len = 0
#     diff_count = defaultdict(int)

#     for right in range(len(arr)):
#         curr_sum += arr[right]

#         # add new difference
#         if right > 0:
#             d = arr[right] - arr[right-1]
#             diff_count[d] += 1

#         # CONDITION 1: sum must be < K
#         while curr_sum >= K:
#             if left+1 <= right:
#                 d = arr[left+1] - arr[left]
#                 diff_count[d] -= 1
#                 if diff_count[d] == 0:
#                     del diff_count[d]
#             curr_sum -= arr[left]
#             left += 1

#         # CONDITION 2: must not be arithmetic progression
#         while (right-left+1) >= 3 and len(diff_count) == 1:
#             d = arr[left+1] - arr[left]
#             diff_count[d] -= 1
#             if diff_count[d] == 0:
#                 del diff_count[d]
#             curr_sum -= arr[left]
#             left += 1

#         max_len = max(max_len, right-left+1)

#     return max_len


arr=[1,2,4,5,7]
k=10
r=max_valid_subarray(arr,k)
print(r)  