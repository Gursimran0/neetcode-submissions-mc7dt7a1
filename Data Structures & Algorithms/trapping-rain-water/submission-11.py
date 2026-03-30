class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftMin = height[l]
        rightMin = height[r]
        res = 0
        while l<=r:
            if height[l]<height[r]:
                leftMin = max(leftMin,height[l])
                res += leftMin -height[l]
                l+=1
            else:
                rightMin = max(rightMin,height[r])
                res += rightMin-height[r]
                r-=1
            
        return res