class StockSpanner:

    def __init__(self):
        self.ms = []        

    def next(self, price: int) -> int:
        val = 1
        while self.ms and price >= self.ms[-1][0]:
            p = self.ms.pop()
            val += p[1]
        self.ms.append([price, val])
        return val



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)