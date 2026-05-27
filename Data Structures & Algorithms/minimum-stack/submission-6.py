class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, val: int) -> None:
        if not self.s2 or val <= self.s2[-1]:
            self.s2.append(val)
        self.s1.append(val)
        
    def pop(self) -> None:
        p = self.s1.pop()
        if p == self.s2[-1]:
            self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1] if self.s2 else self.s1[0]
        
