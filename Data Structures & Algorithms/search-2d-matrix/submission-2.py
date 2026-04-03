class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, (rows * cols) -1

        while left <= right:
            mid = (left + right) // 2
            
            row = mid // cols
            col = mid % cols
            val = matrix[row][col]

            if val > target:
                right = mid - 1
            elif val < target:
                left = mid + 1
            else:
                return True
        return False