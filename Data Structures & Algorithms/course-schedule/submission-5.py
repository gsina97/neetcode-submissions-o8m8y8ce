class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = defaultdict(list)

        for crs, preq in prerequisites:
            adj[crs].append(preq)

        visited = set()
        def dfs(course):
            if adj[course] == []:
                return True
            
            if course in visited:
                return False

            visited.add(course)
            for preq in adj[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            adj[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True