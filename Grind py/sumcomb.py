def combinationSum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])  # Make a copy of path
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # Not i+1 because we can reuse
            path.pop()  # Undo last choice (backtrack)

    backtrack(0, [], 0)
    return result


# === Entry point ===
if __name__ == "__main__":
    # Input handling
    candidates = list(map(int, input("Enter candidate numbers (space-separated): ").split()))
    target = int(input("Enter target value: "))

    # Call the function
    combinations = combinationSum(candidates, target)

    # Output result
    print("\nCombinations that sum to target:")
    for combo in combinations:
        print(combo)
