class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        if not prices or len(prices) <= 1:
            return mp
        
        l = 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                mp = max(mp, prices[r] - prices[l])
            else:
                l = r
        return mp