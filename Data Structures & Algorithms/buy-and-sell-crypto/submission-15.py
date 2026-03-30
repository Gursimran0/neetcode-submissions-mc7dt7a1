class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        res = 0
        price=prices[l]
        for r in range(1,len(prices)):
            if prices[r]>price:
                res = max(res,prices[r]-price)
            else:
                price = prices[r]
        return res


        