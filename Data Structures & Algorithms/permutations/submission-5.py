class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        s = []
        def dfs():
            if len(s) == len(nums):
                res.append(s[:])
                

            for n in nums:
                if n not in s:
                    s.append(n)
                    dfs()
                    s.pop()
        dfs()
        return res

