class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if new i s
        res = []
        for i in range(len(intervals)):
            # if new falls later
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if falls before
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                # res.append()
                return res
            else:
                # if overlap , merge
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        
        res.append(newInterval)
        return res