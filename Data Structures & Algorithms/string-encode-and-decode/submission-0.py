class Solution:

    def encode(self, strs:List[str]) -> List[str]:
        delm = "$"
        s = ""
        for e in strs:
            s += str(len(e)) + delm + e
        return s
    
    def decode(self, strs:str) -> List[str]:
        delm = "$"
        res = []
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != delm:
                j += 1
            w_l = int(strs[i:j])
            print(w_l)
            w = strs[j+1: j+1+w_l]
            res.append(w)
            i = j + 1 + w_l
        return res
