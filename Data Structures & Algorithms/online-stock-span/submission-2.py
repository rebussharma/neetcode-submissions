class StockSpanner:

    def __init__(self):
        self.ms = []
        self.cntr = []
        self.val = 1
        

    def next(self, price: int) -> int:
        self.val = 1
        while self.ms and price >= self.ms[-1][0]:
            p = self.ms.pop()
            self.val += p[1]
        self.ms.append([price, self.val])
        return self.val



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)