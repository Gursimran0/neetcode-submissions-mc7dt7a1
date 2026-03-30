class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: 
        res = 0
        stack = [] # added as (index,height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                ind,height = stack.pop()
                area = height*(i-ind)
                res = max(area,res)
                start = ind
            stack.append((start,h))
        
        for i,h in stack:
            area = h*(len(heights)-i)
            res = max(area,res)
        return res

        