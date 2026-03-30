class Solution {
    public boolean isValid(String s) {
        HashMap<Character,Character> keyDict = new HashMap<>();
        keyDict.put('}','{');
        keyDict.put(']','[');
        keyDict.put(')','(');
        Stack<Character> stack = new Stack<>();
        for (int i =0;i<s.length();i++){
            if (keyDict.containsKey(s.charAt(i))){
                if (stack.size()!=0 && stack.peek() == keyDict.get(s.charAt(i))){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.add(s.charAt(i));
            }

        }
        return stack.size() == 0;
        
    }
}
