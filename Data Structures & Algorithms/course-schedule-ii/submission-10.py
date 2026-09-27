class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        indegree =[0] * numCourses
        # [0,1] , take 1 before taking 0
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque()
        res =[]
        visited = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                res.append(i)

        while q:
            node = q.popleft()

            for nei in adj[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    res.append(nei)
                    q.append(nei)

        return res if len(res) == numCourses else []
        


        


