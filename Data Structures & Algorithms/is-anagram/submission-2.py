class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSetS = {}
        hashSetT = {}

        for elem in s:
            if elem in hashSetS:
                hashSetS[elem]+=1
            else:
                hashSetS[elem]=1
        for elem in t:
            if elem in hashSetT:
                hashSetT[elem]+=1
            else:
                hashSetT[elem]=1
        
        if hashSetS == hashSetT:
            return True
        return False