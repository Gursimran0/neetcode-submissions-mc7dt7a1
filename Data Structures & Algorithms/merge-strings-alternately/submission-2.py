class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0 
        m = 0
        res = ""

        while l<len(word1) and m<len(word2):
            res+= word1[l]
            res+=word2[m]
            l+=1
            m+=1
        if l<len(word1):
            res+=word1[l:]
        if m<len(word2):
            res+=word2[m:]
        return res