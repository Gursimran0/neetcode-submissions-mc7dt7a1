class Solution {
    private Set<List<Integer>> res;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        res = new HashSet<>();
        Arrays.sort(candidates);
        List<Integer> curr = new ArrayList<>();
        dfs(candidates,target,0,curr,0);
        return new ArrayList<>(res);
    }
    private void dfs(int[] candidates,int target,int i, List<Integer> curr, int total){
        if (total==target){
            res.add(new ArrayList<>(curr));
            return;
        }
        if (total>target || i>=candidates.length){
            return;
        }
        curr.add(candidates[i]);
        dfs(candidates,target,i+1,curr,total+candidates[i]);
        curr.remove(curr.size()-1);
        dfs(candidates,target,i+1,curr,total);

    }
}
