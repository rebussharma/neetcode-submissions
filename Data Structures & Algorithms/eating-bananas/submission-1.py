class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_r = 1 # minimum rate bananas can be ate
        max_r = max(piles) # max rate bananas can be ate
        
        while min_r <= max_r:
            mid = (min_r + max_r) // 2
            th = 0 # total hours

            # loop through piles to find total hrs spent to eat 
                # all bananas at current rate (mid)
            for p in piles:
                th += -(-p // mid)

            # if total hrs spent eating at current rate(mid)
                # is within given hour(h), then 
            if th <= h:
                min_r = min(min_r, mid)
                max_r = mid - 1
            else:
                min_r = mid + 1
        return min_r
            