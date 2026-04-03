class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = []

        for _ in range(m):
            dp.append([0] * n)
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                up = dp[i - 1][j] if i - 1 >= 0 else 0
                left = dp[i][j - 1] if j - 1 >= 0 else 0
                dp[i][j] = up + left
        
        return dp[m - 1][n -1]
