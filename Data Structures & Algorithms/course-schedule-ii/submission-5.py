class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adj = defaultdict(list)

        for a,b in prerequisites:
            adj[a].append(b)

        order = []
        UNVISITED, VISITING, VISITED = 0,1,2
        states = [UNVISITED] * numCourses
        def dfs(crs):
            if states[crs] == VISITING:
                return False
            elif states[crs] == VISITED:
                return True
            
            states[crs] = VISITING

            for nei in adj[crs]:
                if not dfs(nei):
                    return False
                
            states[crs] = VISITED
            order.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order

