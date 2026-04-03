class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        s = set()

        def dfs(c, r, idx):
            if idx == len(word):
                return True
            if c < 0 or r < 0 or c >= COLS or r >= ROWS or word[idx] != board[r][c] or (c, r) in s:
                return False
            

            s.add((c,r))

            res = (dfs(c+1, r, idx + 1) or
            dfs(c, r + 1, idx + 1) or
            dfs(c - 1, r, idx + 1) or
            dfs(c, r - 1, idx + 1))
            
            s.remove((c,r))
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(c, r, 0):
                    return True
        
        return False