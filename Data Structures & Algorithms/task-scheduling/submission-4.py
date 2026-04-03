class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap and a queue
        # heap gives me what can be processed NOW (max heap), heap stores [countleft, char]
        # queue stores whatever task is on cooldown (Cant be processed yet)
        q = collections.deque()
        heap = []
        countMap = Counter(tasks)

        for char, count in countMap.items():
            heapq.heappush(heap, [- count, char])


        time = 0
        while q or heap:
            # first claim max item from heap
            if heap:
                count, char = heapq.heappop(heap)
                count += 1
                if count:
                    q.append([time+n, count, char])

            if q and q[0][0] == time:
                _, count, char = q.popleft()
                heapq.heappush(heap, [count, char])
            time += 1
        
        return time

