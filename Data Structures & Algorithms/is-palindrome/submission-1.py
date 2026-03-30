class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1 = []
        for char in s:
            if char.isalnum():
                l1.append(char.lower())
        if len(l1)==0:
            return True
        j=len(l1)-1
        for i in range(len(l1)):
            if l1[i]!=l1[j]:
                return False
            j -=1
        return True
        