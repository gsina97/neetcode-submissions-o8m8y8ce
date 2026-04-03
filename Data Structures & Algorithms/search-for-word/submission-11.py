class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])


        visited = set()
        def dfs(i,j, idx):
            if idx == len(word):
                return True
            if (i,j) in visited or i == rows or j == cols or i < 0 or j < 0 or board[i][j] != word[idx]:
                return False

            visited.add((i,j))
            found = dfs(i + 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i , j - 1, idx + 1)
            visited.remove((i,j))
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False

            