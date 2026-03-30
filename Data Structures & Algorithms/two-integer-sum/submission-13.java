class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] res = new int[nums.length];

        for (int i = 0;i<nums.length;i++){
            Integer newTarget = target - nums[i];
            for (int j = i+1 ; j<nums.length;j++){
                if (nums[j] == newTarget){
                    return new int[]{i,j};
                }
            }
        }return new int[0];
        
    }
}
