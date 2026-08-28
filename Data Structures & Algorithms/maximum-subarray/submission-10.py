class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            if i == 0:
                dp[0] = nums[i]
                continue
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        print(dp)
        return max(dp)