class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 

        res = 0

        # buy at 0
        # if we can find lower, buy that that price/
        # try sell

        
        b = 0

        for s in range(1,len(prices)):

            tmp = prices[s] - prices[b]
            res = max(res, tmp)
            if prices[s] < prices[b]:
                b = s
        
        return res