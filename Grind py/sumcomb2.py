def combinationSum2(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result

# ---- User Input Section ----
candidates = list(map(int, input("Enter the candidates (space-separated): ").split()))
target = int(input("Enter the target value: "))

# ---- Execution ----
combinations = combinationSum2(candidates, target)

# ---- Output ----
print("Unique combinations that sum to", target, "are:")
for combo in combinations:
    print(combo)
