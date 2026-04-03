class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            if a not in courses:
                courses[a] =[]
            courses[a].append(b)

        
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if courses[course] == []:
                return True

            
            visiting.add(course)

            for preq in courses[course]:
                if not dfs(preq):
                    return False
            
            visiting.remove(course)
            courses[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True