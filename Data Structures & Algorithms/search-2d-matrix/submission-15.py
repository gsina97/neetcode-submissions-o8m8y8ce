class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])


        l, r = 0, (ROWS*COLS) - 1

        while r >= l:
            m = (r + l) // 2
            

            row = m // COLS
            col = m % COLS
            val = matrix[row][col]
            if val > target:
                r = m -1
            elif val < target:
                l = m + 1
            else:
                return True
        
        return False