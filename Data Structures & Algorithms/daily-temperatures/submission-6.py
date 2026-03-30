class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for ind,val in enumerate(temperatures):
            while stack and val>stack[-1][1]:
                stackInd,stackVal = stack.pop()
                res[stackInd]=ind-stackInd
            stack.append((ind,val))
        return res
        