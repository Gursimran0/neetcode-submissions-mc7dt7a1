class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        newP = prices[0]
        maxP = 0
        for price in prices:
            maxP = max(price-newP,maxP)
            newP = min(newP,price)
        return maxP
            
        