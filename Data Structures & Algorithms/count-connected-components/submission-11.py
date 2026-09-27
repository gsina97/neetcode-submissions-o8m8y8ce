class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def bfs(node):
            
            q = deque()
            q.append(node)

            while q:
                node = q.popleft()
                visited.add(node)

                for nei in adj[node]:
                    if nei not in visited:
                        q.append(nei)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                bfs(i)
        
        return res