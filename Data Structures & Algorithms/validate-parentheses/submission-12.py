class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(","}":"{","]":"["}
        for i in range(len(s)):
            if s[i]==")" or s[i] == "}" or s[i] == "]":
                if stack and stack[-1]==dic[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return len(stack)==0
        