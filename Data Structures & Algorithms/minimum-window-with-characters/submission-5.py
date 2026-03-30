class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = {}
        countT = {}
        l = 0 
        
        for r in range(len(t)):
            countT[t[r]] = 1+countT.get(t[r],0)
        
        need = len(countT)
        have = 0
        resLen = float("infinity")
        res = [-1,-1]
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1+countS.get(c,0)
            if c in countT  and countS[c] == countT[c]:
                have  +=1

            while have == need:
                if r-l+1<resLen:
                    res = [l,r]
                    resLen = r-l+1
                countS[s[l]]-=1
                if s[l] in countT and countT[s[l]]>countS[s[l]]:
                    have -=1
                l+=1
            
        l,r = res
        print(res)
        return s[l:r+1] if resLen<float("infinity") else ""

