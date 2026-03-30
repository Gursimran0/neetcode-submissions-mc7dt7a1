class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in range(len(strs)):
            c = [0]*26
            for char in strs[i]:
                c[ord(char)-ord('a')]+=1
            count[tuple(c)].append(strs[i])
        return list(count.values())
        