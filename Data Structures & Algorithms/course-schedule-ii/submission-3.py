class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = defaultdict(list)

        for crs, preq in prerequisites:
            adj[crs].append(preq)

        visited = set()
        checked = set()
        def dfs(course):
            if course in visited:
                return False
            
            if course in checked:
                return True
            if course == []:
                return True
            
            visited.add(course)
            for preq in adj[course]:
                if not dfs(preq):
                    return False
            
            visited.remove(course)
            checked.add(course)
            adj[course] = []
            res.append(course)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
                
