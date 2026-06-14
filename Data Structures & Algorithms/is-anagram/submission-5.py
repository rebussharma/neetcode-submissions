class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''
            r: 2
            a: 2
            c: 2
            e: 1

        '''
        # check for sure: hasMap O(1)

        hm = {}

        for i in range(len(s)):
            hm[s[i]] = hm.get(s[i], 0) + 1
            hm[t[i]] = hm.get(t[i], 0) - 1

        return all( k == 0 for k in hm.values())