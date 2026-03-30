class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> prefix = new HashMap<>();
        prefix.put(0,1);
int res = 0;
int cSum = 0;
        System.out.print(prefix);
        for (int i = 0;i<nums.length;i++){
            cSum += nums[i];
            int diff = cSum - k;
            res+= prefix.getOrDefault(diff,0);
            prefix.put(cSum,prefix.getOrDefault(cSum,0)+1);
        }
        
        return res;
        
    }
}