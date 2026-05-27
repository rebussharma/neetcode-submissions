class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            # # Keep swapping nums[i] to its correct position (nums[i]-1) as long as:
                # 1) nums[i] is a valid POSITIVE number and WITHIN bounds (1 to n), and
                # 2) nums[i] is not already in its correct position
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # swap nums[i] to its correct position nums[nums[i]-1]
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        
        # 8. Once done with the swaps, re-scan the array
        for i in range(n):
            # Check the rule: array[n-1] = n
            # i.e., at index n, the expected number is n+1
            if nums[i] != i + 1:
                # If the rule is broken, the smallest missing positive is i+1
                return i + 1

        # If all numbers 1..n are in place, the missing number is n+1
        return n + 1