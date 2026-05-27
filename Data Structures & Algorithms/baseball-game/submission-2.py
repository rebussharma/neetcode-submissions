from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        total = 0

        for c in operations:
            match c:
                case "+":
                    val = res[-1] + res[-2]
                    res.append(val)
                    total += val

                case "D":
                    val = 2 * res[-1]
                    res.append(val)
                    total += val

                case "C":
                    val = res.pop()
                    total -= val

                case _:
                    val = int(c)
                    res.append(val)
                    total += val

        return total