class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.sort()

        iStart, iEnd = newInterval
        for i in range(len(intervals)):
            if iStart > intervals[i][1]:
                res.append(intervals[i])
            elif iEnd < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], iStart), max(intervals[i][1], iEnd)]
                iStart, iEnd = newInterval
        res.append(newInterval)
        return res