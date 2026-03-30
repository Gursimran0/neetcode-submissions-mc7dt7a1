class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            newProfit = price - minPrice
            maxProfit = max(maxProfit,newProfit)
            minPrice = min(minPrice,price)

        return maxProfit
