class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        counts2 = {}
        if (len(s2))<len(s1):
            return False
        for i in range(26):
            counts1[i] = 0
            counts2[i] = 0
        matches  = 0
        for i in range(len(s1)):
            counts1[ord(s1[i])-ord('a')] = 1 + counts1.get(ord(s1[i])-ord('a'),0)
            counts2[ord(s2[i])-ord('a')] = 1 + counts2.get(ord(s2[i])-ord('a'),0)
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches+=1
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            ind = ord(s2[r])-ord('a')
            counts2[ind] +=1
            if counts2[ind] == counts1[ind]:
                matches +=1
            elif counts2[ind]-1 == counts1[ind]:
                matches -=1
            ind = ord(s2[l])-ord('a')
            counts2[ind]-=1
            if counts2[ind] == counts1[ind]:
                matches +=1
            elif counts2[ind]+1 == counts1[ind]:
                matches -=1
            l+=1
        return matches == 26
