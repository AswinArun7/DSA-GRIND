# MAX PDT FROM SUBARRAYS

def max_product_subarray(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]

        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, num * max_prod)
        min_prod = min(num, num * min_prod)

        result = max(result, max_prod)

    return result

arr=list(map(int, input().split()))
print(max_product_subarray(arr))