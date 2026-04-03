class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def dfs(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            res = (dfs(i + 1, curr_sum - nums[i]) + dfs(i + 1, curr_sum + nums[i]))
            cache[(i, curr_sum)] = res
            return res
        
        return dfs(0,0)