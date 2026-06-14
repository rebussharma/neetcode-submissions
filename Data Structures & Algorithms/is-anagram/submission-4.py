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

        s_hm = {}
        t_hm = {}

        for i in range(len(s)):
            if s[i] in s_hm:
                s_hm[s[i]] = 1 + s_hm.get(s[i])
            else:
                s_hm[s[i]] = 0
            

        for i in range(len(t)):
            if t[i] in t_hm:
                t_hm[t[i]] = 1 + t_hm.get(t[i])
            else:
                t_hm[t[i]] = 0

        print(s_hm, t_hm)
        return s_hm == t_hm