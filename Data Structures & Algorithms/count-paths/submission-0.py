class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # row = [1] * n

        # for i in range(m - 1):
        #     newRow = [1] * n
        #     for j in range(n - 2, -1 , -1):
        #         newRow[j] = newRow[j + 1] + row[j]
        #     row = newRow
        # return row[0]
        def paths(i,j):
            if i == j == 0:
                return 1
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                return paths(i, j - 1) + paths(i - 1, j)
        return paths(m-1, n -1)