class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resSet = set()
        count = 0
        l=0
        for r in range(len(s)):
            while s[r] in resSet:
                resSet.remove(s[l])
                l+=1
            resSet.add(s[r])
            count = max(count,r-l+1)
        return count
