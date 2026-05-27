class MyStack:
    def __init__(self):
        self.mq = deque()
        

    def push(self, x: int) -> None:
        # [1,2]
        print("before push", self.mq)
        dq = deque(self.mq)
        print("q set to m1", dq, "mq", self.mq)
        self.mq.clear() # []
        self.mq.append(x) # [3]
        print("mq after append x", self.mq)
        print("dq after mq has x", dq)
        self.mq.extend(dq) # [3,2,1]
        print("after push", self.mq)

        

    def pop(self) -> int:
        print("before pop", self.mq)
        return self.mq.popleft()
        print("After pop", self.mq)

    def top(self) -> int:
        return self.mq[0]
        
    def empty(self) -> bool:
        print("empty", self.mq)
        return len(self.mq) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()