class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        HashMap<Integer,Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];
        for (int i = 0 ; i<freq.length; i++){
            freq[i] = new ArrayList();
        }
        for (int i = 0;i<nums.length;i++){
            count.put(nums[i],1+count.getOrDefault(nums[i],0));
        }
        for (int num : count.keySet()){
            int t = count.get(num);
            freq[t].add(num);
        }
        int index = 0;
        for (int i = freq.length-1;i>0 && index<k;i--){
            for(int n:freq[i]){
                res[index++]=n;
                if (index == k){
                    return res;
                }
            }
        }
        return res;
    
    }
    
}
