class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}
        arr = []
        for n in range(len(nums)):
            if target - nums[n] in hmp.keys():
                arr.append(hmp.get(target-nums[n]))
                arr.append(n)

            hmp[nums[n]] = n
        return arr