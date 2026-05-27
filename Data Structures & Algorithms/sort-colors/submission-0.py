class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums)) < 2:
            return nums
        
        min_val, max_val = min(nums), max(nums)

        buckets = [[] for _ in range(len(nums))]
        for n in nums:
            index = int((n - min_val) / (max_val - min_val + 1) * len(buckets))
            buckets[index].append(n)

        for b in buckets:
            self.insertion_sort(b)
        
        res = []

        for b in buckets:
            res.extend(b)

        for i in range(len(nums)):
            nums[i] = res[i]

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            curr = arr[i]
            prev_index = i - 1

            while prev_index >= 0 and curr < arr[prev_index]:
                arr[prev_index + 1] = arr[prev_index]
                prev_index -= 1
            arr[prev_index + 1] = curr