class Solution:
    def isValid(self, s: str) -> bool:
        newKey = {'}':'{',']':'[',')':'('}

        stack  = []

        for elem in s:
            if elem in newKey.keys():
                if len(stack)!=0 and stack[-1] == newKey[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        return len(stack) == 0
        