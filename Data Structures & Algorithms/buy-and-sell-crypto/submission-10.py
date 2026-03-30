class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r=1
        maxP=0
        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l=r
            newP = prices[r]-prices[l]
            maxP = max(maxP,newP)
        return maxP
        