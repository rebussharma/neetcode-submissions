class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        p1, p2 = 0,0 # 0, 0, n, n+1, n+2, n+3

        '''
            3   7,  4,  8,  1,  9,  5,  2,  6,  10
            3   7   7   15  15  24  24  26  30  33
        '''
        for n in nums[:-1]:
            cur = max(p1, p2 + n)
            p2 = p1
            p1 = cur

        lm = p1

        p1, p2 = 0,0

        for n in nums[1:]:
            cur = max(p1, p2 + n)
            p2 = p1
            p1 = cur

        return max(lm, p1)
    
