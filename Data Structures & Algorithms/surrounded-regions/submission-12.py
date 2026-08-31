class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # from edges, mark the Os.
        #  do bfs from those Os in the edges, and spread to Other Os, and mark them.
        # go over board, and covnert unmarked Os


        visited = set()

        rows = len(board)
        cols = len(board[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or c == 0 or r == rows -1 or c == cols -1):
                    q.append((r,c))
                    # visited.add((r,c))
        
    
        directions = [(0, 1), (0, -1), (1, 0), (-1 , 0)]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                visited.add((r,c))

                for x,y in directions:
                    newR, newC = r+ x, c+y

                    if newR < rows and newC < cols and newR >= 0 and newC >= 0 and (newR,newC) not in visited and board[newR][newC] == "O":
                        q.append((newR, newC))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"