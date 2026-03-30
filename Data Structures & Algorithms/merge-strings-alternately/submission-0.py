class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i=0
        r=0
        l = min(len(word1),len(word2))
        while i<l and r<l:
            res +=word1[i]
            res+=word2[r]
            i+=1
            r+=1
        
        if len(word1)>l:
            res+=word1[i:]
        if len(word2)>l:
            res+=word2[r:]   

        return res   