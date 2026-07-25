class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            _, count = self.stack.pop()
            res += count
        
        self.stack.append((price, res))
        
        return res

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.arr = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1] <= price:
            self.stack.pop()
            res += 1
        
        self.arr.append(price)
        self.stack = self.arr.copy()

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)