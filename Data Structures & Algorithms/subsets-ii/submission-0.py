class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(i, ss):
            if i >= len(nums):
                res.append(ss[::])
                return

            ss.append(nums[i])
            bt(i+1, ss)

            ss.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            bt(i+1, ss)
            
        bt(0, [])
        return res