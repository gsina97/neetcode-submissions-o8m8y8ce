class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for i in range(n)]

        res = []
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            
            for c in range(n):
                if c in cols or (c+r) in posDiag or (c - r ) in negDiag:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(c+r)
                negDiag.add(c - r)
                dfs(r + 1)
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(c+r)
                negDiag.remove(c - r)
        dfs(0)
        return res
