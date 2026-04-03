class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        cache = {}
        def dfs(i, target):
            if (i,target) in cache:
                return cache[(i, target)]
            if i == len(nums):
                return target == 0
            if target < 0:
                return False
            
            cache[(i, target)] = dfs(i + 1, target - nums[i]) or  dfs(i + 1, target)
            return cache[(i, target)]

        
        return dfs(0, sum(nums) // 2)