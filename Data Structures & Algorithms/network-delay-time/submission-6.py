class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for ui,vi,ti in times:
            adj[ui].append([vi, ti])


        heap = [[0,k]]

        visited = set()
        res = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            res = max(res, cost)
            visited.add(node)
            for target, cost2 in adj[node]:
                if target in visited:
                    continue
                heapq.heappush(heap, [cost + cost2,target])

        
        return res if len(visited) == n else -1
        