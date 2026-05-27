class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target: return True

            if nums[l] < nums[m]: #left portion
                # if we in left portion
                # if target is between left and mid
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]: # right portion
                # if we in right portion
                # if target is between mid and right
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            else: # nums[l] == nums[m] we can't determine if we're in left or right portion
                l += 1
            
        return False
