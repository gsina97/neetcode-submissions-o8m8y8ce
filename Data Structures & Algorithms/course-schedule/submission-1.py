class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visitedCourse = set()


        prevMap = { i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        def dfs(crs):
            if crs in visitedCourse:
                return False
            
            if prevMap[crs] == []:
                return True

            
            visitedCourse.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            
            visitedCourse.remove(crs)
            prevMap[crs] = []
            return True
        
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True