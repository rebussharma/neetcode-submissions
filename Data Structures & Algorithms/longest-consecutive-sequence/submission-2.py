class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        s_n = sorted(s)

        cnt = max_c = 1
        prev = s_n[0]
        for n in s_n[1:]:
            if n - prev != 1:
                cnt = 1
            else:
                cnt += 1
                max_c = max(max_c, cnt)
            prev = n
        return max_c