class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_rev = [i*-1 for i in stones]
        heapq.heapify(stones_rev)
        print(stones_rev)

        while len(stones_rev) > 1:
            h1 = heapq.heappop(stones_rev)
            h2 = heapq.heappop(stones_rev)
            if h1 < h2:
                print(h1, h2, h2-h1)
                heapq.heappush(stones_rev, (abs(h2)-abs(h1)))
            print(stones_rev)

        return abs(stones_rev[0]) if stones_rev else 0