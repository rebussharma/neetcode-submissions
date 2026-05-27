class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            
        '''
        if not points:
            return []
        heap = [
            [x*x + y*y, x, y] for x,y in points
        ]

        heapq.heapify(heap)
        res = []

        for _ in range(k): # rest of the rows
            d, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res