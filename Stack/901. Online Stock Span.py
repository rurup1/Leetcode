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
