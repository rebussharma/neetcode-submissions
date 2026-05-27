class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_r = 1
        max_r = max(piles)
        
        while min_r <= max_r:
            mid = (min_r + max_r) // 2
            th = 0
            for p in piles:
                th += -(-p // mid)
            if th <= h:
                res = min(min_r, mid)
                max_r = mid - 1
            else:
                min_r = mid + 1
        return min_r
            