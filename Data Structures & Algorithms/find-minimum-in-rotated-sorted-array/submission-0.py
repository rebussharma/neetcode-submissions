class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3,4,5,6,1,2
        l = 0
        r = len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] > nums[-1]:
                res = min(res, nums[-1])
                l = mid + 1

            else:
                res = min(res, nums[mid])
                r = mid - 1
        return res