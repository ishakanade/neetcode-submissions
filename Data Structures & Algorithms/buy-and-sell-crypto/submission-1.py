class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                current_profit = prices[sell] - prices[buy]
                profit = max(profit,current_profit)
        return profit