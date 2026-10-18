class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        # Base case: first day
        if not self.prices:
            self.prices.append(price)
            return 1

        if price < self.prices[-1]:
            self.prices.append(price)
            return 1

        num_days = 1
        index = -1
        len_prices = len(self.prices)
        while index >= -len_prices and self.prices[index] <= price:
            num_days += 1
            index -= 1

        self.prices.append(price)
        return num_days
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)