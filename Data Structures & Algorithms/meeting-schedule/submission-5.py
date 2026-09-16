"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        # intervals.sort()
        sorted_by_start = sorted(intervals, key=lambda interval: interval.start)

        prevEnd = sorted_by_start[0].end

        for i in range(1, len(sorted_by_start)):
            if prevEnd > sorted_by_start[i].start:
                return False
            else:
                prevEnd = sorted_by_start[i].end
        
        return True

