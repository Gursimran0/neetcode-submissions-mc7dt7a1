class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if not n:
            return res
        
        def backtrack(curr,openN,closeN):
            if openN == closeN == n:
                res.append("".join(curr.copy()))
                return 
          
            
            if openN<n:
                curr.append("(")
                backtrack(curr,openN+1,closeN)
                curr.pop()
            if closeN<openN:
                curr.append(")")
                backtrack(curr,openN,closeN+1)
                curr.pop()
        backtrack([],0,0)
        return res
        