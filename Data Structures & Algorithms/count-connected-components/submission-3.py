class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total = 0


        visited = set()

        adj = {i:[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

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
                dfs(i)
                total += 1
        
        return total
