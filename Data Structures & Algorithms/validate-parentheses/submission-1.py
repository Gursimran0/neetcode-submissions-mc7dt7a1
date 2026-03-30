class Solution:
    def isValid(self, s: str) -> bool:
        thisDict = {")":"(",
                    "}":"{",
                    "]":"["}
        emptyList = []
        for i in s:
            if i in thisDict:
                if len(emptyList)>0 and emptyList[-1]==thisDict[i]:
                    emptyList.pop()
                else:
                    return False
            else:
                emptyList.append(i)
        if len(emptyList) ==0:
            return True
        else:
            return False 
      



