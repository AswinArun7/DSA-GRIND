# MAX PDT FROM SUBSETS

# arr=list(map(int,input().split()))
# arr.sort()
# max_pd=0
# curr_pd=1
# for i in arr:
#     if i==0:
#         if max_pd<0:
#             max_pd=0
#         continue
#     else:
#         curr_pd*=i
#         max_pd=max(max_pd,curr_pd)
# print(max_pd)

# BETTER SOLUTION

arr = list(map(int, input().split()))

product = 1
count_neg = 0
max_neg = float('-inf')
zero_count = 0

for x in arr:
    if x == 0:
        zero_count += 1
        continue

    if x < 0:
        count_neg += 1
        max_neg = max(max_neg, x)

    product *= x

# If all elements are zero
if zero_count == len(arr):
    print(0)

# If odd negatives → remove largest negative
elif count_neg % 2 == 1:
    # Special case: only one negative and rest zeros
    if count_neg == 1 and zero_count > 0 and count_neg + zero_count == len(arr):
        print(0)
    else:
        print(product // max_neg)

else:
    print(product)