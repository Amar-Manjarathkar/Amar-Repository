class Solution:
    def maxProfit(self, arr):
        n = len(arr)
        if n < 2:
            return 0

        # Initialize the 3 states
        # 'hold': Max profit if we end the day holding a stock
        # 'sold': Max profit if we end the day having just sold a stock
        # 'rest': Max profit if we end the day not holding (ready to buy or in cooldown)

        # We set 'hold' to -inf to ensure we must buy from the 'rest' state first.
        # 'rest' starts at 0 (no profit).
        # 'sold' starts at 0 (no profit).
        hold = -float('inf')
        sold = 0
        rest = 0

        for price in arr:
            # We need to store the previous 'sold' value
            # because 'rest' depends on it, but 'sold' is updated first.
            prev_sold = sold
            
            # 1. Update 'sold' state
            #    We can only sell if we were 'holding' yesterday.
            sold = hold + price

            # 2. Update 'hold' state
            #    We either 'hold' what we had, or we 'buy' from a 'rest' state.
            hold = max(hold, rest - price)
            
            # 3. Update 'rest' state
            #    We either 'rest' again, or we enter 'rest' (cooldown) from 'prev_sold'.
            rest = max(rest, prev_sold)

        # The final max profit is the most we could have
        # by either ending in a 'sold' state or a 'rest' state.
        return max(sold, rest)
