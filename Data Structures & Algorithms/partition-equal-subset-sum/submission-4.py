class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        self.s1 = 0
        self.s2 = 0

        cache = {}
        def dfs(i, s1, s2):
            if (i, s1, s2) in cache:
                return cache[(i, s1, s2)]
            if i == len(nums) and s1 == s2:
                return True
            if i == len(nums):
                return False
            

            r1 = dfs(i + 1, s1 + nums[i], s2)

            r2 = dfs(i + 1,  s1, s2 + nums[i])


            res = r2 or r1
            cache[(i,s1,s2)] = res
            return res
        
        return dfs(0,0,0)