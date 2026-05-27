class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        res = defaultdict(int)
        arr = set()

        for n in nums:
            res[n] += 1
            if res[n] > len(nums)/3:
                arr.add(n)
        return list(arr)
        