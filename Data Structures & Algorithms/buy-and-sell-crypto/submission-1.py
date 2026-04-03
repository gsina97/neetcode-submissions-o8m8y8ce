class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l=buy, r= sell
        totalP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                totalP = max(totalP, prices[r] - prices[l]) 
            else:
                l = r
            r += 1


        return totalP