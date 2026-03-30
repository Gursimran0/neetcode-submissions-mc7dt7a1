class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        countCheck = {}
        for i in range(len(s1)):
            countCheck[s1[i]] = 1 + countCheck.get(s1[i],0)
        while r<=len(s2):
            countS2={}
            newString  = s2[l:r]
            for i in range(len(newString)):
                countS2[newString[i]] = 1+countS2.get(newString[i],0)
            if countS2==countCheck:
                return True
            l+=1
            r+=1
        return False
            
        