class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for elem in strs:
            count = [0] * 26
            for char in elem:
                count[ord(char)-ord('a')] += 1
            res[tuple(count)].append(elem)
        return list(res.values())
        

        