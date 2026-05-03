class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adj = defaultdict(list)
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)

            for nei in adj[i]:
                dfs(nei)
            
            return
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res