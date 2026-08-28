class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        cache = {}
        def dfs(i, s):
            if s == target and i == len(nums):
                return 1
            if i == len(nums) and s != target:
                return 0
            if (i, s) in cache:
                return cache[(i, s)]

            res = dfs(i + 1, s + nums[i]) + dfs(i + 1, s - nums[i])
            cache[(i, s)] = res
            return res
        
        return dfs(0,0)
        