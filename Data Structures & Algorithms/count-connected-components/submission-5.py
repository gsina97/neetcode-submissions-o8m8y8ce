class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()


        adj = {i:[] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        
        def dfs(i):
            if i in visited:
                return

            visited.add(i)
            for nei in adj[i]:
                if nei in visited:
                    continue
                dfs(nei)
            return
        
        res =0 
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res

