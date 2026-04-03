class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        # lefthalf
        heapq.heappush(self.maxheap, -num)

        val = -heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, - heapq.heappop(self.minheap))


    def findMedian(self) -> float:
        if len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2


        