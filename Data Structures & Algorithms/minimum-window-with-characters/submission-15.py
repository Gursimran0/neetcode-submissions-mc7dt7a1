class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)>len(s):
            return ""
        
        res = [-1,-1]
        resLen = float("inf")
        countT = {}
        countS = {}
        for i in range(len(t)):
            countT[t[i]] =  1 + countT.get(t[i],0)
        
        need = len(countT)
        l = 0
        have = 0 
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have +=1
            
            while have == need:
                if (r-l+1)<resLen:
                    resLen = r-l+1
                    res = [l,r]
                
                countS[s[l]]-=1
                if s[l] in countT and countS[s[l]]<countT[s[l]]:
                     have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen <float("inf") else ""
            



