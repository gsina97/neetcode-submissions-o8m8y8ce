class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        cache = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("+inf")
            if rem in cache:
                return cache[rem]
            
            res = float("+inf")
            for c in coins:
                res = min(res, 1 + dfs(rem - c))
            
            cache[rem] = res
            return res

            
        r = dfs(amount)
        return r if r != float("+inf") else -1



                