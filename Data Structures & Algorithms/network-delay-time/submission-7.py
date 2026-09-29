class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append([vi, ti])
        
        heap = []
        heapq.heappush(heap, [0,k])

        visited = {}
        visited[k] = 0
        total = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if visited[node] < dist:
                continue
            
            for nei, t in adj[node]:
                newdist = t + dist
                if newdist < visited.get(nei, float("inf")):
                    heapq.heappush(heap, [newdist, nei])
                    visited[nei] = newdist
        return max(visited.values()) if len(visited) == n else -1