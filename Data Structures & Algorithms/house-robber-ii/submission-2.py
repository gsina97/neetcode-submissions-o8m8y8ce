class Solution:
    def rob(self, nums: List[int]) -> int:
        
        x = len(nums)
        if x == 1:
            return nums[0]
        if x == 2:
            return max(nums[0], nums[1])

        def helper(array):
            n = len(array)
            if n == 1:
                return array[0]
            if n == 2:
                return max(array[0], array[1])

            dp = [0] * n
            dp[0] = array[0]
            dp[1] = max(array[0], array[1])

            for i in range(2,n):
                dp[i] = max(array[i] + dp[i - 2], dp[i - 1])
            
            return dp[-1]

        return max(helper(nums[:x - 1]), helper(nums[1:]))




        