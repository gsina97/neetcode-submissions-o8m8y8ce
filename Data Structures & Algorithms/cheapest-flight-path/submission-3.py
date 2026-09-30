class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        adj = defaultdict(list)

        for origin, dest, cost in flights:
            adj[origin].append([cost, dest])

        
        heap = []
        heapq.heappush(heap, [0, 0, src])
                            # price, stops, airport
                            
        k = k + 1
        best_stops = [float("inf")] * n 


        while heap:
            price, stops, airport = heapq.heappop(heap)
            if airport == dst and stops <= k:
                return price
            if stops > k or stops > best_stops[airport]:
                continue
            best_stops[airport] = stops
            
            for cost2, nei in adj[airport]:
                heapq.heappush(heap, [price + cost2, stops + 1, nei])
        
        return -1