class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(","}":"{","]":"["}
        for i in range(len(s)):
            if s[i]==")" or s[i] == "}" or s[i] == "]":
                if not stack or stack.pop()!=dic[s[i]]:
                    return False
            else:
                stack.append(s[i])
        
        return len(stack)==0
        