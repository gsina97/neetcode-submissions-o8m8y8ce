class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])

        def spread(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or board[r][c] != "O" or (r,c) in immune:
                return
            immune.add((r,c))     

            spread(r + 1, c)
            spread(r - 1, c)
            spread(r, c + 1)
            spread(r, c  - 1)

        immune = set()
        for r in range(rows):
            if board[r][0] == "O":
                # immune.add((r,0))
                spread(r,0)
            if board[r][cols - 1] == "O":
                # immune.add((r, cols - 1))
                spread(r, cols - 1)


        for c in range(cols):
            if board[0][c] == "O":
                # immune.add((0,c))
                spread(0,c)
            if board[rows - 1][c] == "O":
                # immune.add((rows-1, c))
                spread(rows-1, c)



        for r in range(rows):
            for c in range(cols):
                if (r,c) not in immune and board[r][c] == "O":
                    board[r][c] = "X"
        