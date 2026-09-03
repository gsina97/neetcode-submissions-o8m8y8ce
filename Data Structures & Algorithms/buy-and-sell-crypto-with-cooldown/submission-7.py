from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        @cache
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            if canBuy:

                buy = dfs(i + 1, False) - prices[i]
                
                wait = dfs(i + 1, True)

                res = max(buy, wait)
                
                return res
            else:
                # if i can sell
                sell = dfs(i + 2, True) + prices[i]

                # wait
                wait = dfs(i + 1, False)
                res = max(wait, sell)
                
                return res

        return dfs(0, True)
