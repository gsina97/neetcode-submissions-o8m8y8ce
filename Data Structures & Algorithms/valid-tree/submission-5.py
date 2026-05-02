class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = 0
        visited = set()
        def has_cycle(node, parent):
            
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return True
                if has_cycle(nei, node):
                    return True
            return False
        
        if has_cycle(0, -1):
            return False
        
        return len(visited) == n