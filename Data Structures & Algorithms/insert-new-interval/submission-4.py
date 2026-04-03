class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
# if intervals[]
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            # if new interval alnds before my curr one, since its sorted, its safe to append and return
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if it's after, continue searching
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newMin = min(intervals[i][0], newInterval[0])
                newMax = max(intervals[i][1], newInterval[1])
                newInterval = [newMin, newMax]
        res.append(newInterval)
        return res
