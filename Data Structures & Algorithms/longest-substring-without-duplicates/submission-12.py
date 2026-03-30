class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resSet = set()
        l=0
        
        res = 0
        for r in range(len(s)):
            while s[r] in resSet:
                resSet.remove(s[l])
                l+=1
            resSet.add(s[r])
            res = max(res,r-l+1)
        return res
        