class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        res = [-1,-1]
        resLen = float("inf")
        countT = {}
        countS={}
        for i in range(len(t)):
            countT[t[i]] = 1+countT.get(t[i],0)
        l = 0
        need = len(countT)
        have = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c,0)

            if c in countT and countS[c] == countT[c]:
                have+=1
            
            while have == need:
                if r-l+1<resLen:
                    res = [l,r]
                    resLen = r-l+1
                countS[s[l]] -=1
                if s[l] in countT and countT[s[l]]>countS[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen < float("inf") else ""




        