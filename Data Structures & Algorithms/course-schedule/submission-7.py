class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)


        visited = set()
        def dfs(crs):
            if adj[crs] == []:
                return True
            if crs in visited:
                return False
            
            visited.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            adj[crs] == []
            visited.remove(crs)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True