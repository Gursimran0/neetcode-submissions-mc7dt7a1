class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int left = heights[0];
        int right = heights[heights.length-1];
        int l = 0;
        int r = heights.length - 1;
        while (l<r){
            if (heights[l]<heights[r]){
                int width = r-l;
                int area = heights[l]*width;
                max = Math.max(area,max);
                l++;
            }
            else{int width = r-l;
                int area = heights[r]*width;
                max = Math.max(area,max);
                r--;

            }
        }
        return max;
        
    }
}
