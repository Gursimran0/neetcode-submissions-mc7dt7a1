class Solution {
    public int trap(int[] height) {
        if (height.length == 0){
            return 0;
        }
        int res = 0;
        int l = 0;
        int r = height.length - 1;
        int maxLeft = height[0];
        int maxRight = height[r];
        while(l<r){
            if (height[l]<height[r]){
                l++;
                maxLeft = Math.max(height[l],maxLeft);
                res += maxLeft - height[l];
            }
            else{
                r--;
                maxRight = Math.max(height[r],maxRight);
                res += maxRight - height[r];
            }


        }
        return res;
    }
}
