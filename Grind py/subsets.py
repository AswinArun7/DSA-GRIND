class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

# Test
solution = Solution()
nums = [1, 2, 3]
print("Subsets for:", nums)
print(solution.subsets(nums))
