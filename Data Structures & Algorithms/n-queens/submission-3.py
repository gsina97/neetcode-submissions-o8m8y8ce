class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        board = [["."] * n for i in range(n)]


        cols = set()
        posDiag = set()
        negDiag = set()
        res =[]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return


            for c in range(n):

                if c in cols or (c + r) in negDiag or (r - c) in posDiag:
                    continue
                
                cols.add(c)
                negDiag.add(c + r)
                posDiag.add(r - c)
                board[r][c] = "Q"
                dfs(r+1)
                board[r][c] = "."
                cols.remove(c)
                negDiag.remove(c + r)
                posDiag.remove(r - c)
            return
        
        dfs(0)
        return res