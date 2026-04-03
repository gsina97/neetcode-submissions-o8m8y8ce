class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        total = rows * cols

        l, r = 0, total - 1

        while l <= r:
            m = (r + l) // 2

            row = m // cols
            col = m % cols
            val = matrix[row][col]

            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True
        return False

