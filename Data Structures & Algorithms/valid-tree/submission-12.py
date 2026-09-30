class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)


        q = deque()
        q.append((0, None))
        visited= set()
        visited.add(0)

        while q:
            node, prev = q.popleft()

            for nei in adj[node]:
                if nei != prev:
                    if nei in visited:
                        return False
                    q.append((nei, node))
                    visited.add(nei)
        
        return len(visited) == n


