class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res = 0
        while l<r:
            if heights[l]<heights[r]:
                area = heights[l]*(r-l)
                res = max(area,res)
                l+=1
            else:
                area = heights[r]*(r-l)
                res = max(area,res)
                r-=1
        return res
        