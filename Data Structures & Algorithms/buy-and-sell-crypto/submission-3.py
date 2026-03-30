class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l,r = 0,1
        # maxP = 0
        # while r<len(prices):
        #     if prices[l]<prices[r]:
        #         maxP = max(maxP,prices[r]-prices[l])
        #     else:
        #         l=r
        #     r+=1
        # return maxP

        maxP = 0
        minBuy = prices[0]
        for price in prices:
            maxP = max(maxP,price - minBuy)
            minBuy = min(price,minBuy)
        return maxP

        