class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        sell,buy = 1,0
        while prices[sell] < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[but]
                maxp = max(maxp,profit)
            else :
                buy = sell
            sell += 1
        return maxp 