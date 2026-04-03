class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        intervals.sort()

        for i in range(len(intervals)):
            # if new starts after curr one ends, continue
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if new interval ends before the curr one.
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)
        return res
