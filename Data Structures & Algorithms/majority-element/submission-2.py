from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
            if res[n] > len(nums) // 2:
                return n
        return -1