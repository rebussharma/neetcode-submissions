class MyStack:
    def __init__(self):
        self.mq = deque()
        

    def push(self, x: int) -> None:
        dq = deque(self.mq)
        self.mq.clear() 
        self.mq.append(x) 
        self.mq.extend(dq) 

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