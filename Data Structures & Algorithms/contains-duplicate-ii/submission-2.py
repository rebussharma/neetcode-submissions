class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = defaultdict(int)
        ans = False
        for i, n in enumerate(nums):
            if n in res:
                ans = abs(res[n] - i) <= k
            res[n] = i
        return ans