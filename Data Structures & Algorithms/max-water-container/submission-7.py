class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        
        r=len(heights)-1
        res = 0

        while l<r:
            if heights[l]<heights[r]:
                width = r-l
                res = max(res,width*heights[l])
                l+=1
            else:
                width = r-l
                res = max(res,width*heights[r])
                r-=1
        return res