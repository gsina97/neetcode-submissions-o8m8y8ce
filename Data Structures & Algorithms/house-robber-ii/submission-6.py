class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        
        return max(self.split(nums[0:n - 1]), self.split(nums[1:n]))
        


    def split(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        elif n == 2:
            return max(arr[0], arr[1])
        
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + arr[i], dp[i -1])

        return dp[-1]