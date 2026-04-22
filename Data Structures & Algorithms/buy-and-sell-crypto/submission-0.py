class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = end = 0
        max_profit = 0
        while end < len(prices):
            buy_price = prices[start]
            sale_price = prices[end]
            if buy_price <= sale_price:
                profit = sale_price - buy_price
                max_profit = max(max_profit, profit)
                end+=1
            else:
                start+=1
        return max_profit
        