class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for ind,val in enumerate(temperatures):
            while stack and val>stack[-1][1]:
                stackInd,stackVal = stack.pop()
                res[stackInd] = ind - stackInd
            stack.append((ind,val))
        return res
        