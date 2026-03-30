class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        count = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l+=1
            
            charSet.add(s[i])
            count = max(count,i-l+1)
        return count


