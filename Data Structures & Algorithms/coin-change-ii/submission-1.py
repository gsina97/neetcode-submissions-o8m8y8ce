class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        


        cache = {}

        def dfs(i, rem):
            if rem == 0:
                return 1
            elif (i, rem) in cache:
                return cache[(i, rem)]
            elif rem < 0 or i == len(coins):
                return 0

            
            res = dfs(i + 1, rem) + dfs(i, rem-coins[i])

            cache[(i, rem)] = res
            return res
        
        return dfs(0,amount)