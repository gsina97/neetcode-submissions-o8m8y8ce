class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        adj = [[] for x in range(numCourses)]
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return numCourses == visited
