class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p1, p2 = 0,0

        for n in nums:
            cur = max(p1, n + p2)
            p2 = p1
            p1 = cur
        return p1
