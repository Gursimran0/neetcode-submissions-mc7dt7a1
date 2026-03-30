class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        
        minPrice = prices[0]
        profit = float("-infinity")
        for r in range(1,len(prices)):
            if prices[r]>minPrice:
                newProfit = prices[r] - minPrice
                profit = max(newProfit,profit)
            else:
                minPrice = prices[r]
        return profit if profit != float("-infinity") else 0 