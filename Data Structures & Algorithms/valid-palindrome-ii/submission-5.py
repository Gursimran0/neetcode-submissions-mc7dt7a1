class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                sLeft = s[l+1:r+1]
                sRight = s[l:r]
                return sLeft == sLeft[::-1] or sRight == sRight[::-1]
            l+=1
            r-=1
        return True