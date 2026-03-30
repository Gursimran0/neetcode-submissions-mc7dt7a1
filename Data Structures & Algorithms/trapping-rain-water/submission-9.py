class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxLeft = height[0]
        maxRight = height[r]
        total = 0
        while l<r:
            if height[l]<height[r]:
                maxLeft = max(height[l],maxLeft)
                total += (maxLeft-height[l])
                l+=1
            else:
                maxRight = max(height[r],maxRight)
                total += (maxRight-height[r])
                r-=1
        return total


        