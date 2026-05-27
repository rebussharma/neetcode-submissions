class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 and word2:
            return ""
        if not word1 or len(word1) == 0:
            return word2
        if not word2 or len(word2) == 0:
            return word1
        
        i = j = 0
        res = []
        
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1
        res.extend(word1[i:])
        res.extend(word2[j:])

        return ''.join(res)