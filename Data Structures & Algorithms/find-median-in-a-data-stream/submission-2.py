class MedianFinder:

    def __init__(self):
        # two heaps, large and small
        # small will be maxHeap
        # large will be minHeap
        # max of small + min of large / 2 is median if both have same len
        # if one has extra len:
            # if small has extra len, median is max of small
            # if large has extra len, median is min of large

        self.s = []
        self.l = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, -1 * num) # maxHeap

        # make sure each element in small is less or equal to large
        if (self.s and self.l and (-1 * self.s[0]) > self.l[0]):
            val = -1 * heapq.heappop(self.s)
            heapq.heappush(self.l, val)

        # what if len of heaps are not approx same
        # what if len differ by more than 1?
        if len(self.s) > len(self.l) + 1:
            val = -1 * heapq.heappop(self.s)
            heapq.heappush(self.l, val)
        if len(self.l) > len(self.s) + 1:
            val = heapq.heappop(self.l)
            heapq.heappush(self.s, -1 * val)

    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return -1 * self.s[0]
        if len(self.s) < len(self.l):
            return self.l[0]
        if len(self.s) == len(self.l):
            return (-1 * self.s[0] + self.l[0]) / 2
