class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return nums
        
        mid_index = len(nums) // 2
        left_half = nums[:mid_index]
        right_half = nums[mid_index:]

        sortedLeft = self.sortArray(left_half)
        sortedRight = self.sortArray(right_half)

        return self.merge_sort(sortedLeft, sortedRight)
    
    def merge_sort(self, left, right):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res.extend(left[i:])
        res.extend(right[j:])
        return res