class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1st no cycles
        # all nodes within 1 tree (no disconnects)

        adj = {i:[] for i in range(n)}
        

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            

            visited.add(i)

            for node in adj[i]:
                if node == prev:
                    continue
                if not dfs(node, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)
