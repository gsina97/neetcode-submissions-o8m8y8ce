class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        numToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        
        def backtrack(i, subStr):
            if i == len(digits):
                res.append(subStr)
                return
            

            for c in numToChar[digits[i]]:
                backtrack(i + 1, subStr + c)
        
        if digits:
            backtrack(0, "")

        return res
