class Solution {
    public int missingNumber(int[] nums) {
        int total=0;
        int res;
        int len = nums.length;
        for(int i =0;i<=len;i++){
            total = total + i;
        }
        for(int i =0;i<nums.length;i++){
            total = total - nums[i];
        }
        return total;
    }
}
