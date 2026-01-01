def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    used = [False] * len(nums)
    backtrack([], used)
    return result


# -------------------------------
# 🔽 User Input and Execution 🔽
# -------------------------------

if __name__ == "__main__":
    # Example input: 1 2 3
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    
    permutations = permute(nums)
    
    print("\nAll permutations:")
    for p in permutations:
        print(p)
