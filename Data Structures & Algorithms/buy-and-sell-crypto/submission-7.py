class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        b, s = 0, 1
        maxProfit = 0
        while s < len(prices):
            maxProfit = max(maxProfit, prices[s] - prices[b])
            if prices[s] < prices[b]:
                b = s 
            s += 1
        
        return maxProfit
