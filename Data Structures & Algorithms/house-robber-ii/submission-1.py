class Solution:
    def rob(self, nums: List[int]) -> int:
        x = len(nums)
        if x == 1:
            return nums[0]

        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]

            dp = [0] * n

            dp[0] = arr[0]
            dp[1] = max(arr[1], arr[0])

            for i in range(2, n ):
                dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
            
            return dp[-1]

        res = max(helper(nums[1:]), helper(nums[:len(nums) - 1]))
        return res


