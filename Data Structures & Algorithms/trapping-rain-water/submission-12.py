class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        left = height[l]
        right = height[r]
        res=0
        while l<=r:
            if left<right:
                left = max(left,height[l])
                res += left - height[l]
                l+=1
            else:
                right = max(right,height[r])
                res += right - height[r]
                r-=1
            
        return res

        