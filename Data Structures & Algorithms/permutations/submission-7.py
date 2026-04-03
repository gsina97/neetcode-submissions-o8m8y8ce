class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []

        def dfs(i):
            if i == len(nums):
                res.append(curr[:])
                return

            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs(i + 1)
                    curr.pop()
            
                
        dfs(0)
        return res