from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        
        @cache
        def dfs(i,s1, s2):
            if i == len(nums):
                if s1 == s2:
                    return True
                return False
            

            r1 = dfs(i + 1, s1+ nums[i], s2)

            r2 = dfs(i + 1, s1, s2 + nums[i])

            return r1 or r2
        
        return dfs(0,0,0)
        
            
