class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = {}
        countT ={}
        if len(t)>len(s):
            return ""

        resLen = float("inf")
        res = [-1,-1]
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        need = len(countT)
        have = 0
        l=0
        for r in range(len(s)):
            c=s[r]
            countS[c] = 1+countS.get(c,0)
            if c in countT and countT[c] == countS[c]:
                have +=1
            while have == need:
                if r-l+1<resLen:
                    res = [l,r] 
                    resLen=r-l+1
                countS[s[l]]-=1
                if s[l] in countT and countS[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen<float("inf") else ""
        