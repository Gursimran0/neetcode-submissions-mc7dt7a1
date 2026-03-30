class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
       
        for elem in strs:
            count = [0]*26
            for char in elem:
                count[ord(char)-ord('a')] +=1
            result[tuple(count)].append(elem)
        return list(result.values())