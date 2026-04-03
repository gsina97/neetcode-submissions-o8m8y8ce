class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #  need a queue and a heap
        #  queue will keep whatever is currently on "cooldown"/cant use it yet.
        #  each item in queue will have the letter and the next time it can be processed. so ("X", 54)
        #  in heap , it'll be a max heap of what is processable (max heap)

        heap = []
        q = deque()

        c = Counter(tasks)
        
        for letter, count in c.items():
            heapq.heappush(heap, [- count, letter])
        

        time = 0
        while q or heap:
            if heap:
                count, letter = heapq.heappop(heap)
                count += 1 # since count is negative
                if count < 0:
                    q.append([letter, time + n, count])
            
            if q:
                if q[0][1] == time:
                    letter, t, c = q.popleft()
                    heapq.heappush(heap, [c, letter])
        
            time += 1
        
        return time

