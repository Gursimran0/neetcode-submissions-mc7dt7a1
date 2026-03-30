class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = [amount+1]*(amount+1)
        count = amount+1

        res[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    res[i]=min(res[i],1+res[i-c])
        
        return res[amount] if res[amount]!=amount+1 else -1
        