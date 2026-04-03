class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProf = 0

        for r in range(len(prices)):
            if r == 0:
                continue
            amount = prices[r] - prices[l]
            maxProf = max(maxProf, amount)

            if prices[l] > prices[r]:
                l = r
        return maxProf

        