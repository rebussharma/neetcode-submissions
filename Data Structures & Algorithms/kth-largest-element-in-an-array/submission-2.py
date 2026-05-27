class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [2,3,1,5,4]

        # heap = [2,3]
        heap = nums[:k]
        heapq.heapify(heap) # [2,3]

        for num in nums[k:]:# nums in [1,5,4]
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]