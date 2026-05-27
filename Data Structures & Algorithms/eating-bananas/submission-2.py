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
                # is within given hour(h), then update minimum rate(min_r)
            if th <= h:
                # we found new minimum but we're not 100% certain 
                    # new minimum is the lowest rate, so we continue searching
                
                # we move maximum rate (max_r) as NEW minimum rate was found at mid
                # there's no point in looking at values GREATER than mid
                # we need to look at values less than mid
                max_r = mid - 1
            else:
                # total hours was greater than given hour(h)
                # this means current rate is too slow
                # we need to find faster rate so that bananas can be eated in specified time(h)
                # no point in searching 1->mid as mid is too slow,
                # we need to search beyond mid
                min_r = mid + 1
        return min_r
            