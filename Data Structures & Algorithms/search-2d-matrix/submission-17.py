class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while r >= l:
            m = (l + r) // 2

            rrow = m // cols
            ccol = m % cols
            val = matrix[rrow][ccol]

            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True
        return False