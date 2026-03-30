class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashDict = {}
        copyHash = {}
        for elem in s:
            if elem in hashDict.keys():
                hashDict[elem] +=1
            else:
                hashDict[elem]=1
        for elem in t:
            if elem in copyHash.keys():
                copyHash[elem] += 1
            else:
                copyHash[elem]=1
        return hashDict == copyHash
        