class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # check if selling today is better
            max_profit = max(max_profit, price - min_price)
            # update lowest buy price seen so far
            min_price = min(min_price, price)
                                                                                        
        return max_profit