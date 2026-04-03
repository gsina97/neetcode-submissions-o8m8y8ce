class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}
        def dfs(i, rem):
            if (i,rem) in cache:
                return cache[(i,rem)]
            if rem == 0:
                return 1
            if i == len(coins) or rem < 0:
                return 0

            res = dfs(i, rem - coins[i])  +dfs(i + 1, rem )
            cache[(i,rem)] = res
            return res
        return dfs(0,amount)