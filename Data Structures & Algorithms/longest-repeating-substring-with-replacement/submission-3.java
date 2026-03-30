class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character,Integer> count = new HashMap<>();
        int res = 0;
        int maxF = 0;
        int l = 0;

        for (int r=0;r<s.length();r++){
            count.put(s.charAt(r),1+count.getOrDefault(s.charAt(r),0));
            maxF = Math.max(maxF,count.get(s.charAt(r)));
            while(r-l+1 - maxF>k){
                count.put(s.charAt(l),count.getOrDefault(s.charAt(l),0)-1);
                l++;
            }
            res = Math.max(maxF,r-l+1);
        }return res;
        
    }
}
