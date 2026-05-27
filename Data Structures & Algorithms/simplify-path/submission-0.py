class Solution:
    def simplifyPath(self, path: str) -> str:
        ms = []
        cur =  ""

        for p in path.split("/"):
            if p == "..":
                if ms: ms.pop()
            elif p != "" and p != ".":
                ms.append(p)
        return "/" + "/".join(ms) 
