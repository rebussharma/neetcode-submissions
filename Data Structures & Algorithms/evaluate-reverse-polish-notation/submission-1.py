class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            match c:
                case "+":
                    res.append(res.pop() + res.pop())
                case "-":
                    a, b = res.pop(), res.pop()
                    res.append(b-a)
                case "*":
                    res.append(res.pop() * res.pop())
                case "/":
                    a, b = res.pop(), res.pop()
                    res.append(int(b/a))
                case _:
                    res.append(int(c))
        return res[0]
