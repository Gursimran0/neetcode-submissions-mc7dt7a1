class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int L = 0;
        int R = matrix.length-1;
        while(L<=R){
            int M = (L+R)/2;
            if (target<matrix[M][0]){
                 R = M-1;
            }
            else if (target>matrix[M][matrix[M].length-1]){
                L =M+1 ;
            }
            else{
                break;
            }
        }
        int l = 0 ;
        int r = matrix[(L+R)/2].length-1;
        int M = (L+R)/2;
        if (L>R){
            return false;
        }
        while(l<=r){
            int m = (l+r)/2;
            if (target>matrix[M][m]){
                l=m+1;
            }
            else if (target<matrix[M][m]){
                r=m-1;
            }
            else{
                return true;
            }
        }
        return false;
    }
}
