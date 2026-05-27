class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        if not operations:
            return s
        
        for i, c in enumerate(operations):
            match c:
                case "+":
                    if len(res) > 1:
                        s = (int(res[-1]) + int(res[-2]))
                        res.append(s)
                case "D":
                    if len(res) > 0:
                        s =  2 * int(res[-1])
                        res.append(2 * int(res[-1]))
                case "C":
                    res.pop()
                case _ :
                    res.append(int(c))
            
        return sum(res)