class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for sell in prices:
            maxP = max(maxP,sell - minBuy)
            minBuy = min(minBuy,sell)
        return maxP

        # maxP =0
        # l,r=0,1
        # while r<len(prices):
        #     if prices[l]<prices[r]:
        #         maxP = max(maxP,prices[r]-prices[l])

        #     else:
        #         l=r
        #     r+=1

        # return maxP
        

        