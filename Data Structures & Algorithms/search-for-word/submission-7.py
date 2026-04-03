class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c, s, idx):
            if idx == len(word):
                return True
            if r == rows or c == cols or r < 0 or c < 0 or board[r][c] != word[idx] or (r,c) in s:
                return False
            
            s.add((r,c))
            res = dfs(r + 1, c, s, idx + 1) or  dfs(r , c+ 1, s, idx + 1) or  dfs(r - 1 , c, s, idx + 1) or  dfs(r , c-  1, s, idx + 1) 
            s.remove((r,c))
            return res 





        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c, set(), 0):
                        return True
        
        return False



