class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]: # sell is high
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else: # sell is lower than buy, meaning we need to buy at the lower price
                l = r
            r += 1
        return max_profit