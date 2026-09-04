class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for src, target, cost in times:
            adj[src].append([cost, target])
        


        heap = []
        heapq.heappush(heap, [0, k])
        shortest = {}

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for w2, n2 in adj[n1]:
                heapq.heappush(heap, [w1+ w2, n2])
        
        
        if len(shortest) !=n:
            return -1
        
        return max(shortest.values())
        
