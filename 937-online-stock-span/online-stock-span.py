class StockSpanner:

    def __init__(self):
        self.result = []

        

    def next(self, price: int) -> int:
        result, span = self.result, 1

        while result and result[-1][0] <= price:
            span += result[-1][1]
            result.pop()
        result.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)