from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            if i == len(coins):
                return 0
            

            r1 = dfs(i, rem - coins[i])
            r2 = dfs(i + 1, rem)

            return r1 + r2
        
        return dfs(0, amount)