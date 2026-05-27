class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        window_start = 0

        for right in range(len(nums)):
            if right - window_start > k: # there's already enough numbers in window set:
                window.remove(nums[window_start])
                window_start += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False