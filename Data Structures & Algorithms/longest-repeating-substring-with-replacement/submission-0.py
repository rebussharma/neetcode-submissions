class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            charSet[s[r]] = 1 + charSet.get(s[r], 0)

            while (r - l + 1) - max(charSet.values()) > k:
                charSet[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res