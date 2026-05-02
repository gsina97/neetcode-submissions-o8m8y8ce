class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        for a,b in prerequisites:
            adj[a].append(b)

        

        unvisited, visiting, visited = 0,1,2
        state = [0] * (numCourses)
        res = []
        def dfs(crs):
            if state[crs] == visited:
                return True
            if state[crs] == visiting:
                return False
            
            state[crs] = visiting
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            state[crs] = visited
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


