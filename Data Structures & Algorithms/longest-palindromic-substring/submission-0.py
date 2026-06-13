class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        ml = 0

        for i in range(len(s)):
            # odd lengh
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > ml:
                    ml = curLen
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # even length
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > ml:
                    ml = curLen
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
