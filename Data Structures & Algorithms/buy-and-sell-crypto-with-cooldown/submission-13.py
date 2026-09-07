from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.res = 0


        @cache
        def dfs(canBuy, i):
            if i >= len(prices):
                return 0
            if canBuy:
                # buy
                a = dfs(False, i + 1) -  prices[i]

                b = dfs(True, i + 1)
                return max(a,b)
            else:
                # can sell or wait
                a = dfs(True, i + 2) + prices[i]

                # wait
                b= dfs(False, i + 1)

                return max(a,b)
        return dfs(True, 0)
            