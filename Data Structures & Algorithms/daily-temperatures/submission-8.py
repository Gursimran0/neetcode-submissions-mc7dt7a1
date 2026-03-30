class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for ind,val in enumerate(temperatures):
            while stack and  val>stack[-1][1]:
                indStack,indVal = stack.pop()
                res[indStack] = ind - indStack
            stack.append([ind,val])
        return res
        