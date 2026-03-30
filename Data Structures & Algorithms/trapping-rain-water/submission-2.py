class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        res = 0
        l=0
        r = len(height)-1
        maxLeft = height[0]
        maxRight = height[r]

        while l<r:
            if height[l]<height[r]:
                l+=1
                maxLeft = max(height[l],maxLeft)
                res += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(height[r],maxRight)
                res += maxRight - height[r]
        return res
        