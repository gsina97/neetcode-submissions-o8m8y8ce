class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            else:
                l = r
            r += 1
        
        return maxProfit