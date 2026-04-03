class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.cache = {}
        def dfs(i, canBuy):
            if (i, canBuy) in self.cache:
                return self.cache[(i, canBuy)]
            if i >= len(prices):
                return 0
            elif canBuy:

                # will buy 
                buy = dfs(i + 1, False) - prices[i]

                # will wait
                wait = dfs(i + 1, True)

                res = max(buy, wait)
                self.cache[(i, canBuy)] = res
                return res
            else:
                wait = dfs(i + 1, False)
                # sell
                sell = dfs(i + 2, True) + prices[i]

                res = max(wait, sell)
                self.cache[(i, canBuy)] = res
                return res
        return dfs(0, True)