class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        myStairs = [0]*(n+1)
        myStairs[1]=1
        myStairs[2]=2
        for i in range(3,n+1):
            myStairs[i]=myStairs[i-1] + myStairs[i-2]
        return myStairs[n]