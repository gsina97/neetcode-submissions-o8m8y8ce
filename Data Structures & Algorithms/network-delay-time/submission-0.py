class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        t = 0
        visited = set()

        adj = {i:[] for i in range(1, n + 1)}

        
        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]

        while minHeap:
            w1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)
            t = max(t, w1)
            for node2, w2 in adj[node1]:
                heapq.heappush(minHeap, (w2 + w1, node2))
        
        return t if n == len(visited) else - 1
 