class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total = 0

        visited = set()

        adj = {i:[] for i in range(n)}

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)

            for node in adj[i]:
                if node in visited:
                    continue
                dfs(node)
            return

        for i in range(n):
            if i not in visited:
                total += 1
                dfs(i)

        return total