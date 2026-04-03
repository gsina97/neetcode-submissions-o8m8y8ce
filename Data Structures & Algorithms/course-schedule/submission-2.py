class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            preqMap[crs].append(preq)
        visiting = set()
        
        def dfs(crs):
            if crs in visiting:
                return False

            if preqMap[crs] == []:
                return True

            visiting.add(crs)

            for preq in preqMap[crs]:
                if not dfs(preq):
                    return False
            
            visiting.remove(crs)
            preqMap[crs] = []
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
