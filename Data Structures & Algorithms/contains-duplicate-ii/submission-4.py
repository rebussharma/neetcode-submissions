class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        res = set()
        l = 0

        for r in range(len(nums)):
            if nums[r] in res:
                return True
            res.add(nums[r])
            if r - l + 1 > k: # 0,1,2,0
                res.remove(nums[l])
                l += 1
        return False