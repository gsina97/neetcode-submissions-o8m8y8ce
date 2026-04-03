class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # row = [1] * n

        # for i in range(m - 1):
        #     newRow = [1] * n
        #     for j in range(n - 2, -1 , -1):
        #         newRow[j] = newRow[j + 1] + row[j]
        #     row = newRow
        # return row[0]

        dp= []
        for _ in range(m):
            dp.append([0] * n)
        
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                
                left = dp[i][j -1] if j - 1 >= 0 and j -1 < n else 0
                up = dp[i - 1][j] if i - 1 >= 0 and i -1 < m else 0
                dp[i][j] = left + up
        
        return dp[m - 1][n - 1]