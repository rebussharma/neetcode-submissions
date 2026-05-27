class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res, curQuad = [], []
        nums.sort()

        def kSum(k, start_index, target):
            # not base case
            if k != 2:
                for i in range(start_index, len(nums) - k + 1): # make sure there are atleast k+1 eleemnts in loop to go for
                    if i > start_index and nums[i] == nums[i - 1]:
                        continue
                    curQuad.append(nums[i])
                    kSum(k-1, i + 1, target - nums[i])
                    curQuad.pop()
                return

            # base case if k == 2
            l, r = start_index, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(curQuad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        kSum(4, 0, target)
        return res