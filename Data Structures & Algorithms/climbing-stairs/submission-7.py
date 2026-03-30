class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2  or n == 1:
            return n
        res = [0]*(n+1)
        res[1]=1
        res[2]=2
        
        for i in range(3,n+1):
            res[i] = res[i-1]+res[i-2]
        print (res[i])
        return res[i]


        