def letterCombinations(digits: str):
    if not digits:
        return []

    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index: int, path: str):
        if index == len(digits):
            result.append(path)
            return

        possible = phone_map[digits[index]]
        for i in possible:
            backtrack(index + 1, path + i)

    backtrack(0, "")
    return result


n = input("Enter the digits: ")
combinations = letterCombinations(n)
print(combinations)
