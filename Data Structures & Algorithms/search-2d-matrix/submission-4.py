class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows*cols) - 1

        while r >= l:
            mid = (r + l) // 2

            row = mid // cols
            col = mid % cols

            val = matrix[row][col]

            if val > target:
                r = mid - 1
            elif val < target:
                l = mid + 1
            else:
                return True
        
        return False