class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0 
    

        for r in range(1, len(prices)):

            prof = prices[r] - prices[l]
            maxProf = max(maxProf, prof)

            if prices[r] < prices[l]:
                l = r
        
        return maxProf
