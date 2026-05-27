class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False    
        s_set = {}
        t_set = {}
        for i in s:
            s_set[i] = s_set.get(i, 0) +  1
        for j in t:
            t_set[j] = t_set.get(j, 0) +  1
        return s_set == t_set