class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        HashMap<Character,Integer> sHashmap = new HashMap<>();
        HashMap<Character,Integer> tHashmap = new HashMap<>();

        for (int i =0;i<s.length();i++){
            sHashmap.put(s.charAt(i),1+sHashmap.getOrDefault(s.charAt(i),0));
            tHashmap.put(t.charAt(i),1+tHashmap.getOrDefault(t.charAt(i),0));
        }
        return sHashmap.equals(tHashmap);
        }

    }

