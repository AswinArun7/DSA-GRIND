class Solution:
    def permuteUnique(self, nums):
        result = []
        nums.sort()
        
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue  # Skip duplicates
                
                path.append(nums[i])
                used[i] = True
                print(f"Choose {nums[i]} → Path: {path}")
                backtrack(path, used)
                used[i] = False
                path.pop()
                print(f"Backtrack {nums[i]} ← Path before pop: {path}")

        backtrack([], [False] * len(nums))
        return result


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    input_nums = [1, 1, 2]
    print("Unique Permutations:")
    output = sol.permuteUnique(input_nums)
    for perm in output:
        print(perm)
