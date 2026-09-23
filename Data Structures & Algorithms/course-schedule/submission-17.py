class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b]
        # a depends on b <-> take b first


        indegree = [0] * numCourses

        adj = defaultdict(list)

        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1     
        

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
                    
        if len(res) != numCourses:
            return False
        return True