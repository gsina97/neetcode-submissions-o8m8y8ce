class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        currMin, currMax = 1,1
        res = max(nums)

        for n in nums:
            temp = currMin
            currMin = min(currMin * n, currMax * n, n)
            currMax = max(temp * n, currMax * n, n)
            res = max(currMin, currMax, res)

        return res