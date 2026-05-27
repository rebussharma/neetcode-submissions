class MedianFinder:

    def __init__(self):
        self.arr = []
        self.heap = []
        

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        temp = self.heap.copy()
        heapq.heapify(temp)

        self.arr = []
        print("num to add:", num)
        print("heap arr:", self.heap)
        print("tmp arr:", temp)
        print("arr:", self.arr)
        while temp:
            val = heapq.heappop(temp)
            print("POPPPED", val)
            self.arr.append(val)
        print("arr after llop:", self.arr)
        
    def findMedian(self) -> float:
        print(" ======== arr is: ", self.arr)

        if len(self.arr) == 1:
            return self.arr[0]

        mid = len(self.arr)//2
        if len(self.arr) % 2 == 0:
            return (self.arr[mid] + self.arr[mid-1])/2
        else:
            return self.arr[mid]