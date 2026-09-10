class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        rows = len(board)
        cols = len(board[0])

        q = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or c == 0 or r == rows - 1 or c == cols - 1):
                    q.append((r,c))
                    visited.add((r,c))


        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:

                newR, newC = dr + r, dc + c
                
                if newR < 0 or newC < 0 or newR == rows or newC == cols or board[newR][newC] != "O" or (newR, newC) in visited:
                    continue
                q.append((newR,newC))
                visited.add((newR, newC))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
        
                