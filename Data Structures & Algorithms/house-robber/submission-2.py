class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        #[first, second, n, n+1, n+2...]
        for n in nums:
            tmp = max(n+first, second)
            first = second
            second = tmp

        return second