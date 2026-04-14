class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        res = 0
        b = 0
        for s in range(1, len(prices)):


            tmp = prices[s] - prices[b] 
            res = max(res, tmp)
            if tmp < 0:
                b = s
        
        return res