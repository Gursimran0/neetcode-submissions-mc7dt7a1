class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        countS ={}
        countT = {}
        
        for elem in t:
            countT[elem]=1+countT.get(elem,0)
        need = len(countT)
        res = [-1,-1]
        resLen = float("infinity")
        l=0
        have =0
        for r in range(len(s)):
            c=s[r]
            countS[c] = 1 + countS.get(c,0)
            if c in countT and countT[c] == countS[c]:
                have +=1
            
            while have == need:
                if (r-l+1)<resLen:
                    resLen = r-l+1
                    res = [l,r]
                countS[s[l]]-=1
                if s[l] in countT and countS[s[l]]<countT[s[l]]:
                    have -=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float("infinity") else ""

            