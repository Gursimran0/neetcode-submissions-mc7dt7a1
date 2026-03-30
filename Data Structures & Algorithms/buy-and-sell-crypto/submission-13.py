class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxP = 0
        minPrice = prices[l]
        for r in range(1,len(prices)):
            if prices[r]<prices[l]:
                l=r
            newPrice = prices[r]-prices[l]
            maxP = max(newPrice,maxP)
        return maxP