class Solution:
    def decodeString(self, s: str) -> str:
        ms = []
        for c in s:
            if c == "]":
                tmp = ""
                dg = ""

                while ms and ms[-1] != "[":
                    tmp = ms.pop() + tmp   # build in correct order

                ms.pop()  # remove "["

                while ms and ms[-1].isdigit():
                    dg = ms.pop() + dg

                num = int(dg)
                expanded = tmp * num

                for ch in expanded:       # push char-by-char
                    ms.append(ch)

            else:
                ms.append(c)

        return ''.join(ms)