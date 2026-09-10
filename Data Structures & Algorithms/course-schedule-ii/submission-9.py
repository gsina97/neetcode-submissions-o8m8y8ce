class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses

        adj = defaultdict(list)
        # adj = which courses depend on X
        # indegree = how many courses does X depend on
        
        # a depends on b
        for a,b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)

            for newc in adj[crs]:
                indegree[newc] -= 1
                if indegree[newc] == 0:
                    q.append(newc)

        if len(res) != numCourses:
            return []
        return res