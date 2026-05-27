class MyQueue:

    def __init__(self):
        self.ms = []

    def push(self, x: int) -> None:
        self.ms.append(x) # 1,2,3
        d = self.ms.copy()
        for i in range(1, len(self.ms)):
            self.ms[i] = d[i-1]
        self.ms[0] = x
        
    def pop(self) -> int:
        return self.ms.pop()
        
    def peek(self) -> int:
        return self.ms[-1]

    def empty(self) -> bool:
        return len(self.ms) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()