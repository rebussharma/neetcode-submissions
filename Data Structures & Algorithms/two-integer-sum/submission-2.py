class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return
        res = {}
        
        for i in range(len(nums)):
            if target - nums[i] in res:
                return [res.get((target - nums[i])), i]
            res[nums[i]] = i