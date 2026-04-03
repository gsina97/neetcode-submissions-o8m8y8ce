class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        
        def dfs(r,c, i, visited):
            if i == len(word):
                return True
            if r == rows or c == cols or r < 0 or c < 0 or board[r][c] != word[i] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = dfs(r + 1, c, i + 1, visited) or dfs(r - 1, c, i + 1, visited) or dfs(r , c+ 1, i + 1, visited) or dfs(r , c - 1, i + 1, visited)
            visited.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        return False

            