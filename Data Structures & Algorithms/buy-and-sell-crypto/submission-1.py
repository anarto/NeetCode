class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        maxP = 0
        n = len(prices)
        if n <= 1:
            return 0
        
        lowPrice = prices[0]
        for r in range(1, n):
            maxP = max(prices[r] - lowPrice, maxP)
            lowPrice = min(lowPrice, prices[r])

        return maxP