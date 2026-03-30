class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def backtrack(closeN,openN):
            if openN == closeN==n:
                res.append("".join(curr.copy()))
                return
            if openN<n:
                curr.append("(")
                backtrack(closeN,openN+1)
                curr.pop()
            if closeN<openN:
                curr.append(")")
                backtrack(closeN+1,openN)
                curr.pop()
        backtrack(0,0)
        return res
        