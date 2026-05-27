class Solution:
    def maxArea(self, heights: list[int]) -> int:
        res = 0
        if not heights:
            return res
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            # elif heights[r] < heights[l]: # this can be commented out as below we're doing the same
            #     r -= 1
            else: # if equal move either
                r -= 1  
        return res