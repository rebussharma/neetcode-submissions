class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        curSum = 0
        prevSums = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k
            res += prevSums.get(diff, 0)
            prevSums[curSum] = 1 + prevSums.get(curSum, 0)

        return res