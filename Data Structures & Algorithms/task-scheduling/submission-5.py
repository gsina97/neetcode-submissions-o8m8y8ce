class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Q = (letter, count, coolDownTime)
        # heap = (-cnt, letter)
        heap = []
        q = deque()

        time = 0

        counter = Counter(tasks)

        for key, cnt in counter.items():
            heapq.heappush(heap, (-cnt, key))
        
        while q or heap:
            if heap:
                cnt, letter = heapq.heappop(heap)
                cnt += 1
                if cnt != 0:
                    q.append((letter, cnt, time + n))
            
            if q and q[0][2] == time:
                letter, cnt, _ = q.popleft()
                heapq.heappush(heap, (cnt, letter))
            

            time += 1

        return time