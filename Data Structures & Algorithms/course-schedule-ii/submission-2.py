class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visitedCourse = set()
        prevMap = {i: [] for i in range(numCourses)}
        checked = set()
        res = []

        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        def dfs(crs):
            if crs in visitedCourse:
                return False

            if crs in checked:
                return True

            visitedCourse.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False

            visitedCourse.remove(crs)
            checked.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res # reverse to get correct order
