class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[]
        res=[]
        for i in range(n):
            l.append(i+1)
        def backtrack(i,curr):
            if len(curr)==k:
                res.append(curr.copy())
                return
            if i>=len(l):
                return
            curr.append(l[i])
            backtrack(i+1,curr)
            curr.pop()
            backtrack(i+1,curr)
        backtrack(0,[])
        return res


        