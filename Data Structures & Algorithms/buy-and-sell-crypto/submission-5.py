class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r= len(prices)-1
        profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)-1,i,-1):
                newProfit = prices[j]-prices[i]
                profit = max(profit,newProfit)
        return profit

        