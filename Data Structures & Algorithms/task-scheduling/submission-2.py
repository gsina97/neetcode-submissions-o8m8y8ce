class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # what i have already picked + next process time allowed.
        q = deque()

        #  keep track of maximum pickable task
        counter = Counter(tasks)

        heap = []
        # key is letter, val is value
        for key,val in counter.items():
            heapq.heappush(heap, (- val, key ))
        
        t = 0
        print(heap)
        while heap or q:
            
            # what i process now
            if heap:
                # count is negative
                count, item = heapq.heappop(heap)
                count += 1
                if count != 0:
                    q.append(((t+n), (count, item)))
           
            if q:
                timeToProcess, countItem = q[0]
                count2, item2 = countItem
                if t  == timeToProcess:
                    q.popleft()
                    heapq.heappush(heap, (count2, item2))
            t += 1
        return t
            


