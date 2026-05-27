class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # find the peak element
        l, r = 1, length - 2 # peak will never be at first or last element

        while l <= r:
            m = (l+r) // 2
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left < mid > right:
                break # we found mid
            elif left < mid < right: # we're still in increasing order, so we're in left portion, need to go right
                l = m + 1
            else: # we're in decreasing order left > mid > right, we're in right portion, need to go left
                r = m - 1
        peak = m # in python m will be in scope
                
        # search left portion
        l,r = 0, peak
        while l <= r:
            m = (l+r) // 2
            val = mountainArr.get(m)

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # search right portion
        l,r = peak, length - 1
        while l <= r:
            m = (l+r) // 2
            val = mountainArr.get(m)

            # we're in descing portion 3,2,1, if mid if target is 3 and mid is 2, so we search left
            if val < target:
                r = m - 1
            elif val > target:
                l = m + 1
            else:
                return m

        return -1