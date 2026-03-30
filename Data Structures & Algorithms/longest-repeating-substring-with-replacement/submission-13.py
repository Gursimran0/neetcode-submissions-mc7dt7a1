class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxF = 0
        res = 0
        l=0
        for r in range(len(s)):
            c=s[r]
            count[c] = 1+count.get(c,0)
            maxF = max(maxF,count[c])
            if (r-l+1-maxF)>k:
                count[s[l]]-=1
                l+=1
            res = max(r-l+1,res)
        return res

        