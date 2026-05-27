class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = ""
        '''
            check if first letter of first word is in all words
        '''
        for i, letter in enumerate(first):
            for word in strs[1:]:
                if i >= len(word) or word[i] != letter:
                    return res
            res += letter
        return res