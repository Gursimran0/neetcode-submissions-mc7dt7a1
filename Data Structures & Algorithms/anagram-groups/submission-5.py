class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for elem in strs:
            count = [0]*26
            for i in (elem):
                count[ord(i)-ord('a')] += 1
            hashMap[tuple(count)].append(elem)
        return list(hashMap.values())