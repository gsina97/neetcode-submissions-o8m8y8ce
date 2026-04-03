class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while r >= l:
            m = (l + r) // 2

            row = m // COLS
            cols = m % COLS
            val = matrix[row][cols]
            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True
        return False