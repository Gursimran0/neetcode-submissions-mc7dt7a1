class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cou = {}
        for elem in strs:
            count = [0]*26
            for char in elem:
                count[ord(char)-ord('a')] +=1
            if tuple(count) in cou.keys():
                cou[tuple(count)].append(elem)
            else:
                cou[tuple(count)] = [elem]
        return list(cou.values())
        