class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or s is None:
            return False

        parenMap = { "}":"{", ")":"(", "]":"[" }
        stack = []
        for i in s:
            if i in parenMap: # meaning i is in the KEYS of map
                if stack and stack[-1] == parenMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False