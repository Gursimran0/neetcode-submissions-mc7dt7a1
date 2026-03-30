class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxP = 0
        for price in prices:
            minPrice = min(minPrice,price)
            maxP = max(maxP,price-minPrice)
        return maxP

        