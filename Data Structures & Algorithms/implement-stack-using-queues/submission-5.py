class MyStack:
    def __init__(self):
        self.mq = deque()
        

    def push(self, x: int) -> None:
        self.mq.append(x) 
        for _ in range(len(self.mq) - 1):
            self.mq.append(self.mq.popleft()) # get left most element from mq and appned it to mq
            # basically rotate mq

    def pop(self) -> int:
        return self.mq.popleft()

    def top(self) -> int:
        return self.mq[0]
        
    def empty(self) -> bool:
        return len(self.mq) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()