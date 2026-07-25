class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l,r = 0,1 #left = buy right = sell
        while r < len(prices):
            if l < r :
                profit = prices[r] - prices[l]
                maxp = max(maxp,profit)
                
            else:
                l = r
            r += 1
        return maxp