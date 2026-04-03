class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        


        time = 0

        q = deque()

        # 

        # map -> letter, count

        c = Counter(tasks)

        heap = []
        for letter, cnt in c.items():
            heapq.heappush(heap, (-cnt, letter))
        
        while q or heap:
            
            if heap:
                cnt, letter = heapq.heappop(heap)
                cnt += 1
                if cnt:
                    q.append((time + n, cnt, letter))
            
            if q and q[0][0] == time:
                _ , cnt, letter = q.popleft()
                heapq.heappush(heap, (cnt, letter))
            
            time += 1
        return time