class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> unique = new HashSet<>();
        for (int num:nums){
            unique.add(num);
        }
        int res = 0;
        for (int i =0;i<nums.length;i++){
            int check = nums[i];
            if (!unique.contains(check-1)){
                int length =1;
                while(unique.contains(check+length)){
                    length ++;
                }
                res=Math.max(length,res);
            }
        }
        return res;
        
    }
}
