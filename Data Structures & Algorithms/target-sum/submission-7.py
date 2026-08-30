from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        @cache
        def dfs(i, s1):
            if i == len(nums) and s1==target:
                return 1
            elif i == len(nums):
                return 0
            

            r1 = dfs(i + 1, s1 + nums[i])

            r2 = dfs(i + 1, s1 - nums[i])

            return r1 + r2
        
        return dfs(0,0)