class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            
            for j in range(i + 1, min(nums[i] + 1 + i, n)):
                dp[j] = True

        print(dp)
        return dp[-1]
            
