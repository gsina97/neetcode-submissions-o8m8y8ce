class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        adj = defaultdict(list)
        for src, target, time in times:
            adj[src].append([target, time])

        
        heap = []

        shortest = {}
        heapq.heappush(heap, [0, k])

        while heap:
            cost, n1 = heapq.heappop(heap)

            if n1 in shortest:
                continue
            shortest[n1] = cost

            for target, t2 in adj[n1]:
                if target not in shortest:
                    heapq.heappush(heap, [cost+ t2, target])
        
        
        if len(shortest) != n:
            return -1
        
        res = 0
        for node, cost in shortest.items():
            res = max(res, cost)
        return res