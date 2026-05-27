import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-1 * num for num in stones]
        # -2,-3,-6,-2,-4

        heapq.heapify(stones)

        # in case stone len < 2?
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                y = abs(abs(x) - abs(y)) * -1
                heapq.heappush(stones, y)
        
        return 0 if not stones else abs(stones[0])