class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(i, i+nums[i] + 1):
                    if j == n - 1:
                        return True
                    dp[j] = True
        
        return False