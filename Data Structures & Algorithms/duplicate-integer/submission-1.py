class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for idx, num in enumerate(nums):
            if num in nums[(idx+1):]:
                return True
        return False