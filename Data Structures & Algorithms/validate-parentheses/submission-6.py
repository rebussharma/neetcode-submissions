class Solution:
    def isValid(self, s: str) -> bool:
        hm = {'}':'{', ')': '(', ']': '['}
        res = []

        for c in s:
            if c in hm: # make sure this char is a CLOSING parent
                # if res is not empty and
                # if top is result is matching paren to this char
                if res and res[-1] == hm[c]:
                    res.pop()
                else:
                    return False # if this char is not matching parenthesis to top res
            else:
                res.append(c)
        # only true if res is empty as we pop
        return True if not res else False
