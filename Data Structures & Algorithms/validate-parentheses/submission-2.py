class Solution:
    def isValid(self, s: str) -> bool:
        newS= list(s)
        newDict={")":"(","]":"[","}":"{"}
        emptyList=[]
        for i in s:
            if i in newDict:
                if (len(emptyList)>0 and emptyList[-1]==newDict[i]):
                    emptyList.pop()
                else:
                    return False
            else:
                emptyList.append(i)
        if len(emptyList)==0:
            return True
        return False



        