class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        res = 0
        maxLeft,maxRight = height[0],height[-1]
        l=0
        r=len(height)-1
        while l < r:
            if maxLeft<maxRight:
                l+=1
                maxLeft = max(maxLeft,height[l])
                
                res += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(maxRight,height[r])
                
                res += maxRight - height[r]
        return res
            
        