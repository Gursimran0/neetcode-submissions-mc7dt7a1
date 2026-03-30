class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        sList = list(s)
        tList = list(t)
        for i in sList:
            if i in sDict.keys():
                sDict[i]+=1
            else:
                sDict[i]=1
        for i in tList:
            if i in tDict.keys():
                tDict[i]+=1
            else:
                tDict[i]=1
        return sDict == tDict
            

       