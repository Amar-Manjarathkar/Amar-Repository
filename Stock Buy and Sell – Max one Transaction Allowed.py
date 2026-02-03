class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')  # Initialize with a very high value
        max_profit = 0            # Initialize max profit to 0
        
        for price in prices:
            # Update the minimum price seen so far
            if price < min_price:
                min_price = price
            
            # Check the profit if we sell at the current price
            # current_profit = price - min_price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
