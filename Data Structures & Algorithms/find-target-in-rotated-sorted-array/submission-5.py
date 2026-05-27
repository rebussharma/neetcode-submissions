class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            # left portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]: # search right as target is larger or target is smaller than leftmost value
                    l = mid + 1
                else: # targer is less than middle but greater than left
                    r = mid - 1
            # right portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: # target is greater than middles and less than right
                    l = mid + 1
        return -1
