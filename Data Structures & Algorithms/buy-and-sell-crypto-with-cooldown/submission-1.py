class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if buy -> i + 1
        # if sell -> i + 2

        caching = {} # key= (i, buying=Bool) , val = maxProfit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in caching:
                return caching[(i, buying)]
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                caching[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, False) 
                caching[(i, buying)] = max(sell, cooldown)
            return caching[(i, buying)]
        
        return dfs(0,True)