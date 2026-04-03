class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l, r = 0, 1

        while r < len(prices):

            money = prices[r] - prices[l]
            maxP = max(maxP, money)
            if money < 0:
                l = r
            r += 1
        
        return maxP
