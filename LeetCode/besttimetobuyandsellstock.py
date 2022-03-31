# Kadane's Algorithm - modified
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            cur_profit = prices[i] - buy
            if cur_profit < 0:
                buy = prices[i]
                
            # update max
            if cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit