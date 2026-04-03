class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj = {i:[] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        total = 0
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)

            for node in adj[i]:
                dfs(node)
            return True
        
        for i in range(n):
            if i not in visited:
                total += 1
                dfs(i)
        
        return total
