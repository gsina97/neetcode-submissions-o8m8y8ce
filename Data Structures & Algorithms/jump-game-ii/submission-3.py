class Solution:
    def jump(self, nums: List[int]) -> int:
        


        n = len(nums)

        dp = [float("inf")] * n
        dp[0] = 0

        for i in range(n):
            for j in range(i, i+nums[i] + 1):
                if j == n:
                    break
                dp[j] = min(dp[j], dp[i] + 1) 

        return dp[-1]