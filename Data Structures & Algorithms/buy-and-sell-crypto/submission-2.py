class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        num_days = len(prices)

        if num_days <= 1:
            return 0

        L = 0
        R = 1
        while R < num_days:
            buy_price = prices[L]
            sell_price = prices[R]
            
            if sell_price <= buy_price:
                L = R

            max_profit = max(max_profit, sell_price - buy_price)
            R += 1

        return max_profit

            
        