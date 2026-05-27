class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for m in matrix:
            if m[-1] >= target:
                res = self.searchHere(m, target)
                if res: return res
        return res
    
    def searchHere(self, nums: List[int], target: int):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l)//2)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False