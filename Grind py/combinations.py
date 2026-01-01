def combine(n: int, k: int):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])  # Make a copy of path
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()  # Backtrack

    backtrack(1, [])
    return result


# === Entry Point ===
if __name__ == "__main__":
    # Input from user
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))

    # Get combinations
    combinations = combine(n, k)

    # Print result
    print("\nAll combinations:")
    print(combinations)
