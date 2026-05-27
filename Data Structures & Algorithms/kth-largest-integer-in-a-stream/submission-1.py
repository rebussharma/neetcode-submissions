class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        '''
            1,2,3,3
            add 3 -> 1,2,3,3,3 = 3 # 1,2,3
            1,2,3,3,3,5 => 3 #1,2,3
            1,2,3,3,3,5,6 => 3
            1,2,3,3,3,5,6,7=>5 
            
            1,2,3,4,5
            5 - 4 + 1 = 2
            len - kth alrgest + 1

        '''
        self.nums.append(val)
        res = self.nums.copy()
        heapq.heapify(res)
        print(self.nums)
        for _ in range(len(self.nums) - self.k):
            heapq.heappop(res)
        return heapq.heappop(res)