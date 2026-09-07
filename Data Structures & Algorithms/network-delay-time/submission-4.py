class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for src, target, cost in times:
            adj[src].append([cost, target])

        
        q = []
        heapq.heappush(q, [0, k])

        shortest = {}

        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            
            for w2, n2 in adj[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(q, [w2+ w1, n2])
        
        if len(shortest) != n:
            return -1
        
        return max(shortest.values())
