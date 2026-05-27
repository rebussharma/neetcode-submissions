class Solution:
    def trap(self, nums: List[int]) -> int:
        res = 0
        maxl = maxr = 0
        l, r = 0, len(nums) - 1

        while l < r:
            maxl = max(maxl, nums[l])
            maxr = max(maxr, nums[r])

            if maxl < maxr:
                res += (maxl - nums[l])
                l += 1
            else:
                res += maxr - nums[r]
                r -= 1
        return res