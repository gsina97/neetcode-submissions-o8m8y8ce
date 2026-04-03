class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memoization --->   cache- >    key= (idx, buying) value = profit

        cache = {}
        def dfs(i, buying):
            if (i, buying) in cache:
                return cache[(i, buying)]
            if i >= len(prices):
                return 0
            elif buying:
                buy = dfs(i + 1, False) - prices[i]
                wait = dfs(i + 1, True)
                res = max(buy, wait)
                cache[(i, buying)] = res
                return res
            else:
                # if im eligible to sell, i can sell now, take profit, and move 2 steps
                sell = dfs(i + 2, True) + prices[i]
                # 
                wait = dfs(i + 1, False)
                res = max(sell, wait)
                cache[(i, buying)] = res
                return res

        return dfs(0, True)