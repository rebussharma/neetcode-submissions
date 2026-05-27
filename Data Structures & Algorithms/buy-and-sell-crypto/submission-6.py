class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        if not prices:
            return mp
        
        l, r = 0, 1
        
        while r < len(prices):
            #profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mp = max(profit, mp)
            else: # if right is smaller than left, then lets take right to be left
                l = r
            r += 1
        return mp