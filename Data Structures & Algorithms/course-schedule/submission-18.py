class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = defaultdict(list)

        indegree =[0] * numCourses
        # [0,1] , take 1 before taking 0
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque()
        visited = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)

        while q:
            node = q.popleft()

            for nei in adj[node]:
                indegree[nei] -= 1
                if not indegree[nei] and nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return len(visited) == numCourses
        


        


