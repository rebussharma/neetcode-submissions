class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, val: int) -> None:
        self.s1.append(val)

        if not self.s2 or val <= self.s2[-1]:
            self.s2.append(val)
        
    def pop(self) -> None:
        if not self.s1:
            raise Exception("stack is empty")
        p = self.s1.pop()
        if p == self.s2[-1]:
            self.s2.pop()

    def top(self) -> int:
        if not self.s1:
            raise Exception("stack is empty")
        return self.s1[-1]

    def getMin(self) -> int:
        if not self.s2:
            raise Exception("stack is empty")
        return self.s2[-1]
        