class Solution {
    public boolean isAnagram(String s, String t) {
        if((s.length())!=(t.length())){
            return false;
        }
        int[] res = new int[26];
        int index ;
        for (int i = 0;i<s.length();i++){
            res[s.charAt(i)-'a']+=1;
            res[t.charAt(i)-'a']-=1;

        }
        for (int i =0;i<26;i++){
            if (res[i]!=0){
                return false;
            }
        }
        return true;

    }
}
