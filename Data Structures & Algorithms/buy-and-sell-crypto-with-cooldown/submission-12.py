from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.res = 0


        @cache
        def dfs(canBuy, i, curr):
            if i >= len(prices):
                self.res = max(self.res, curr)
                return
            
            if canBuy:
                # buy
                dfs(False, i + 1, curr-  prices[i])

                dfs(True, i + 1, curr)
            else:
                # can sell or wait
                dfs(True, i + 2, prices[i] + curr)

                # wait
                dfs(False, i + 1, curr)
            return
        dfs(True, 0, 0)
        return self.res
            