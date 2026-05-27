class MyQueue:

    def __init__(self):
        self.ms = []
        self.cs = []

    def push(self, x: int) -> None:
        self.ms.append(x)
        
    def move(self):
        if not self.cs:
            while self.ms:
                self.cs.append(self.ms.pop())

    def pop(self) -> int:
        self.move()
        return self.cs.pop()
        
    def peek(self) -> int:
        self.move()
        return self.cs[-1]

    def empty(self) -> bool:
        return not self.ms and not self.cs


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()