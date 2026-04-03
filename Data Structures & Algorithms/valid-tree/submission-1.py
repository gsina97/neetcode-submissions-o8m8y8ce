class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        adj = {i:[] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

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

        return dfs(0,-1) and n == len(visited)