class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        dfs(res,curr,0,nums,0,target);
        return res;
        
    }
    private void dfs(List<List<Integer>> res, List<Integer> curr, int i,int [] nums,int total,int target){
        if (i>=nums.length || total>target){
            return;
        }
        if (total == target){
            res.add(new ArrayList<>(curr));
            return;
        }
        curr.add(nums[i]);
        dfs(res,curr,i,nums,total+nums[i],target);
        curr.remove(curr.size()-1);
        dfs(res,curr,i+1,nums,total,target);
    }
}
