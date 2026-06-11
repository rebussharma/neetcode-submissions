class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
            
        nums[1] = max(nums[0], nums[1])

        for n in range(2, len(nums)):
            nums[n] = max(
                (nums[n] + nums[n-2]),
                nums[n-1]
            )
        return nums[-1]
