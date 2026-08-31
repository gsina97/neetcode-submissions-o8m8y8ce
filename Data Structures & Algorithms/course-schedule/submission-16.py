class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        indegree = [0] * numCourses
        adj = defaultdict(list)
        # take b before taking a
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        while q:
            crs = q.popleft()
            visited += 1
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return visited == numCourses
