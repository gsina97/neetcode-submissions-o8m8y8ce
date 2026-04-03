class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        
        rows, cols = len(board), len(board[0])

        survivors = set()
        
        def capture(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or board[r][c] != "O":
                return
            
            board[r][c] = "T"

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c  - 1)

        # (DFS) capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r,c)
        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O": # capture surrounded regions(O -> X)
                    board[r][c] = "X"
                elif board[r][c] == "T":  # uncapture unsurrounded regions (T -> O)
                    board[r][c] = "O"
        
        



        
