class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]


        for start, end in intervals[1:]:
            endLast = res[-1][1]
            if endLast >= start:
                res[-1][1] = max(endLast, end)
            else:
                res.append([start,end])
        return res
