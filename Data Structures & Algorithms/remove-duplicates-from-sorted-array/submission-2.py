class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        il = len(nums)
        prev = nums[0]
        nums.append(prev)
        for i in range(1, il):
            if nums[i] != prev:
                nums.append(nums[i])
            prev = nums[i]
        del nums[:il]
        return len(nums)